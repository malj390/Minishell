# 🛠️ Minishell: Additional Tests Suite

### Command 1: Triple pipe with late signal
**Description:** Tests pipe persistence and EOF handling.
**Type:**
```bash
cat | cat | ls
```
**Action:** Press `Enter`, then `Ctrl+D`.
**Expect:** Output of `ls`, then return to prompt.

---

### Command 2: Pipe to head
**Description:** Tests data throttling in pipes.
```bash
yes | head -n 20
```
**Expect:** Exactly 20 lines of "y", then return to prompt.

---

### Command 3: Multi-pipe with builtin
**Description:** Ensures builtins work correctly at the end of a pipe chain.
```bash
cat | cat | echo hello
```
**Expect:** "hello" printed once.

---

### Command 4: Multiple output redirections
**Description:** Multiple files are created; output goes to the last one.
```bash
ls > a > b > c > d
```
**Expect:** Files `a`, `b`, `c` created (empty). File `d` created containing `ls` output.

---

### Command 5: Simple Heredoc
**Description:** Basic heredoc functionality.
```bash
cat << EOF
Hello world
EOF
```
**Expect:** "Hello world" printed to stdout.

---

### Command 6: Heredoc with pipe and redirection
**Description:** Tests if you are hardcoding temp files (like .heredoc_tmp_0).
```bash
cat << EOF | echo hello world > test_file
```
**Expect:** Prompt for heredoc. No output to stdout. `test_file` contains "hello world".

---

### Command 7: Syntax errors (Pipes/Redirects)
**Description:** Invalid token combinations.
* `ls | > wc` (Error near `>`)
* `ls | | wc` (Error near `|`)
* `echo hola > | file` (Error near `|`)

---

### Command 8: Empty / Whitespace Input
**Description:** Robustness against "nothing".
* ` ` (Empty line)
* `     ` (Spaces)
**Expect:** New prompt, `$?` unchanged.

---

### Command 9: Unclosed quotes
**Description:** Lexer error handling.
```bash
echo "hello
```
**Expect:** `minishell: syntax error: unclosed quote`; `$?` = 2 (or your shell's error code).

---

### Command 10: Environment Sensitivity (PATH/HOME)
**Description:** Commands should fail if PATH is gone unless absolute path is used.
```bash
unset PATH
ls          # Expect: command not found
/bin/ls     # Expect: directory listing
unset HOME
cd          # Expect: cd: HOME not set
```

---

### Command 11: Heredoc Priority
**Description:** Multiple heredocs must all be prompted, but only the last is used.
```bash
cat << 1 << 2 << 3
content1
1
content2
2
content3
3
```
**Expect:** Prompts for 1, 2, and 3. `cat` prints "content3".

---

### Command 12: Redirect without command
**Description:** Redirections should still happen (files created) even without a command.
```bash
> test1 < test2
```
**Expect:** If `test2` exists, `test1` is created. No error.

---

### Command 13: Redirection without spaces
**Description:** Tokenizer check.
```bash
echo hola>file
```
**Expect:** File `file` contains "hola".

---

### Command 14: Input redirect error
**Description:** Missing file handling.
```bash
wc < non_existent_file
```
**Expect:** `minishell: non_existent_file: No such file or directory`; `$?` = 1.

---

### Command 15: Pipe with error
**Description:** Pipe should not stop because one command fails.
```bash
cat non_existent | wc
```
**Expect:** Error from cat; `wc` prints `0 0 0`.

---

# ⌨️ Manual Signals (Keyboard Tests)

## **Ctrl+C in interactive prompt**
* **Action:** Press `Ctrl+C` on empty line.
* **Expect:** New line, new prompt, `$? = 130`.

## **Ctrl+C during a running command**
* **Type:** `sleep 10` then `Ctrl+C`.
* **Expect:** Command terminates immediately, `$? = 130`.

## **Ctrl+\ during a running command**
* **Type:** `sleep 10` then `Ctrl+\`.
* **Expect:** `Quit (core dumped)`, `$? = 131`.

## **Ctrl+\ in interactive prompt**
* **Action:** Press `Ctrl+\` on empty line.
* **Expect:** Nothing happens (ignored), prompt stays.

## **Ctrl+D on empty line**
* **Action:** Press `Ctrl+D` on empty line.
* **Expect:** Shell exits. `echo $?` in parent shell is `0`.

## **Ctrl+C during heredoc**
* **Type:** `cat << EOF` then `Ctrl+C`.
* **Expect:** Heredoc closes, new prompt, `$? = 130`.

