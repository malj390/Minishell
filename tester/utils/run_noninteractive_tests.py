#!/usr/bin/env python3
import sys
import os
import re
import subprocess
from pathlib import Path

# ---------------------------------------------------------------------------
# Config and Setup
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent # Points to tester/
TIMEOUT_S = int(os.environ.get("TIMEOUT", 5))
VERBOSE = os.environ.get("VERBOSE") == "1"
FILTER_STR = os.environ.get("FILTER", "")
EXCLUDE_STR = os.environ.get("EXCLUDE", "")
TEST_DIR = BASE_DIR / "non_interactive"

# Binary discovery
if (BASE_DIR.parent / "minishell").exists():
    MINISHELL = str(BASE_DIR.parent / "minishell")
elif (BASE_DIR / "minishell").exists():
    MINISHELL = str(BASE_DIR / "minishell")
else:
    print(f"ERROR: minishell binary not found in {BASE_DIR} or {BASE_DIR.parent}")
    sys.exit(1)

# Terminal output colors (for the live console only)
T_GREEN = "\033[32m"; T_RED = "\033[31m"; T_RESET = "\033[0m"

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def normalize(lines):
    out = []
    for ln in lines:
        ln = re.sub(r'^bash: ', 'shell: ', ln)
        ln = re.sub(r'^minishell: ', 'shell: ', ln)
        ln = re.sub(r'^shell: line \d+: ', 'shell: ', ln)
        ln = re.sub(r'^shell: command not found: (.+)', r'shell: \1: command not found', ln)
        ln = re.sub('/usr/bin/python3', '/usr/bin/env', ln)
        if ln.strip():
            out.append(ln)
    return out

def parse_commands(path):
    commands, current = [], []
    in_heredoc, hd_delim = False, None
    try:
        with open(path, errors='replace') as f:
            for raw in f:
                raw = raw.rstrip('\n')
                stripped = raw.strip()
                if in_heredoc:
                    current.append(raw)
                    if stripped == hd_delim:
                        in_heredoc = False
                        commands.append('\n'.join(current))
                        current = []
                    continue
                if not stripped or stripped.startswith('#'): continue
                current.append(raw)
                m = re.search(r'<<-?\s*[\'"]?(\w+)[\'"]?', raw)
                if m:
                    in_heredoc, hd_delim = True, m.group(1)
                    continue
                if raw.rstrip().endswith('\\'): continue
                commands.append('\n'.join(current))
                current = []
        if current: commands.append('\n'.join(current))
    except FileNotFoundError: return []
    return commands

def build_marked_script(commands):
    parts = []
    for i, cmd in enumerate(commands):
        parts.append(f'echo ___CMD_{i}___')
        parts.append(cmd)
        parts.append(f"/usr/bin/printf '\\n___END_{i}___\\n'")
    parts.append(f'echo ___CMD_{len(commands)}___')
    return '\n'.join(parts)

def run_shell(shell, script, timeout):
    try:
        p = subprocess.run(
            [shell], input=script.encode(),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            timeout=timeout,
        )
        return p.stdout.decode(errors='replace'), p.returncode, False
    except subprocess.TimeoutExpired: return '', 124, True

def split_by_markers(raw, num_cmds):
    buckets, cur, collecting = [[] for _ in range(num_cmds)], -1, False
    for line in raw.splitlines():
        m_cmd = re.fullmatch(r'___CMD_(\d+)___', line)
        m_end = re.fullmatch(r'___END_(\d+)___', line)
        if m_cmd:
            cur = int(m_cmd.group(1))
            collecting = (cur < num_cmds)
        elif m_end: collecting, cur = False, -1
        elif collecting and 0 <= cur < num_cmds: buckets[cur].append(line)
    return [normalize(b) for b in buckets]

# ---------------------------------------------------------------------------
# Main Execution
# ---------------------------------------------------------------------------

if not TEST_DIR.exists():
    print(f"ERROR: Directory {TEST_DIR} not found.")
    sys.exit(1)

