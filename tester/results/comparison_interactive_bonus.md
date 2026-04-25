# Interactive Comparison (interactive - bonus)

**Results:** 364/369 match | 5 differ

| Status | Input | Bash Output | Minishell Output |
| :---: | :--- | :--- | :--- |
| ✅ | `echo "red" > colors.txt  ` | `                         ` | `                         ` |
| ✅ | `echo "green" >> colors.tx`<br>`t                        ` | `                         ` | `                         ` |
| ✅ | `echo "blue" >> colors.txt` | `                         ` | `                         ` |
| ✅ | `echo "yellow" >> colors.t`<br>`xt                       ` | `                         ` | `                         ` |
| ✅ | `echo hello               ` | `hello                    ` | `hello                    ` |
| ✅ | `echo -n noeol            ` | `noeol                    ` | `noeol                    ` |
| ✅ | `echo -n                  ` | `                         ` | `                         ` |
| ✅ | `echo hello world         ` | `hello world              ` | `hello world              ` |
| ✅ | `echo ""                  ` | `                         ` | `                         ` |
| ✅ | `echo "  spaces  "        ` | ` spaces                  ` | ` spaces                  ` |
| ✅ | `echo -n one -n two       ` | `one -n two               ` | `one -n two               ` |
| ✅ | `echo one two   three     ` | `one two three            ` | `one two three            ` |
| ✅ | `echo                     ` | `                         ` | `                         ` |
| ✅ | `echo "" hola             ` | ` hola                    ` | ` hola                    ` |
| ✅ | `echo -n -n hola          ` | `hola                     ` | `hola                     ` |
| ✅ | `echo -n -nh -n hola      ` | `-nh -n hola              ` | `-nh -n hola              ` |
| ✅ | `echo -nnnnnnnnn hola     ` | `hola                     ` | `hola                     ` |
| ✅ | `echo 'echo "hola'        ` | `echo "hola               ` | `echo "hola               ` |
| ✅ | `echo $?hcudshfuewrf ew  w`<br>`r 4ew""""                ` | `0hcudshfuewrf ew wr 4ew  ` | `0hcudshfuewrf ew wr 4ew  ` |
| ✅ | `echo ""uhjkhnkj"hjbmb"'''`<br>`' defdjhfkjb "iujiouhj"f'`<br>`f'f'f'f''f'f'f'f'f'f'    ` | `uhjkhnkjhjbmb defdjhfkjb `<br>`iujiouhjfffffffffff      ` | `uhjkhnkjhjbmb defdjhfkjb `<br>`iujiouhjfffffffffff      ` |
| ✅ | `echo ""uhjkhnkj"hjbmb"'''`<br>`' defdjhfkjb "iujiouhj"f'`<br>`f'a'j'o''i'w'q''q        ` | `uhjkhnkjhjbmb defdjhfkjb `<br>`iujiouhjffajoiwqq        ` | `uhjkhnkjhjbmb defdjhfkjb `<br>`iujiouhjffajoiwqq        ` |
| ✅ | `echo ""aaaaaaaa"bbbbb"'''`<br>`' ccccccccc "dddddddd"e'e`<br>`'e                       ` | `aaaaaaaabbbbb ccccccccc d`<br>`dddddddeee               ` | `aaaaaaaabbbbb ccccccccc d`<br>`dddddddeee               ` |
| ✅ | `echo "ho   $USER"  'la   `<br>`$LESS'   $USER$TERM      ` | `ho 42user la $LESS 42user`<br>`xterm                    ` | `ho 42user la $LESS 42user`<br>`xterm                    ` |
| ✅ | `echo "ho   $USER"'la   $L`<br>`ESS'$USER$TERM           ` | `ho 42userla $LESS42userxt`<br>`erm                      ` | `ho 42userla $LESS42userxt`<br>`erm                      ` |
| ✅ | `echo"ho   $USER"         ` | `shell: echoho 42user: com`<br>`mand not found           ` | `shell: echoho 42user: com`<br>`mand not found           ` |
| ✅ | `echo"ho   $USE$LESS"     ` | `shell: echoho : command n`<br>`ot found                 ` | `shell: echoho : command n`<br>`ot found                 ` |
| ✅ | `"echo" "ho   $USER"      ` | `ho 42user                ` | `ho 42user                ` |
| ✅ | `e"cho" "ho   $USER"      ` | `ho 42user                ` | `ho 42user                ` |
| ✅ | `echo "ho   $USER"        ` | `ho 42user                ` | `ho 42user                ` |
| ✅ | `echo "$HOME '$LESS' $USER`<br>`"                        ` | `/home/42user '' 42user   ` | `/home/42user '' 42user   ` |
| ✅ | `echo '$HOME "$LESS" $USER`<br>`'                        ` | `$HOME "$LESS" $USER      ` | `$HOME "$LESS" $USER      ` |
| ✅ | `echo '$'"HOME"           ` | `$HOME                    ` | `$HOME                    ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/app                     ` | `/app                     ` |
| ✅ | `cd /tmp                  ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/tmp                     ` | `/tmp                     ` |
| ✅ | `cd /                     ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/                        ` | `/                        ` |
| ✅ | `cd /usr/bin              ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/usr/bin                 ` | `/usr/bin                 ` |
| ✅ | `cd ..                    ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/usr                     ` | `/usr                     ` |
| ✅ | `cd .                     ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/usr                     ` | `/usr                     ` |
| ✅ | `cd /nonexistent_directory`<br>`_xyz                     ` | `shell: cd: /nonexistent_d`<br>`irectory_xyz: No such fil`<br>`e or directory           ` | `shell: cd: /nonexistent_d`<br>`irectory_xyz: No such fil`<br>`e or directory           ` |
| ✅ | `echo $?                  ` | `1                        ` | `1                        ` |
| ✅ | `cd $_MSDIR               ` | `                         ` | `                         ` |
| ✅ | `export _SAVED_HOME=$HOME ` | `                         ` | `                         ` |
| ✅ | `unset HOME               ` | `                         ` | `                         ` |
| ✅ | `cd                       ` | `shell: cd: HOME not set  ` | `shell: cd: HOME not set  ` |
| ✅ | `echo $?                  ` | `1                        ` | `1                        ` |
| ✅ | `export HOME=$_SAVED_HOME ` | `                         ` | `                         ` |
| ✅ | `unset _SAVED_HOME        ` | `                         ` | `                         ` |
| ✅ | `cd $_MSDIR               ` | `                         ` | `                         ` |
| ✅ | `cd -                     ` | `/app                     ` | `/app                     ` |
| ✅ | `pwd                      ` | `/app                     ` | `/app                     ` |
| ✅ | `cd ~                     ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/home/42user             ` | `/home/42user             ` |
| ✅ | `cd $_MSDIR               ` | `                         ` | `                         ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `echo '$USER'             ` | `$USER                    ` | `$USER                    ` |
| ✅ | `echo '$?'                ` | `$?                       ` | `$?                       ` |
| ✅ | `echo 'hello world'       ` | `hello world              ` | `hello world              ` |
| ✅ | `echo ''                  ` | `                         ` | `                         ` |
| ✅ | `echo 'no \| pipe here'   ` | `no \| pipe here          ` | `no \| pipe here          ` |
| ✅ | `echo 'no > redirect'     ` | `no > redirect            ` | `no > redirect            ` |
| ✅ | `echo 'spaces   preserved'` | `spaces preserved         ` | `spaces preserved         ` |
| ✅ | `echo '$USER is not expand`<br>`ed in single quotes'     ` | `$USER is not expanded in `<br>`single quotes            ` | `$USER is not expanded in `<br>`single quotes            ` |
| ✅ | `echo "hello world"       ` | `hello world              ` | `hello world              ` |
| ✅ | `echo "spaces   preserved"` | `spaces preserved         ` | `spaces preserved         ` |
| ✅ | `echo "cat lol.c \| cat > `<br>`lol.c"                   ` | `cat lol.c \| cat > lol.c ` | `cat lol.c \| cat > lol.c ` |
| ✅ | `export DQTEST=expanded   ` | `                         ` | `                         ` |
| ✅ | `echo $DQTEST             ` | `expanded                 ` | `expanded                 ` |
| ✅ | `echo "$DQTEST"           ` | `expanded                 ` | `expanded                 ` |
| ✅ | `echo "value is $DQTEST en`<br>`d"                       ` | `value is expanded end    ` | `value is expanded end    ` |
| ✅ | `echo "$?"                ` | `0                        ` | `0                        ` |
| ✅ | `echo "'$USER'"           ` | `'42user'                 ` | `'42user'                 ` |
| ✅ | `echo '"$USER"'           ` | `"$USER"                  ` | `"$USER"                  ` |
| ✅ | `echo "$COMPLICADO"       ` | `                         ` | `                         ` |
| ✅ | `echo '$COMPLICADO'       ` | `$COMPLICADO              ` | `$COMPLICADO              ` |
| ✅ | `echo "'$COMPLICADO'"     ` | `''                       ` | `''                       ` |
| ✅ | `echo '"$COMPLICADO"'     ` | `"$COMPLICADO"            ` | `"$COMPLICADO"            ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `echo "first line" > /tmp/`<br>`ms_test_redir.txt        ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_test_redir.tx`<br>`t                        ` | `first line               ` | `first line               ` |
| ✅ | `echo "second line" >> /tm`<br>`p/ms_test_redir.txt      ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_test_redir.tx`<br>`t                        ` | `first line second line   ` | `first line second line   ` |
| ✅ | `echo "third line" >> /tmp`<br>`/ms_test_redir.txt       ` | `                         ` | `                         ` |
| ✅ | `wc -l < /tmp/ms_test_redi`<br>`r.txt                    ` | `3                        ` | `3                        ` |
| ✅ | `echo "overwrite" > /tmp/m`<br>`s_test_redir.txt         ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_test_redir.tx`<br>`t                        ` | `overwrite                ` | `overwrite                ` |
| ✅ | `rm /tmp/ms_test_redir.txt` | `                         ` | `                         ` |
| ✅ | `echo hola > /tmp/ms_rout1`<br>`.txt                     ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_rout1.txt    ` | `hola                     ` | `hola                     ` |
| ✅ | `echo caracola >> /tmp/ms_`<br>`rout1.txt                ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_rout1.txt    ` | `hola caracola            ` | `hola caracola            ` |
| ✅ | `echo hola > /tmp/ms_rout1`<br>`.txt > /tmp/ms_rout2.txt `<br>`> /tmp/ms_rout3.txt      ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_rout1.txt    ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_rout2.txt    ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_rout3.txt    ` | `hola                     ` | `hola                     ` |
| ✅ | `rm -f /tmp/ms_rout1.txt /`<br>`tmp/ms_rout2.txt /tmp/ms_`<br>`rout3.txt                ` | `                         ` | `                         ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `cat << EOF               ` | `> line one > line two > l`<br>`ine three > EOF line one `<br>`line two line three      ` | `> line one > line two > l`<br>`ine three > EOF line one `<br>`line two line three      ` |
| ✅ | `grep "an" << WORDS       ` | `> apple > banana > cherry`<br>` > mango > WORDS banana m`<br>`ango                     ` | `> apple > banana > cherry`<br>` > mango > WORDS banana m`<br>`ango                     ` |
| ✅ | `wc -l << COUNTER         ` | `> a > b > c > d > e > COU`<br>`NTER 5                   ` | `> a > b > c > d > e > COU`<br>`NTER 5                   ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `echo hello \| cat        ` | `hello                    ` | `hello                    ` |
| ✅ | `echo hello \| cat \| cat ` | `hello                    ` | `hello                    ` |
| ✅ | `echo hello \| wc -c      ` | `6                        ` | `6                        ` |
| ✅ | `/bin/ls /dev/null \| cat ` | `/dev/null                ` | `/dev/null                ` |
| ✅ | `echo "apple banana cherry`<br>`" \| tr ' ' '\n' \| sort ` | `apple banana cherry      ` | `apple banana cherry      ` |
| ✅ | `echo "abc" \| rev \| rev ` | `abc                      ` | `abc                      ` |
| ✅ | `echo "line1" > /tmp/ms_pi`<br>`pe_a.txt                 ` | `                         ` | `                         ` |
| ✅ | `echo "line2" >> /tmp/ms_p`<br>`ipe_a.txt                ` | `                         ` | `                         ` |
| ✅ | `echo "line3" >> /tmp/ms_p`<br>`ipe_a.txt                ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_pipe_a.txt \|`<br>` wc -l                   ` | `3                        ` | `3                        ` |
| ✅ | `cat /tmp/ms_pipe_a.txt \|`<br>` grep "line" \| wc -l    ` | `3                        ` | `3                        ` |
| ✅ | `cat /tmp/ms_pipe_a.txt \|`<br>` sort -r > /tmp/ms_pipe_b`<br>`.txt                     ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_pipe_b.txt   ` | `line3 line2 line1        ` | `line3 line2 line1        ` |
| ✅ | `rm /tmp/ms_pipe_a.txt /tm`<br>`p/ms_pipe_b.txt          ` | `                         ` | `                         ` |
| ✅ | `mkdir test_ls_pipe_wc    ` | `                         ` | `                         ` |
| ✅ | `cd test_ls_pipe_wc       ` | `                         ` | `                         ` |
| ✅ | `touch file1 file2 file3  ` | `                         ` | `                         ` |
| ✅ | `ls \| wc                 ` | ` 3 3 18                  ` | ` 3 3 18                  ` |
| ✅ | `ls\|wc                   ` | ` 3 3 18                  ` | ` 3 3 18                  ` |
| ✅ | `cd ..                    ` | `                         ` | `                         ` |
| ✅ | `rm -rf test_ls_pipe_wc   ` | `                         ` | `                         ` |
| ✅ | `wc < colors.txt > /tmp/ms`<br>`_wc_out.txt              ` | `                         ` | `                         ` |
| ✅ | `cat /tmp/ms_wc_out.txt   ` | ` 4 4 22                  ` | ` 4 4 22                  ` |
| ✅ | `rm -f /tmp/ms_wc_out.txt ` | `                         ` | `                         ` |
| ✅ | `cat colors.txt \| wc     ` | ` 4 4 22                  ` | ` 4 4 22                  ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `export TESTVAR=hello42   ` | `                         ` | `                         ` |
| ✅ | `echo $TESTVAR            ` | `hello42                  ` | `hello42                  ` |
| ✅ | `export TESTVAR=updated   ` | `                         ` | `                         ` |
| ✅ | `echo $TESTVAR            ` | `updated                  ` | `updated                  ` |
| ✅ | `echo $?                  ` | `0                        ` | `0                        ` |
| ✅ | `unset TESTVAR            ` | `                         ` | `                         ` |
| ✅ | `echo $TESTVAR            ` | `                         ` | `                         ` |
| ✅ | `export MY_VAR=hello      ` | `                         ` | `                         ` |
| ✅ | `echo $MY_VAR             ` | `hello                    ` | `hello                    ` |
| ✅ | `env \| grep MY_VAR       ` | `MY_VAR=hello             ` | `MY_VAR=hello             ` |
| ✅ | `export MY_VAR=updated    ` | `                         ` | `                         ` |
| ✅ | `echo $MY_VAR             ` | `updated                  ` | `updated                  ` |
| ✅ | `env \| grep MY_VAR       ` | `MY_VAR=updated           ` | `MY_VAR=updated           ` |
| ✅ | `unset MY_VAR             ` | `                         ` | `                         ` |
| ✅ | `echo $MY_VAR             ` | `                         ` | `                         ` |
| ✅ | `echo "exit:$?"           ` | `exit:0                   ` | `exit:0                   ` |
| ✅ | `export A=1               ` | `                         ` | `                         ` |
| ✅ | `echo $A                  ` | `1                        ` | `1                        ` |
| ✅ | `export B=2               ` | `                         ` | `                         ` |
| ✅ | `echo $B                  ` | `2                        ` | `2                        ` |
| ✅ | `export C=3               ` | `                         ` | `                         ` |
| ✅ | `echo $C                  ` | `3                        ` | `3                        ` |
| ✅ | `unset B                  ` | `                         ` | `                         ` |
| ✅ | `echo $A                  ` | `1                        ` | `1                        ` |
| ✅ | `echo $B                  ` | `                         ` | `                         ` |
| ✅ | `echo $C                  ` | `3                        ` | `3                        ` |
| ✅ | `env \| grep -E "^A=\|^B=\`<br>`|^C=" \| sort            ` | `A=1 C=3                  ` | `A=1 C=3                  ` |
| ✅ | `export a=b               ` | `                         ` | `                         ` |
| ✅ | `echo $a                  ` | `b                        ` | `b                        ` |
| ✅ | `export b=wawa            ` | `                         ` | `                         ` |
| ✅ | `echo $b                  ` | `wawa                     ` | `wawa                     ` |
| ✅ | `export b=lala            ` | `                         ` | `                         ` |
| ✅ | `echo $b                  ` | `lala                     ` | `lala                     ` |
| ✅ | `export c=lala=kaka       ` | `                         ` | `                         ` |
| ✅ | `echo $c                  ` | `lala=kaka                ` | `lala=kaka                ` |
| ✅ | `export a=                ` | `                         ` | `                         ` |
| ✅ | `echo "\|$a\|"            ` | `\|\|                     ` | `\|\|                     ` |
| ✅ | `export a3=l              ` | `                         ` | `                         ` |
| ✅ | `echo $a3                 ` | `l                        ` | `l                        ` |
| ✅ | `export 2a=lala           ` | `shell: export: `2a=lala':`<br>` not a valid identifier  ` | `shell: export: `2a=lala':`<br>` not a valid identifier  ` |
| ✅ | `export NUEVA=$TERM       ` | `                         ` | `                         ` |
| ✅ | `echo $NUEVA              ` | `xterm                    ` | `xterm                    ` |
| ✅ | `export POLLOS=asados     ` | `                         ` | `                         ` |
| ✅ | `echo $POLLOS             ` | `asados                   ` | `asados                   ` |
| ✅ | `unset POLLOS             ` | `                         ` | `                         ` |
| ✅ | `echo $POLLOS             ` | `                         ` | `                         ` |
| ✅ | `export A=1 B=2           ` | `                         ` | `                         ` |
| ✅ | `echo $A $B               ` | `1 2                      ` | `1 2                      ` |
| ✅ | `unset A B                ` | `                         ` | `                         ` |
| ✅ | `echo $A $B               ` | `                         ` | `                         ` |
| ✅ | `export a= b=o            ` | `                         ` | `                         ` |
| ✅ | `echo $a $b               ` | `o                        ` | `o                        ` |
| ✅ | `export a===              ` | `                         ` | `                         ` |
| ✅ | `echo $a                  ` | `==                       ` | `==                       ` |
| ✅ | `export ""                ` | `shell: export: `': not a `<br>`valid identifier         ` | `shell: export: `': not a `<br>`valid identifier         ` |
| ❌ | `env                      ` | `SHELL=/usr/bin/fish _MSDI`<br>`R=/app ASCIINEMA_REC=1 HO`<br>`STNAME=42container LANGUA`<br>`GE=en_US:en SSH_AUTH_SOCK`<br>`=/ssh-agent PWD=/app C=3 `<br>`a3=l c=lala=kaka HOME=/ho`<br>`me/42user b=o a=== LANG=e`<br>`n_US.UTF-8 NUEVA=xterm HI`<br>`STFILE=/home/42user/.bash`<br>`_history LS_COLORS=rs=0:d`<br>`i=01;34:ln=01;36:mh=00:pi`<br>`=40;33:so=01;35:do=01;35:`<br>`bd=40;33;01:cd=40;33;01:o`<br>`r=40;31;01:mi=00:su=37;41`<br>`:sg=30;43:ca=30;41:tw=30;`<br>`42:ow=34;42:st=37;44:ex=0`<br>`1;32:*.tar=01;31:*.tgz=01`<br>`;31:*.arc=01;31:*.arj=01;`<br>`31:*.taz=01;31:*.lha=01;3`<br>`1:*.lz4=01;31:*.lzh=01;31`<br>`:*.lzma=01;31:*.tlz=01;31`<br>`:*.txz=01;31:*.tzo=01;31:`<br>`*.t7z=01;31:*.zip=01;31:*`<br>`.z=01;31:*.dz=01;31:*.gz=`<br>`01;31:*.lrz=01;31:*.lz=01`<br>`;31:*.lzo=01;31:*.xz=01;3`<br>`1:*.zst=01;31:*.tzst=01;3`<br>`1:*.bz2=01;31:*.bz=01;31:`<br>`*.tbz=01;31:*.tbz2=01;31:`<br>`*.tz=01;31:*.deb=01;31:*.`<br>`rpm=01;31:*.jar=01;31:*.w`<br>`ar=01;31:*.ear=01;31:*.sa`<br>`r=01;31:*.rar=01;31:*.alz`<br>`=01;31:*.ace=01;31:*.zoo=`<br>`01;31:*.cpio=01;31:*.7z=0`<br>`1;31:*.rz=01;31:*.cab=01;`<br>`31:*.wim=01;31:*.swm=01;3`<br>`1:*.dwm=01;31:*.esd=01;31`<br>`:*.jpg=01;35:*.jpeg=01;35`<br>`:*.mjpg=01;35:*.mjpeg=01;`<br>`35:*.gif=01;35:*.bmp=01;3`<br>`5:*.pbm=01;35:*.pgm=01;35`<br>`:*.ppm=01;35:*.tga=01;35:`<br>`*.xbm=01;35:*.xpm=01;35:*`<br>`.tif=01;35:*.tiff=01;35:*`<br>`.png=01;35:*.svg=01;35:*.`<br>`svgz=01;35:*.mng=01;35:*.`<br>`pcx=01;35:*.mov=01;35:*.m`<br>`pg=01;35:*.mpeg=01;35:*.m`<br>`2v=01;35:*.mkv=01;35:*.we`<br>`bm=01;35:*.webp=01;35:*.o`<br>`gm=01;35:*.mp4=01;35:*.m4`<br>`v=01;35:*.mp4v=01;35:*.vo`<br>`b=01;35:*.qt=01;35:*.nuv=`<br>`01;35:*.wmv=01;35:*.asf=0`<br>`1;35:*.rm=01;35:*.rmvb=01`<br>`;35:*.flc=01;35:*.avi=01;`<br>`35:*.fli=01;35:*.flv=01;3`<br>`5:*.gl=01;35:*.dl=01;35:*`<br>`.xcf=01;35:*.xwd=01;35:*.`<br>`yuv=01;35:*.cgm=01;35:*.e`<br>`mf=01;35:*.ogv=01;35:*.og`<br>`x=01;35:*.aac=00;36:*.au=`<br>`00;36:*.flac=00;36:*.m4a=`<br>`00;36:*.mid=00;36:*.midi=`<br>`00;36:*.mka=00;36:*.mp3=0`<br>`0;36:*.mpc=00;36:*.ogg=00`<br>`;36:*.ra=00;36:*.wav=00;3`<br>`6:*.oga=00;36:*.opus=00;3`<br>`6:*.spx=00;36:*.xspf=00;3`<br>`6: DQTEST=expanded TERM=x`<br>`term USER=42user SHLVL=4 `<br>`LC_ALL=en_US.UTF-8 PATH=/`<br>`usr/local/sbin:/usr/local`<br>`/bin:/usr/sbin:/usr/bin:/`<br>`sbin:/bin DEBIAN_FRONTEND`<br>`=noninteractive OLDPWD=/a`<br>`pp/test_ls_pipe_wc _=/usr`<br>`/bin/env                 ` | `SHELL=/usr/bin/fish ASCII`<br>`NEMA_REC=1 HOSTNAME=42con`<br>`tainer LANGUAGE=en_US:en `<br>`SSH_AUTH_SOCK=/ssh-agent `<br>`PWD=/app LANG=en_US.UTF-8`<br>` HISTFILE=/home/42user/.b`<br>`ash_history LS_COLORS=rs=`<br>`0:di=01;34:ln=01;36:mh=00`<br>`:pi=40;33:so=01;35:do=01;`<br>`35:bd=40;33;01:cd=40;33;0`<br>`1:or=40;31;01:mi=00:su=37`<br>`;41:sg=30;43:ca=30;41:tw=`<br>`30;42:ow=34;42:st=37;44:e`<br>`x=01;32:*.tar=01;31:*.tgz`<br>`=01;31:*.arc=01;31:*.arj=`<br>`01;31:*.taz=01;31:*.lha=0`<br>`1;31:*.lz4=01;31:*.lzh=01`<br>`;31:*.lzma=01;31:*.tlz=01`<br>`;31:*.txz=01;31:*.tzo=01;`<br>`31:*.t7z=01;31:*.zip=01;3`<br>`1:*.z=01;31:*.dz=01;31:*.`<br>`gz=01;31:*.lrz=01;31:*.lz`<br>`=01;31:*.lzo=01;31:*.xz=0`<br>`1;31:*.zst=01;31:*.tzst=0`<br>`1;31:*.bz2=01;31:*.bz=01;`<br>`31:*.tbz=01;31:*.tbz2=01;`<br>`31:*.tz=01;31:*.deb=01;31`<br>`:*.rpm=01;31:*.jar=01;31:`<br>`*.war=01;31:*.ear=01;31:*`<br>`.sar=01;31:*.rar=01;31:*.`<br>`alz=01;31:*.ace=01;31:*.z`<br>`oo=01;31:*.cpio=01;31:*.7`<br>`z=01;31:*.rz=01;31:*.cab=`<br>`01;31:*.wim=01;31:*.swm=0`<br>`1;31:*.dwm=01;31:*.esd=01`<br>`;31:*.jpg=01;35:*.jpeg=01`<br>`;35:*.mjpg=01;35:*.mjpeg=`<br>`01;35:*.gif=01;35:*.bmp=0`<br>`1;35:*.pbm=01;35:*.pgm=01`<br>`;35:*.ppm=01;35:*.tga=01;`<br>`35:*.xbm=01;35:*.xpm=01;3`<br>`5:*.tif=01;35:*.tiff=01;3`<br>`5:*.png=01;35:*.svg=01;35`<br>`:*.svgz=01;35:*.mng=01;35`<br>`:*.pcx=01;35:*.mov=01;35:`<br>`*.mpg=01;35:*.mpeg=01;35:`<br>`*.m2v=01;35:*.mkv=01;35:*`<br>`.webm=01;35:*.webp=01;35:`<br>`*.ogm=01;35:*.mp4=01;35:*`<br>`.m4v=01;35:*.mp4v=01;35:*`<br>`.vob=01;35:*.qt=01;35:*.n`<br>`uv=01;35:*.wmv=01;35:*.as`<br>`f=01;35:*.rm=01;35:*.rmvb`<br>`=01;35:*.flc=01;35:*.avi=`<br>`01;35:*.fli=01;35:*.flv=0`<br>`1;35:*.gl=01;35:*.dl=01;3`<br>`5:*.xcf=01;35:*.xwd=01;35`<br>`:*.yuv=01;35:*.cgm=01;35:`<br>`*.emf=01;35:*.ogv=01;35:*`<br>`.ogx=01;35:*.aac=00;36:*.`<br>`au=00;36:*.flac=00;36:*.m`<br>`4a=00;36:*.mid=00;36:*.mi`<br>`di=00;36:*.mka=00;36:*.mp`<br>`3=00;36:*.mpc=00;36:*.ogg`<br>`=00;36:*.ra=00;36:*.wav=0`<br>`0;36:*.oga=00;36:*.opus=0`<br>`0;36:*.spx=00;36:*.xspf=0`<br>`0;36: TERM=xterm USER=42u`<br>`ser SHLVL=4 LC_ALL=en_US.`<br>`UTF-8 PATH=/usr/local/sbi`<br>`n:/usr/local/bin:/usr/sbi`<br>`n:/usr/bin:/sbin:/bin DEB`<br>`IAN_FRONTEND=noninteracti`<br>`ve _=/usr/bin/expect OLDP`<br>`WD=/app/test_ls_pipe_wc M`<br>`AIL=mlermo-j@student.42ma`<br>`laga.com _MSDIR=/app HOME`<br>`=/home/42user DQTEST=expa`<br>`nded C=3 a=== b=o c=lala=`<br>`kaka a3=l NUEVA=xterm    ` |
| ✅ | `env lalal                ` | `env: ‘lalal’: No such fil`<br>`e or directory           ` | `env: ‘lalal’: No such fil`<br>`e or directory           ` |
| ✅ | `env directorio           ` | `env: ‘directorio’: No suc`<br>`h file or directory      ` | `env: ‘directorio’: No suc`<br>`h file or directory      ` |
| ✅ | `unset                    ` | `                         ` | `                         ` |
| ✅ | `unset $HOME $USER        ` | `                         ` | `                         ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `mkdir -p /tmp/ms_wildcard`<br>`_test                    ` | `                         ` | `                         ` |
| ✅ | `echo "c file" > /tmp/ms_w`<br>`ildcard_test/foo.c       ` | `                         ` | `                         ` |
| ✅ | `echo "h file" > /tmp/ms_w`<br>`ildcard_test/foo.h       ` | `                         ` | `                         ` |
| ✅ | `echo "txt file" > /tmp/ms`<br>`_wildcard_test/bar.txt   ` | `                         ` | `                         ` |
| ✅ | `cd /tmp/ms_wildcard_test ` | `                         ` | `                         ` |
| ✅ | `echo *.c                 ` | `foo.c                    ` | `foo.c                    ` |
| ✅ | `echo *.h                 ` | `foo.h                    ` | `foo.h                    ` |
| ✅ | `echo *.txt               ` | `bar.txt                  ` | `bar.txt                  ` |
| ✅ | `ls *.c                   ` | `foo.c                    ` | `foo.c                    ` |
| ✅ | `ls *.h                   ` | `foo.h                    ` | `foo.h                    ` |
| ✅ | `echo *                   ` | `bar.txt foo.c foo.h      ` | `bar.txt foo.c foo.h      ` |
| ✅ | `cd $_MSDIR               ` | `                         ` | `                         ` |
| ✅ | `rm -rf /tmp/ms_wildcard_t`<br>`est                      ` | `                         ` | `                         ` |
| ✅ | `cat < colors.txt         ` | `red green blue yellow    ` | `red green blue yellow    ` |
| ✅ | `cat < colors.txt > copia.`<br>`txt                      ` | `                         ` | `                         ` |
| ✅ | `cat copia.txt            ` | `red green blue yellow    ` | `red green blue yellow    ` |
| ✅ | `rm -f copia.txt          ` | `                         ` | `                         ` |
| ✅ | `cat colors.txt \| wc     ` | ` 4 4 22                  ` | ` 4 4 22                  ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `echo "extra" > /tmp/ms_lo`<br>`gic_a.txt && cat /tmp/ms_`<br>`logic_a.txt              ` | `extra                    ` | `extra                    ` |
| ✅ | `echo one && echo two     ` | `one two                  ` | `one two                  ` |
| ✅ | `true && echo "true_passed`<br>`"                        ` | `true_passed              ` | `true_passed              ` |
| ✅ | `false && echo "SHOULD_NOT`<br>`_PRINT"                  ` | `                         ` | `                         ` |
| ✅ | `false \|\| echo "false_re`<br>`covered"                 ` | `false_recovered          ` | `false_recovered          ` |
| ✅ | `true \|\| echo "SHOULD_NO`<br>`T_PRINT"                 ` | `                         ` | `                         ` |
| ✅ | `echo "start" && false \|\`<br>`| echo "fallback"        ` | `start fallback           ` | `start fallback           ` |
| ✅ | `false \|\| false \|\| ech`<br>`o "last_resort"          ` | `last_resort              ` | `last_resort              ` |
| ✅ | `true && true && echo "all`<br>`_true"                   ` | `all_true                 ` | `all_true                 ` |
| ✅ | `false \|\| true && echo "`<br>`chain_ok"                ` | `chain_ok                 ` | `chain_ok                 ` |
| ✅ | `(echo uno && (false \|\| `<br>`echo dos)) && echo tres  ` | `uno dos tres             ` | `uno dos tres             ` |
| ✅ | `(false && echo "nope") \|`<br>`\| (true && echo "ok")   ` | `ok                       ` | `ok                       ` |
| ✅ | `(echo "A" && (false \|\| `<br>`(echo "B" && true))) \|\|`<br>` echo "C"                ` | `A B                      ` | `A B                      ` |
| ✅ | `(true && (false \|\| (tru`<br>`e && echo "deep"))) && ec`<br>`ho "final"               ` | `deep final               ` | `deep final               ` |
| ✅ | `(echo "start" && (false \`<br>`|\| (echo "mid" && false)`<br>`) && echo "never") \|\| e`<br>`cho "end"                ` | `start mid end            ` | `start mid end            ` |
| ✅ | `(false \|\| (false && ech`<br>`o "no") \|\| (true && ech`<br>`o "yes")) && echo "done" ` | `yes done                 ` | `yes done                 ` |
| ✅ | `mkdir test_ls_bool       ` | `                         ` | `                         ` |
| ✅ | `cd test_ls_bool          ` | `                         ` | `                         ` |
| ✅ | `touch file1 file2 file3  ` | `                         ` | `                         ` |
| ✅ | `ls && echo "exito"       ` | `file1 file2 file3 exito  ` | `file1 file2 file3 exito  ` |
| ✅ | `ls archivo_que_no_existe `<br>`&& echo "no se ve"       ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory       ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory       ` |
| ✅ | `ls \|\| echo "no se ve"  ` | `file1 file2 file3        ` | `file1 file2 file3        ` |
| ✅ | `ls archivo_que_no_existe `<br>`\|\| echo "se ve"        ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory se ve ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory se ve ` |
| ✅ | `true && echo "exito" \|\|`<br>` echo "fallo"            ` | `exito                    ` | `exito                    ` |
| ✅ | `false && echo "no se ve" `<br>`\|\| echo "se ve"        ` | `se ve                    ` | `se ve                    ` |
| ✅ | `ls && ls && ls && ls && e`<br>`cho "todos exitosos"     ` | `file1 file2 file3 file1 f`<br>`ile2 file3 file1 file2 fi`<br>`le3 file1 file2 file3 tod`<br>`os exitosos              ` | `file1 file2 file3 file1 f`<br>`ile2 file3 file1 file2 fi`<br>`le3 file1 file2 file3 tod`<br>`os exitosos              ` |
| ✅ | `ls && ls archivo_que_no_e`<br>`xiste && ls && ls        ` | `file1 file2 file3 ls: can`<br>`not access 'archivo_que_n`<br>`o_existe': No such file o`<br>`r directory              ` | `file1 file2 file3 ls: can`<br>`not access 'archivo_que_n`<br>`o_existe': No such file o`<br>`r directory              ` |
| ✅ | `ls \|\| ls \|\| ls \|\| l`<br>`s                        ` | `file1 file2 file3        ` | `file1 file2 file3        ` |
| ✅ | `ls archivo_que_no_existe `<br>`\|\| echo "recuperacion" `<br>`&& echo "continua"       ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory recupe`<br>`racion continua          ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory recupe`<br>`racion continua          ` |
| ✅ | `(ls && echo "dentro de pa`<br>`rentesis") && echo "fuera`<br>` de parentesis"          ` | `file1 file2 file3 dentro `<br>`de parentesis fuera de pa`<br>`rentesis                 ` | `file1 file2 file3 dentro `<br>`de parentesis fuera de pa`<br>`rentesis                 ` |
| ✅ | `(ls archivo_que_no_existe`<br>` \|\| echo "recuperado") `<br>`&& echo "continua"       ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory recupe`<br>`rado continua            ` | `ls: cannot access 'archiv`<br>`o_que_no_existe': No such`<br>` file or directory recupe`<br>`rado continua            ` |
| ✅ | `false \|\| (true && echo `<br>`"esto se ve")            ` | `esto se ve               ` | `esto se ve               ` |
| ✅ | `true && (false \|\| echo `<br>`"esto tambien")          ` | `esto tambien             ` | `esto tambien             ` |
| ✅ | `true && true \|\| false &`<br>`& false                  ` | `                         ` | `                         ` |
| ✅ | `false && false \|\| true `<br>`&& true                  ` | `                         ` | `                         ` |
| ✅ | `(ls && echo a) && (ls && `<br>`echo b) \|\| (ls && echo `<br>`c)                       ` | `file1 file2 file3 a file1`<br>` file2 file3 b           ` | `file1 file2 file3 a file1`<br>` file2 file3 b           ` |
| ✅ | `cd ..                    ` | `                         ` | `                         ` |
| ✅ | `rm -rf test_ls_bool      ` | `                         ` | `                         ` |
| ✅ | `rm -f /tmp/ms_logic_a.txt` | `                         ` | `                         ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `mkdir -p /tmp/ms_user42_t`<br>`est                      ` | `                         ` | `                         ` |
| ✅ | `mkdir -p /tmp/ms_user42_t`<br>`est/dir_existe           ` | `                         ` | `                         ` |
| ✅ | `touch /tmp/ms_user42_test`<br>`/file_existe             ` | `                         ` | `                         ` |
| ✅ | `mkdir -p /tmp/ms_user42_t`<br>`est/dir_noperm           ` | `                         ` | `                         ` |
| ✅ | `chmod 000 /tmp/ms_user42_`<br>`test/dir_noperm          ` | `                         ` | `                         ` |
| ✅ | `echo -e "red\ngreen\nblue`<br>`\nyellow" > /tmp/ms_user4`<br>`2_test/colors.txt        ` | `                         ` | `                         ` |
| ✅ | `cd /tmp/ms_user42_test   ` | `                         ` | `                         ` |
| ✅ | `echo $?hcudshfuewrf ew  w`<br>`r 4ew""                  ` | `0hcudshfuewrf ew wr 4ew  ` | `0hcudshfuewrf ew wr 4ew  ` |
| ✅ | `echo "ho   $USER"  "la   `<br>`$LESS"   $USER$TERM      ` | `ho 42user la 42userxterm ` | `ho 42user la 42userxterm ` |
| ✅ | `echo "ho   $USER"        ` | `ho 42user                ` | `ho 42user                ` |
| ✅ | `echo"ho   $USER"         ` | `shell: echoho 42user: com`<br>`mand not found           ` | `shell: echoho 42user: com`<br>`mand not found           ` |
| ✅ | `e"cho" "ho   $USER"      ` | `ho 42user                ` | `ho 42user                ` |
| ✅ | `echo "ho   $USER"        ` | `ho 42user                ` | `ho 42user                ` |
| ✅ | `echo "$HOME" "$USER"     ` | `/home/42user 42user      ` | `/home/42user 42user      ` |
| ✅ | `cd dir_existe            ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/tmp/ms_user42_test/dir_e`<br>`xiste                    ` | `/tmp/ms_user42_test/dir_e`<br>`xiste                    ` |
| ✅ | `cd directorio_no_existe  ` | `shell: cd: directorio_no_`<br>`existe: No such file or d`<br>`irectory                 ` | `shell: cd: directorio_no_`<br>`existe: No such file or d`<br>`irectory                 ` |
| ✅ | `echo $?                  ` | `1                        ` | `1                        ` |
| ✅ | `cd file_existe           ` | `shell: cd: file_existe: N`<br>`o such file or directory ` | `shell: cd: file_existe: N`<br>`o such file or directory ` |
| ✅ | `echo $?                  ` | `1                        ` | `1                        ` |
| ✅ | `cd /tmp/ms_user42_test   ` | `                         ` | `                         ` |
| ✅ | `cd                       ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/home/42user             ` | `/home/42user             ` |
| ❌ | `ls \| wc                 ` | ` 1 1 8                   ` | ` 2 2 19                  ` |
| ❌ | `ls\|wc                   ` | ` 1 1 8                   ` | ` 2 2 19                  ` |
| ✅ | `echo "colorinchis" > colo`<br>`rs.txt                   ` | `                         ` | `                         ` |
| ✅ | `cat colors.txt \| sort -r`<br>` \| wc                   ` | ` 1 1 12                  ` | ` 1 1 12                  ` |
| ✅ | `cd -                     ` | `/tmp/ms_user42_test      ` | `/tmp/ms_user42_test      ` |
| ✅ | `pwd                      ` | `/tmp/ms_user42_test      ` | `/tmp/ms_user42_test      ` |
| ✅ | `cd ~                     ` | `                         ` | `                         ` |
| ✅ | `pwd                      ` | `/home/42user             ` | `/home/42user             ` |
| ✅ | `cd $_MSDIR               ` | `                         ` | `                         ` |
| ✅ | `chmod 755 /tmp/ms_user42_`<br>`test/dir_noperm          ` | `                         ` | `                         ` |
| ✅ | `rm -rf /tmp/ms_user42_tes`<br>`t                        ` | `                         ` | `                         ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `export _SAVED_PATH=$PATH ` | `                         ` | `                         ` |
| ✅ | `unset PATH               ` | `                         ` | `                         ` |
| ✅ | `ls                       ` | `shell: ls: No such file o`<br>`r directory              ` | `shell: ls: No such file o`<br>`r directory              ` |
| ✅ | `echo $?                  ` | `127                      ` | `127                      ` |
| ✅ | `/bin/ls                  ` | `Bonus_tests.md interactiv`<br>`e minishell non_interacti`<br>`ve run_tests.sh colors.tx`<br>`t manual_tests minishell.`<br>`cast results utils       ` | `Bonus_tests.md interactiv`<br>`e minishell non_interacti`<br>`ve run_tests.sh colors.tx`<br>`t manual_tests minishell.`<br>`cast results utils       ` |
| ✅ | `echo $?                  ` | `0                        ` | `0                        ` |
| ✅ | `export PATH=$_SAVED_PATH ` | `                         ` | `                         ` |
| ✅ | `unset _SAVED_PATH        ` | `                         ` | `                         ` |
| ✅ | `ls noexiste              ` | `ls: cannot access 'noexis`<br>`te': No such file or dire`<br>`ctory                    ` | `ls: cannot access 'noexis`<br>`te': No such file or dire`<br>`ctory                    ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit                     ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `0                        ` | `0                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit 0                   ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `0                        ` | `0                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit 42                  ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `42                       ` | `42                       ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit -42                 ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `214                      ` | `214                      ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit 2147483647          ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `255                      ` | `255                      ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit -2147483648         ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `0                        ` | `0                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit 9223372036854775807 ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `255                      ` | `255                      ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit -9223372036854775808` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `0                        ` | `0                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit 9223372036854775808 ` | `shell: exit: 922337203685`<br>`4775808: numeric argument`<br>` required                ` | `shell: exit: 922337203685`<br>`4775808: numeric argument`<br>` required                ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit -9223372036854775809` | `shell: exit: -92233720368`<br>`54775809: numeric argumen`<br>`t required               ` | `shell: exit: -92233720368`<br>`54775809: numeric argumen`<br>`t required               ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit +100                ` | `                         ` | `                         ` |
| ✅ | `echo $?                  ` | `100                      ` | `100                      ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit ++100               ` | `shell: exit: ++100: numer`<br>`ic argument required     ` | `shell: exit: ++100: numer`<br>`ic argument required     ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit +++100              ` | `shell: exit: +++100: nume`<br>`ric argument required    ` | `shell: exit: +++100: nume`<br>`ric argument required    ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit --100               ` | `shell: exit: --100: numer`<br>`ic argument required     ` | `shell: exit: --100: numer`<br>`ic argument required     ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit exit                ` | `shell: exit: exit: numeri`<br>`c argument required      ` | `shell: exit: exit: numeri`<br>`c argument required      ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit 42 53 64            ` | `shell: exit: too many arg`<br>`uments                   ` | `shell: exit: too many arg`<br>`uments                   ` |
| ✅ | `echo $?                  ` | `1                        ` | `1                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit hola mundo          ` | `shell: exit: hola: numeri`<br>`c argument required      ` | `shell: exit: hola: numeri`<br>`c argument required      ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `bash --norc --noprofile  ` | `                         ` | `                         ` |
| ✅ | `exit 42hola              ` | `shell: exit: 42hola: nume`<br>`ric argument required    ` | `shell: exit: 42hola: nume`<br>`ric argument required    ` |
| ✅ | `echo $?                  ` | `2                        ` | `2                        ` |
| ✅ | `                         ` | `                         ` | `                         ` |
| ✅ | `mkdir test_ls_syntax     ` | `                         ` | `                         ` |
| ✅ | `cd test_ls_syntax        ` | `                         ` | `                         ` |
| ✅ | `touch file1 file2 file3  ` | `                         ` | `                         ` |
| ✅ | `ls \|\| wc               ` | `file1 file2 file3        ` | `file1 file2 file3        ` |
| ✅ | `ls \|   \| wc            ` | `shell: syntax error near `<br>`unexpected token `\|'    ` | `shell: syntax error near `<br>`unexpected token `\|'    ` |
| ✅ | `\| ls \| wc              ` | `shell: syntax error near `<br>`unexpected token `\|'    ` | `shell: syntax error near `<br>`unexpected token `\|'    ` |
| ❌ | `ls \| wc \|              ` | `> > > echo "mensaje ignor`<br>`ado" mensaje ignorado    ` | `shell: syntax error near `<br>`unexpected token `newline`<br>`'                        ` |
| ✅ | `cd ..                    ` | `                         ` | `                         ` |
| ✅ | `rm -rf test_ls_syntax    ` | `                         ` | `                         ` |
| ✅ | `rm colors.txt            ` | `                         ` | `                         ` |
| ✅ | `rm -rf test_ls_syntax    ` | `                         ` | `                         ` |
| ✅ | `rm colors.txt            ` | `                         ` | `                         ` |
| ❌ | `echo "Tests finished"    ` | `                         ` | `Tests finished           ` |
| ✅ | `                         ` | `                         ` | `                         ` |
