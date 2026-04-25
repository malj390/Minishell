#!/bin/bash
# ==============================================================================
# 19_exit_codes_signals.sh — Signal-based exit code tests
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"
RESULTS_DIR="$BASE_DIR/results"
MD_FILE="$RESULTS_DIR/signals_comparison.md"

mkdir -p "$RESULTS_DIR"

# Binary discovery
if [ -x "$BASE_DIR/parent/minishell" ]; then
    MINISHELL="$BASE_DIR/parent/minishell"
elif [ -x "$BASE_DIR/minishell" ]; then
    MINISHELL="$BASE_DIR/minishell"
elif [ -x "$(dirname "$BASE_DIR")/minishell" ]; then
    MINISHELL="$(dirname "$BASE_DIR")/minishell"
else
    echo "ERROR: minishell binary not found."
    exit 1
fi

RED="\033[31m"; GREEN="\033[32m"; YELLOW="\033[33m"; RESET="\033[0m"
PASS=0; FAIL=0

# Prepare Markdown
echo "# Signal and Exit Code Test Results" > "$MD_FILE"
echo "" >> "$MD_FILE"
echo "| Status | Test Description | Expected | Got |" >> "$MD_FILE"
echo "| :---: | :--- | :---: | :---: |" >> "$MD_FILE"

pass() { 
    echo -e "${GREEN}[PASS]${RESET} $1"
    echo "| ✅ | $1 | $2 | $3 |" >> "$MD_FILE"
    ((PASS++))
}
fail() { 
    echo -e "${RED}[FAIL]${RESET} $1 — expected: $2  got: $3"
    echo "| ❌ | $1 | $2 | $3 |" >> "$MD_FILE"
    ((FAIL++))
}
info() { echo -e "${YELLOW}[INFO]${RESET} $1"; }

# ==============================================================================
# Helper: run a two-command session in minishell (non-interactive) via a FIFO.
# ==============================================================================
run_signal_test()
{
    local signal="$1"
    local child_cmd="$2"
    local fifo
    fifo=$(mktemp -u /tmp/ms_sig_test_XXXXXX)
    mkfifo "$fifo"

    (
        echo "$child_cmd"
        sleep 0.6
        echo 'echo $?'
        sleep 0.2
    ) > "$fifo" &
    WRITER_PID=$!

    "$MINISHELL" < "$fifo" > /tmp/ms_sig_out 2>/dev/null &
    MINI_PID=$!

    sleep 0.3
    CHILD_PIDS=$(pgrep -P "$MINI_PID" 2>/dev/null)

    if [ -n "$CHILD_PIDS" ]; then
        for cpid in $CHILD_PIDS; do
            kill "-$signal" "$cpid" 2>/dev/null
        done
    else
        kill "-$signal" "$MINI_PID" 2>/dev/null
    fi

    wait "$MINI_PID" 2>/dev/null
    wait "$WRITER_PID" 2>/dev/null
    rm -f "$fifo"

    RESULT_CODE=$(grep -oE '^[0-9]+$' /tmp/ms_sig_out | tail -1)
    rm -f /tmp/ms_sig_out
}

echo ""
echo "========================================"
echo " Automated signal exit-code tests"
echo "========================================"
echo ""

# --- Test 1: SIGINT to child process ---
info "Sending SIGINT to child (sleep 30) inside minishell ..."
run_signal_test "SIGINT" "sleep 30"
if [ "$RESULT_CODE" = "130" ]; then
    pass "SIGINT in child process" "130" "$RESULT_CODE"
else
    fail "SIGINT in child process" "130" "${RESULT_CODE:-<no output>}"
fi

# --- Test 2: SIGQUIT to child process ---
info "Sending SIGQUIT to child (sleep 30) inside minishell ..."
run_signal_test "SIGQUIT" "sleep 30"
if [ "$RESULT_CODE" = "131" ]; then
    pass "SIGQUIT in child process" "131" "$RESULT_CODE"
else
    fail "SIGQUIT in child process" "131" "${RESULT_CODE:-<no output>}"
fi

# --- Test 3: SIGINT to minishell itself ---
info "Sending SIGINT to minishell (interactive mode, no child) ..."
fifo3=$(mktemp -u /tmp/ms_sigself_XXXXXX)
mkfifo "$fifo3"
sleep 10 > "$fifo3" &
WRITER3_PID=$!
"$MINISHELL" < "$fifo3" > /dev/null 2>&1 &
MINI_PID=$!
sleep 0.2
kill -SIGINT "$MINI_PID" 2>/dev/null
wait "$MINI_PID" 2>/dev/null
EXIT_STATUS=$?
kill "$WRITER3_PID" 2>/dev/null
wait "$WRITER3_PID" 2>/dev/null
rm -f "$fifo3"
if [ "$EXIT_STATUS" = "130" ]; then
    pass "SIGINT to minishell itself" "130" "$EXIT_STATUS"
else
    fail "SIGINT to minishell itself" "130" "$EXIT_STATUS"
fi

echo ""
echo "========================================"
echo " Results: $PASS passed, $FAIL failed"
echo " Report saved to: $MD_FILE"
echo "========================================"

exit $((FAIL > 0 ? 1 : 0))
