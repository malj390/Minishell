#!/usr/bin/env python3
"""
compare_results.py

Reads result_interactive_bash.log and result_interactive_minishell.log (produced by tester.exp)
and generates comparison_interactive.txt or comparison_noninteractive.txt with 3 columns:
  INPUT | BASH output | MINISHELL output

Lines where outputs differ are marked with !! at the left edge.

Usage:
    python3 compare_results.py
"""

import re
import sys
import os

# ── Config ────────────────────────────────────────────────────────────────────

# Detect mode (interactive/noninteractive) and type (mandatory/bonus)
mode = 'interactive'
test_type = 'mandatory'

if len(sys.argv) > 1:
    mode = sys.argv[1] # 'interactive' o 'noninteractive'
if len(sys.argv) > 2:
    test_type = sys.argv[2] # 'mandatory' o 'bonus'

# Paths relative to tester/ directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASH_LOG = os.path.join(BASE_DIR, f'results/result_{mode}_{test_type}_bash.log')
MINI_LOG = os.path.join(BASE_DIR, f'results/result_{mode}_{test_type}_minishell.log')
OUT_FILE  = os.path.join(BASE_DIR, f'results/comparison_{mode}_{test_type}.txt')
MD_FILE   = os.path.join(BASE_DIR, f'results/comparison_{mode}_{test_type}.md')
FAILS_FILE = os.path.join(BASE_DIR, f'results/comparison_{mode}_{test_type}_fails.txt')
MD_FAILS_FILE = os.path.join(BASE_DIR, f'results/comparison_{mode}_{test_type}_fails.md')

BASH_PROMPT = "bash$> "
MINI_PROMPT = "Minishell$> "

COL_W = 20          # width of each of the 3 data columns
MARK_OK   = "   "   # prefix when outputs match
MARK_DIFF = "!! "   # prefix when outputs differ

# ANSI colour codes (visible with less -R)
RED   = "\x1b[31m"
RESET = "\x1b[0m"

# ── Helpers ───────────────────────────────────────────────────────────────────
ANSI_RE = re.compile(r'\x1b\[[0-9;]*[mKHJABCDEFGnsuhl]|\x07')

def strip_ansi(s: str) -> str:
    return ANSI_RE.sub('', s)


def parse_log(path: str, prompt: str) -> list[tuple[str, str]]:
    """
    Split log on `prompt` occurrences and return list of (cmd, output) pairs.
    Each element after the prompt up to the next prompt is one entry.
    """
    if not os.path.exists(path):
        print(f"ERROR: {path} not found. Run tester.exp first.", file=sys.stderr)
        sys.exit(1)

    with open(path, errors='replace') as f:
        raw = f.read()

    text = strip_ansi(raw)

    # Remove PS1 assignment lines so that "PS1=bash$> " in env output is never
    # mistaken for a real prompt, then split on the prompt everywhere — including
    # mid-line after echo -n output (which produces no trailing newline).
    text = re.sub(r'(?m)^PS1=.*\n?', '', text)
    parts = re.split(re.escape(prompt), text)

    entries = []
    for part in parts[1:]:          # skip preamble before first prompt
        nl = part.find('\n')
        if nl == -1:
            cmd, out = part.strip(), ''
        else:
            cmd = part[:nl].strip()
            out = part[nl+1:].rstrip('\n')
        entries.append((cmd, out))

    return entries


def wrap(text: str, width: int) -> list[str]:
    """Hard-wrap text to lines of at most `width` chars."""
    if not text:
        return ['']
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


def normalize_for_cmp(text: str) -> str:
    """Replace shell-name prefixes so 'bash: msg' and 'minishell: msg' compare equal.
    Also strip log file names so ls output doesn't differ between runs.
    Also strip Ubuntu's sudo hint that bash prints when spawned interactively.
    Also normalize sub-bash prompts (user@host:path$) to bash$>."""
    # Remove terminal title sequences (e.g. '\x1b]0;user@host:/path\x07')
    text = re.sub(r'\x1b\]0;[^\x07]*\x07', '', text)
    # Remove all prompts like 'user@host:/path$' (including test_ls_syntax and any path)
    text = re.sub(r'[a-zA-Z0-9_][\w-]*@[a-zA-Z0-9][\w-]*:[~\w./-]*\$ ?', '', text)
    # Remove all prompts like 'user@host:/path$' at line start (for extra safety)
    text = re.sub(r'^.*@[a-zA-Z0-9][\w-]*:[~\w./-]*\$ ?', '', text, flags=re.MULTILINE)
    # Replace shell-name prefixes
    text = re.sub(r'^bash: ', 'shell: ', text, flags=re.MULTILINE)
    text = re.sub(r'^minishell: ', 'shell: ', text, flags=re.MULTILINE)
    # Remove log file names
    text = re.sub(r'\b' + re.escape(BASH_LOG) + r'\b', '', text)
    text = re.sub(r'\b' + re.escape(MINI_LOG) + r'\b', '', text)
    # Strip Ubuntu's sudo hint block
    text = re.sub(
        r'To run a command as administrator.*?See "man sudo_root" for details\.\n?',
        '', text, flags=re.DOTALL
    )
    # Remove all prompts (bash$>, Minishell$>) at line start
    text = re.sub(r'^(bash\$>|Minishell\$>)\s*', '', text, flags=re.MULTILINE)
    # Normalize whitespace: replace tabs with spaces, collapse multiple spaces/tabs
    text = text.replace('\t', ' ')
    text = re.sub(r' +', ' ', text)
    # Remove trailing spaces on each line
    text = '\n'.join([line.rstrip() for line in text.split('\n')])
    return text


