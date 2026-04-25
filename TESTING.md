# Minishell Testing Guide

This suite is designed to verify that `minishell` behaves identically to `bash`. It includes automated output comparison, interactive session simulation, and signal handling verification.

## 🚀 Quick Start

To run the tests, use the main menu script:

```bash
bash tester/run_tests.sh
```

### 📋 Available Options
When you run the script, you will see the following menu:

**Interactive Sessions:**
- `1)` Mandatory tests with **Bash** (generate logs)
- `2)` Mandatory tests with **Minishell** (generate logs)
- `3)` Bonus tests with **Bash**
- `4)` Bonus tests with **Minishell**

**Comparisons & Reports:**
- `5)` Compare **Mandatory** results (Generates `.txt` and `.md` reports)
- `6)` Compare **Bonus** results (Generates `.txt` and `.md` reports)

**Other Tests:**
- `7)` Run **Non-Interactive** tests (Script-based comparison)
- `8)` Test **Exit Codes & Signals** (Ctrl+C, Ctrl+\, Ctrl+D)

**Automated Suites:**
- `9)` **Run ALL Mandatory**: Runs 1, 2, 5, 7, 8 and combines them into `Mandatory_tests.md`.
- `10)` **Run ALL Bonus**: Runs 3, 4, 6, 7, 8 and combines them into `Bonus_tests.md`.

### Demo
<p align="center">
  <img src="tester/minishell.gif" alt="Minishell Demo" width="800">
</p>

---

## 📊 Current Status (Non-Interactive)
Example of the output from `run_noninteractive_tests.py`:

```text
==============================================================
 Minishell Test Runner (Markdown Mode)
 Binary    : /app/minishell
 Test Dir  : /app/non_interactive
==============================================================

[PASS] 00_echo
[PASS] 01_cd_pwd
[PASS] 02_export_unset_env
[PASS] 03_external
[PASS] 04_pipes
[PASS] 05_quotes_and_expansion
[PASS] 06_redirections
[PASS] 07_heredoc
[PASS] 08_bonus_wildcards
[PASS] 09_bonus_logical_operators
[PASS] 10_bonus_pipe_consec1
[PASS] 11_pipe_consec2
[PASS] 12_pipe_leading
[FAIL] 13_pipe_trailing_dif_behaviour
[PASS] 15_exit

14 Pass | 1 Fail | 0 Skip. Report: results/noninteractive_comparison.md
```

---

## 🛠️ Detailed Component Breakdown

### 1. Non-Interactive Tests (`utils/run_noninteractive_tests.py`)
Compares the output of `.sh` files in `tester/non_interactive/`.
- **Environment Variables**:
  - `FILTER`: Run only tests matching this string.
  - `EXCLUDE`: Skip tests matching this string.
  - `TIMEOUT`: Execution limit (default 5s).
- **Report**: `tester/results/noninteractive_comparison.md` (Padded columns for readability).

### 2. Interactive Tests (`utils/tester.exp` & `utils/compare_interactive_results.py`)
Simulates a real user typing in the terminal.
- **Workflow**: 
  1. Generate logs for Bash and Minishell.
  2. The comparison script identifies differences and generates a Markdown table.
- **Features**: Columns are hard-wrapped (25 chars) and padded to ensure consistent width in GitHub previews.
- **Reports**: `tester/results/comparison_interactive_[mandatory|bonus].md`

### 3. Signal and Exit Code Tests (`utils/test_exit_codes_signals.sh`)
Automated verification of signal handling.
- **Tests**: SIGINT/SIGQUIT in child processes and SIGINT in the idle shell.
- **Report**: `tester/results/signals_comparison.md`

### 4. Combined Reports (`utils/combine_md_reports.py`)
Merging logic used by the Automated Suites to create a single source of truth.
- **Output**: `tester/Mandatory_tests.md` or `tester/Bonus_tests.md`.

---

## 📂 Directory Structure
- `tester/non_interactive/`: Test source scripts.
- `tester/results/`: Raw logs and individual reports.
- `tester/utils/`: Core logic and helper scripts.
- `Mandatory_tests.md`: Consolidated mandatory report.
- `Bonus_tests.md`: Consolidated bonus report.