scripts = sorted(f for f in os.listdir(TEST_DIR) if re.match(r'\d\d_.*\.sh$', f))
PASS = FAIL = SKIP = 0
sections = []

print("=" * 62)
print(f" Minishell Test Runner (Markdown Mode)")
print(f" Binary    : {MINISHELL}")
print(f" Test Dir  : {TEST_DIR}")
print("=" * 62 + "\n")

for script_name in scripts:
    name = script_name[:-3]
    if FILTER_STR and FILTER_STR not in name:
        SKIP += 1
        continue
    if EXCLUDE_STR and EXCLUDE_STR in name:
        SKIP += 1
        continue

    path = TEST_DIR / script_name
    commands = parse_commands(path)
    if not commands: continue

    use_ec = 'exit' in name
    marked = build_marked_script(commands)
    bash_raw, bash_ec, bash_to = run_shell('bash', marked, TIMEOUT_S)
    ms_raw, ms_ec, ms_to = run_shell(MINISHELL, marked, TIMEOUT_S)

    if ms_to:
        print(f"{T_RED}[FAIL] {name}  -- TIMEOUT{T_RESET}")
        FAIL += 1
        continue

    bash_bkts = split_by_markers(bash_raw, len(commands))
    ms_bkts = split_by_markers(ms_raw, len(commands))

    out_ok = (bash_bkts == ms_bkts)
    ec_ok = (not use_ec) or (bash_ec == ms_ec)

    if out_ok and ec_ok:
        print(f"{T_GREEN}[PASS] {name}{T_RESET}")
        PASS += 1
        status = "PASS"
    else:
        print(f"{T_RED}[FAIL] {name}{T_RESET}")
        FAIL += 1
        status = "FAIL"
    sections.append((name, commands, bash_bkts, ms_bkts, bash_ec, ms_ec, status))

def wrap(text: str, width: int) -> list[str]:
    if not text: return ['']
    result = []
    for line in text.split('\n'):
        if not line:
            result.append('')
            continue
        while len(line) > width:
            result.append(line[:width])
            line = line[width:]
        result.append(line)
    return result or ['']

def format_md_cell(text, width):
    if not text:
        return f"`{' ' * width}`"
    text = text.replace('|', '\\|')
    lines = wrap(text, width)
    return '<br>'.join([f"`{l:<{width}}`" for l in lines])

# ---------------------------------------------------------------------------
# Generate noninteractive_comparison.md (MARKDOWN FORMAT)
# ---------------------------------------------------------------------------
lines_out = ["# Minishell Non-Interactive Test Results", ""]
lines_out.append(f"**Legend:** Status ❌ indicates a mismatch in output or exit code.")
lines_out.append("")

for name, commands, bash_bkts, ms_bkts, b_ec, m_ec, status in sections:
    lines_out.append(f"## {name} ({status})")
    lines_out.append(f"- Bash Exit: `{b_ec}` | Minishell Exit: `{m_ec}`")
    lines_out.append("")
    
    lines_out.append("| Status | Command | Bash Output | Minishell Output |")
    lines_out.append("| :---: | :--- | :--- | :--- |")

    MD_W = 25
    for i, cmd in enumerate(commands):
        bout = "\n".join(bash_bkts[i])
        mout = "\n".join(ms_bkts[i])
        
        cmd_ok = (bash_bkts[i] == ms_bkts[i])
        st = "✅" if cmd_ok else "❌"
        
        c_cell = format_md_cell(cmd, MD_W)
        b_cell = format_md_cell(bout, MD_W)
        m_cell = format_md_cell(mout, MD_W)
        
        lines_out.append(f"| {st} | {c_cell} | {b_cell} | {m_cell} |")
    
    lines_out.append("")

# Save as .md file
out_path = BASE_DIR / "results" / "noninteractive_comparison.md"
with open(out_path, "w") as f:
    f.write("\n".join(lines_out))

print(f"\n{PASS} Pass | {FAIL} Fail | {SKIP} Skip. Report: results/noninteractive_comparison.md")