def render_row(mark: str, col1: list[str], col2: list[str], col3: list[str], colour: str = '') -> list[str]:
    """Render a multi-line table row into a list of strings."""
    n = max(len(col1), len(col2), len(col3))
    col1 = col1 + [''] * (n - len(col1))
    col2 = col2 + [''] * (n - len(col2))
    col3 = col3 + [''] * (n - len(col3))
    lines = []
    reset = RESET if colour else ''
    for i in range(n):
        pfx = mark if i == 0 else '   '
        line = f"{pfx}| {col1[i]:<{COL_W}} | {col2[i]:<{COL_W}} | {col3[i]:<{COL_W}} |"
        lines.append(f"{colour}{line}{reset}" if colour else line)
    return lines


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    bash_entries = parse_log(BASH_LOG,  BASH_PROMPT)
    mini_entries = parse_log(MINI_LOG,  MINI_PROMPT)

    n = max(len(bash_entries), len(mini_entries))

    sep    = '+' + ('-' * (COL_W + 2) + '+') * 3
    header = render_row(
        '   ',
        wrap('INPUT', COL_W),
        wrap('BASH', COL_W),
        wrap('MINISHELL', COL_W)
    )

    matches   = 0
    total     = 0
    diff_cmds = []
    fail_rows = []   # collect rows for the fails-only file
    md_rows = []     # collect rows for the markdown file

    with open(OUT_FILE, 'w') as out:
        out.write(sep + '\n')
        for line in header:
            out.write(line + '\n')
        out.write(sep + '\n')

        for i in range(n):
            b_cmd, b_out = bash_entries[i] if i < len(bash_entries) else ('', '')
            m_cmd, m_out = mini_entries[i] if i < len(mini_entries) else ('', '')

            cmd  = b_cmd or m_cmd
            b_out_norm = normalize_for_cmp(b_out)
            m_out_norm = normalize_for_cmp(m_out)
            same = (b_out_norm.rstrip() == m_out_norm.rstrip())
            mark = MARK_OK if same else MARK_DIFF
            colour = '' if same else RED

            if same:
                matches += 1
            else:
                diff_cmds.append(cmd)
            total += 1

            row_lines = render_row(
                mark,
                wrap(cmd,        COL_W),
                wrap(b_out_norm, COL_W),
                wrap(m_out_norm, COL_W),
                colour=colour,
            )
            for line in row_lines:
                out.write(line + '\n')
            out.write(sep + '\n')

            # Prepare Markdown row (with wrapping and escaping for better readability)
            status_md = "✅" if same else "❌"
            
            def format_md_cell(text, width):
                if not text:
                    return f"`{' ' * width}`"
                # Escape pipes for MD tables and clean up newlines
                text = text.replace('|', '\\|').replace('\n', ' ')
                lines = wrap(text, width)
                # Wrap each individual line in backticks and pad for consistent width
                return '<br>'.join([f"`{l:<{width}}`" for l in lines])

            MD_COL_W = 25 # Narrower width to ensure it fits on screen
            cmd_wrapped = format_md_cell(cmd, MD_COL_W)
            b_out_wrapped = format_md_cell(b_out_norm, MD_COL_W)
            m_out_wrapped = format_md_cell(m_out_norm, MD_COL_W)
            
            md_rows.append(f"| {status_md} | {cmd_wrapped} | {b_out_wrapped} | {m_out_wrapped} |")

            if not same:
                fail_rows.append((row_lines, sep))

    # Write Markdown file
    md_header = [
        f"# Interactive Comparison ({mode} - {test_type})",
        "",
        f"**Results:** {matches}/{total} match | {total - matches} differ",
        "",
        "| Status | Input | Bash Output | Minishell Output |",
        "| :---: | :--- | :--- | :--- |"
    ]
    with open(MD_FILE, 'w') as out:
        out.write('\n'.join(md_header) + '\n')
        out.write('\n'.join(md_rows) + '\n')

    # Write fails-only file
    with open(FAILS_FILE, 'w') as out:
        out.write(sep + '\n')
        for line in header:
            out.write(line + '\n')
        out.write(sep + '\n')
        for row_lines, s in fail_rows:
            for line in row_lines:
                out.write(line + '\n')
            out.write(s + '\n')

    # Write Markdown fails-only file
    with open(MD_FAILS_FILE, 'w') as out:
        out.write('\n'.join(md_header[:2]) + " (Fails Only)\n\n")
        out.write('\n'.join(md_header[2:]) + '\n')
        for i, row in enumerate(md_rows):
            if "❌" in row:
                out.write(row + '\n')

    # Summary
    print(f"\n{OUT_FILE} written.")
    print(f"{MD_FILE} written.")
    print(f"{FAILS_FILE} written ({len(fail_rows)} failures).")
    print(f"{MD_FAILS_FILE} written.")
    print(f"Results: {matches}/{total} match  |  {total - matches} differ\n")
    if diff_cmds:
        print("Commands with different output:")
        for c in diff_cmds:
            print(f"  !! {c}")


if __name__ == '__main__':
    main()
