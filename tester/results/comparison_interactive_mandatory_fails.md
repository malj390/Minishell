# Interactive Comparison (interactive - mandatory)
 (Fails Only)

**Results:** 139/337 match | 198 differ

| Status | Input | Bash Output | Minishell Output |
| :---: | :--- | :--- | :--- |
| ❌ | `echo "red" > colors.txt  ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `echo "green" >> colors.tx`<br>`t                        ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `echo "blue" >> colors.txt` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `echo "yellow" >> colors.t`<br>`xt                       ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `echo hello               ` | `[?2004l hello [?2004h  ` | `hello                    ` |
| ❌ | `echo -n noeol            ` | `[?2004l noeol[?2004h   ` | `noeol                    ` |
| ❌ | `echo -n                  ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `echo hello world         ` | `[?2004l hello world [?2`<br>`004h                     ` | `hello world              ` |
| ❌ | `echo ""                  ` | `[?2004l  [?2004h       ` | `                         ` |
| ❌ | `echo "  spaces  "        ` | `[?2004l  spaces [?2004h` | ` spaces                  ` |
| ❌ | `echo -n one -n two       ` | `[?2004l one -n two[?200`<br>`4h                       ` | `one -n two               ` |
| ❌ | `echo one two   three     ` | `[?2004l one two three [`<br>`?2004h                   ` | `one two three            ` |
| ❌ | `echo                     ` | `[?2004l  [?2004h       ` | `                         ` |
| ❌ | `echo "" hola             ` | `[?2004l  hola [?2004h  ` | ` hola                    ` |
| ❌ | `echo -n -n hola          ` | `[?2004l hola[?2004h    ` | `hola                     ` |
| ❌ | `echo -n -nh -n hola      ` | `[?2004l -nh -n hola[?20`<br>`04h                      ` | `-nh -n hola              ` |
| ❌ | `echo -nnnnnnnnn hola     ` | `[?2004l hola[?2004h    ` | `hola                     ` |
| ❌ | `echo 'echo "hola'        ` | `[?2004l echo "hola [?20`<br>`04h                      ` | `echo "hola               ` |
| ❌ | `echo $?hcudshfuewrf ew  w`<br>`r 4ew""""                ` | `[?2004l 0hcudshfuewrf ew`<br>` wr 4ew [?2004h         ` | `0hcudshfuewrf ew wr 4ew  ` |
| ❌ | `echo ""uhjkhnkj"hjbmb"'''`<br>`' defdjhfkjb "iujiouhj"f'`<br>`f'f'f'f''f'f'f'f'f'f'    ` | `[?2004l uhjkhnkjhjbmb de`<br>`fdjhfkjb iujiouhjffffffff`<br>`fff [?2004h             ` | `uhjkhnkjhjbmb defdjhfkjb `<br>`iujiouhjfffffffffff      ` |
| ❌ | `echo ""uhjkhnkj"hjbmb"'''`<br>`' defdjhfkjb "iujiouhj"f'`<br>`f'a'j'o''i'w'q''q        ` | `[?2004l uhjkhnkjhjbmb de`<br>`fdjhfkjb iujiouhjffajoiwq`<br>`q [?2004h               ` | `uhjkhnkjhjbmb defdjhfkjb `<br>`iujiouhjffajoiwqq        ` |
| ❌ | `echo ""aaaaaaaa"bbbbb"'''`<br>`' ccccccccc "dddddddd"e'e`<br>`'e                       ` | `[?2004l aaaaaaaabbbbb cc`<br>`ccccccc ddddddddeee [?20`<br>`04h                      ` | `aaaaaaaabbbbb ccccccccc d`<br>`dddddddeee               ` |
| ❌ | `echo "ho   $USER"  'la   `<br>`$LESS'   $USER$TERM      ` | `[?2004l ho malj la $LESS`<br>` maljxterm-256color [?20`<br>`04h                      ` | `ho 42user la $LESS 42user`<br>`xterm                    ` |
| ❌ | `echo "ho   $USER"'la   $L`<br>`ESS'$USER$TERM           ` | `[?2004l ho maljla $LESSm`<br>`aljxterm-256color [?2004`<br>`h                        ` | `ho 42userla $LESS42userxt`<br>`erm                      ` |
| ❌ | `echo"ho   $USER"         ` | `[?2004l shell: echoho ma`<br>`lj: command not found [?`<br>`2004h                    ` | `shell: echoho 42user: com`<br>`mand not found           ` |
| ❌ | `echo"ho   $USE$LESS"     ` | `[?2004l shell: echoho : `<br>`command not found [?2004`<br>`h                        ` | `shell: echoho : command n`<br>`ot found                 ` |
| ❌ | `"echo" "ho   $USER"      ` | `[?2004l ho malj [?2004h` | `ho 42user                ` |
| ❌ | `e"cho" "ho   $USER"      ` | `[?2004l ho malj [?2004h` | `ho 42user                ` |
| ❌ | `echo "ho   $USER"        ` | `[?2004l ho malj [?2004h` | `ho 42user                ` |
| ❌ | `echo "$HOME '$LESS' $USER`<br>`"                        ` | `[?2004l /home/malj '' ma`<br>`lj [?2004h              ` | `/home/42user '' 42user   ` |
| ❌ | `echo '$HOME "$LESS" $USER`<br>`'                        ` | `[?2004l $HOME "$LESS" $U`<br>`SER [?2004h             ` | `$HOME "$LESS" $USER      ` |
| ❌ | `echo '$'"HOME"           ` | `[?2004l $HOME [?2004h  ` | `$HOME                    ` |
| ❌ | `                         ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `pwd                      ` | `[?2004l /home/malj/00_Gi`<br>`thub/000_42Repos/Current/`<br>`003_08_Minishell-dev/Mini`<br>`shell/tester [?2004h    ` | `/app                     ` |
| ❌ | `cd /tmp                  ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `pwd                      ` | `[?2004l /tmp [?2004h   ` | `/tmp                     ` |
| ❌ | `cd /                     ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `pwd                      ` | `[?2004l / [?2004h      ` | `/                        ` |
| ❌ | `cd /usr/bin              ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `pwd                      ` | `[?2004l /usr/bin [?2004`<br>`h                        ` | `/usr/bin                 ` |
| ❌ | `cd ..                    ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `pwd                      ` | `[?2004l /usr [?2004h   ` | `/usr                     ` |
| ❌ | `cd .                     ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `pwd                      ` | `[?2004l /usr [?2004h   ` | `/usr                     ` |
| ❌ | `cd /nonexistent_directory`<br>`_xyz                     ` | `[?2004l shell: cd: /none`<br>`xistent_directory_xyz: No`<br>` such file or directory `<br>`[?2004h                  ` | `shell: cd: /nonexistent_d`<br>`irectory_xyz: No such fil`<br>`e or directory           ` |
| ❌ | `echo $?                  ` | `[?2004l 1 [?2004h      ` | `1                        ` |
| ❌ | `cd $_MSDIR               ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `export _SAVED_HOME=$HOME ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `unset HOME               ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `cd                       ` | `[?2004l shell: cd: HOME `<br>`not set [?2004h         ` | `shell: cd: HOME not set  ` |
| ❌ | `echo $?                  ` | `[?2004l 1 [?2004h      ` | `1                        ` |
| ❌ | `export HOME=$_SAVED_HOME ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `unset _SAVED_HOME        ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `cd $_MSDIR               ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `cd -                     ` | `[?2004l /home/malj/00_Gi`<br>`thub/000_42Repos/Current/`<br>`003_08_Minishell-dev/Mini`<br>`shell/tester [?2004h    ` | `/app                     ` |
| ❌ | `pwd                      ` | `[?2004l /home/malj/00_Gi`<br>`thub/000_42Repos/Current/`<br>`003_08_Minishell-dev/Mini`<br>`shell/tester [?2004h    ` | `/app                     ` |
| ❌ | `cd ~                     ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `pwd                      ` | `[?2004l /home/malj [?20`<br>`04h                      ` | `/home/42user             ` |
| ❌ | `cd $_MSDIR               ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `                         ` | `[?2004l [?2004h        ` | `                         ` |
| ❌ | `echo '$USER'             ` | `[?2004l $USER [?2004h  ` | `$USER                    ` |
| ❌ | `echo '$?'                ` | `[?2004l $? [?2004h     ` | `$?                       ` |
| ❌ | `echo 'hello world'       ` | `[?2004l hello world [?2`<br>`004h                     ` | `hello world              ` |
| ❌ | `echo ''                  ` | `[?2004l  [?2004h       ` | `                         ` |
| ❌ | `echo 'no \| pipe here'   ` | `[?2004l no \| pipe here `<br>`[?2004h                 ` | `no \| pipe here          ` |
| ❌ | `echo 'no > redirect'     ` | `[?2004l no > redirect [`<br>`?2004h                   ` | `no > redirect            ` |
| ❌ | `echo 'spaces   preserved'` | `[?2004l spaces preserved`<br>` [?2004h                ` | `spaces preserved         ` |
| ❌ | `echo '$USER is not expand`<br>`ed in single quotes'     ` | `                         ` | `$USER is not expanded in `<br>`single quotes            ` |
| ❌ | `echo "hello world"       ` | `                         ` | `hello world              ` |
| ❌ | `echo "spaces   preserved"` | `                         ` | `spaces preserved         ` |
| ❌ | `echo "cat lol.c \| cat > `<br>`lol.c"                   ` | `                         ` | `cat lol.c \| cat > lol.c ` |
| ❌ | `echo $DQTEST             ` | `                         ` | `expanded                 ` |
| ❌ | `echo "$DQTEST"           ` | `                         ` | `expanded                 ` |
| ❌ | `echo "value is $DQTEST en`<br>`d"                       ` | `                         ` | `value is expanded end    ` |
| ❌ | `echo "$?"                ` | `                         ` | `0                        ` |
| ❌ | `echo "'$USER'"           ` | `                         ` | `'42user'                 ` |
| ❌ | `echo '"$USER"'           ` | `                         ` | `"$USER"                  ` |
| ❌ | `echo '$COMPLICADO'       ` | `                         ` | `$COMPLICADO              ` |
| ❌ | `echo "'$COMPLICADO'"     ` | `                         ` | `''                       ` |
| ❌ | `echo '"$COMPLICADO"'     ` | `                         ` | `"$COMPLICADO"            ` |
| ❌ | `cat /tmp/ms_test_redir.tx`<br>`t                        ` | `                         ` | `first line               ` |
| ❌ | `cat /tmp/ms_test_redir.tx`<br>`t                        ` | `                         ` | `first line second line   ` |
| ❌ | `wc -l < /tmp/ms_test_redi`<br>`r.txt                    ` | `                         ` | `3                        ` |
| ❌ | `cat /tmp/ms_test_redir.tx`<br>`t                        ` | `                         ` | `overwrite                ` |
| ❌ | `cat /tmp/ms_rout1.txt    ` | `                         ` | `hola                     ` |
| ❌ | `cat /tmp/ms_rout1.txt    ` | `                         ` | `hola caracola            ` |
| ❌ | `cat /tmp/ms_rout3.txt    ` | `                         ` | `hola                     ` |
| ❌ | `cat << EOF               ` | `                         ` | `> line one > line two > l`<br>`ine three > EOF line one `<br>`line two line three      ` |
| ❌ | `grep "an" << WORDS       ` | `                         ` | `> apple > banana > cherry`<br>` > mango > WORDS banana m`<br>`ango                     ` |
| ❌ | `wc -l << COUNTER         ` | `                         ` | `> a > b > c > d > e > COU`<br>`NTER 5                   ` |
| ❌ | `echo hello \| cat        ` | `                         ` | `hello                    ` |
| ❌ | `echo hello \| cat \| cat ` | `                         ` | `hello                    ` |
| ❌ | `echo hello \| wc -c      ` | `                         ` | `6                        ` |
| ❌ | `/bin/ls /dev/null \| cat ` | `                         ` | `/dev/null                ` |
| ❌ | `echo "apple banana cherry`<br>`" \| tr ' ' '\n' \| sort ` | `                         ` | `apple banana cherry      ` |
| ❌ | `echo "abc" \| rev \| rev ` | `                         ` | `abc                      ` |
| ❌ | `cat /tmp/ms_pipe_a.txt \|`<br>` wc -l                   ` | `                         ` | `3                        ` |
| ❌ | `cat /tmp/ms_pipe_a.txt \|`<br>` grep "line" \| wc -l    ` | `                         ` | `3                        ` |
| ❌ | `cat /tmp/ms_pipe_b.txt   ` | `                         ` | `line3 line2 line1        ` |
| ❌ | `ls \| wc                 ` | `                         ` | ` 3 3 18                  ` |
| ❌ | `ls\|wc                   ` | `                         ` | ` 3 3 18                  ` |
| ❌ | `cat /tmp/ms_wc_out.txt   ` | `                         ` | ` 4 4 22                  ` |
| ❌ | `cat colors.txt \| wc     ` | `                         ` | ` 4 4 22                  ` |
| ❌ | `echo $TESTVAR            ` | `                         ` | `hello42                  ` |
| ❌ | `echo $TESTVAR            ` | `                         ` | `updated                  ` |
| ❌ | `echo $?                  ` | `                         ` | `0                        ` |
| ❌ | `echo $MY_VAR             ` | `                         ` | `hello                    ` |
| ❌ | `env \| grep MY_VAR       ` | `                         ` | `MY_VAR=hello             ` |
| ❌ | `echo $MY_VAR             ` | `                         ` | `updated                  ` |
| ❌ | `env \| grep MY_VAR       ` | `                         ` | `MY_VAR=updated           ` |
| ❌ | `echo "exit:$?"           ` | `                         ` | `exit:0                   ` |
| ❌ | `echo $A                  ` | `                         ` | `1                        ` |
| ❌ | `echo $B                  ` | `                         ` | `2                        ` |
| ❌ | `echo $C                  ` | `                         ` | `3                        ` |
| ❌ | `echo $A                  ` | `                         ` | `1                        ` |
| ❌ | `echo $C                  ` | `                         ` | `3                        ` |
| ❌ | `env \| grep -E "^A=\|^B=\`<br>`|^C=" \| sort            ` | `                         ` | `A=1 C=3                  ` |
| ❌ | `echo $a                  ` | `                         ` | `b                        ` |
| ❌ | `echo $b                  ` | `                         ` | `wawa                     ` |
| ❌ | `echo $b                  ` | `                         ` | `lala                     ` |
| ❌ | `echo $c                  ` | `                         ` | `lala=kaka                ` |
| ❌ | `echo "\|$a\|"            ` | `                         ` | `\|\|                     ` |
| ❌ | `echo $a3                 ` | `                         ` | `l                        ` |
| ❌ | `export 2a=lala           ` | `                         ` | `shell: export: `2a=lala':`<br>` not a valid identifier  ` |
| ❌ | `echo $NUEVA              ` | `                         ` | `xterm                    ` |
| ❌ | `echo $POLLOS             ` | `                         ` | `asados                   ` |
| ❌ | `echo $A $B               ` | `                         ` | `1 2                      ` |
| ❌ | `echo $a $b               ` | `                         ` | `o                        ` |
| ❌ | `echo $a                  ` | `                         ` | `==                       ` |
| ❌ | `export ""                ` | `                         ` | `shell: export: `': not a `<br>`valid identifier         ` |
| ❌ | `env                      ` | `                         ` | `HOSTNAME=42container SSH_`<br>`AUTH_SOCK=/ssh-agent PWD=`<br>`/app HISTFILE=/home/42use`<br>`r/.bash_history LS_COLORS`<br>`=rs=0:di=01;34:ln=01;36:m`<br>`h=00:pi=40;33:so=01;35:do`<br>`=01;35:bd=40;33;01:cd=40;`<br>`33;01:or=40;31;01:mi=00:s`<br>`u=37;41:sg=30;43:ca=30;41`<br>`:tw=30;42:ow=34;42:st=37;`<br>`44:ex=01;32:*.tar=01;31:*`<br>`.tgz=01;31:*.arc=01;31:*.`<br>`arj=01;31:*.taz=01;31:*.l`<br>`ha=01;31:*.lz4=01;31:*.lz`<br>`h=01;31:*.lzma=01;31:*.tl`<br>`z=01;31:*.txz=01;31:*.tzo`<br>`=01;31:*.t7z=01;31:*.zip=`<br>`01;31:*.z=01;31:*.dz=01;3`<br>`1:*.gz=01;31:*.lrz=01;31:`<br>`*.lz=01;31:*.lzo=01;31:*.`<br>`xz=01;31:*.zst=01;31:*.tz`<br>`st=01;31:*.bz2=01;31:*.bz`<br>`=01;31:*.tbz=01;31:*.tbz2`<br>`=01;31:*.tz=01;31:*.deb=0`<br>`1;31:*.rpm=01;31:*.jar=01`<br>`;31:*.war=01;31:*.ear=01;`<br>`31:*.sar=01;31:*.rar=01;3`<br>`1:*.alz=01;31:*.ace=01;31`<br>`:*.zoo=01;31:*.cpio=01;31`<br>`:*.7z=01;31:*.rz=01;31:*.`<br>`cab=01;31:*.wim=01;31:*.s`<br>`wm=01;31:*.dwm=01;31:*.es`<br>`d=01;31:*.jpg=01;35:*.jpe`<br>`g=01;35:*.mjpg=01;35:*.mj`<br>`peg=01;35:*.gif=01;35:*.b`<br>`mp=01;35:*.pbm=01;35:*.pg`<br>`m=01;35:*.ppm=01;35:*.tga`<br>`=01;35:*.xbm=01;35:*.xpm=`<br>`01;35:*.tif=01;35:*.tiff=`<br>`01;35:*.png=01;35:*.svg=0`<br>`1;35:*.svgz=01;35:*.mng=0`<br>`1;35:*.pcx=01;35:*.mov=01`<br>`;35:*.mpg=01;35:*.mpeg=01`<br>`;35:*.m2v=01;35:*.mkv=01;`<br>`35:*.webm=01;35:*.webp=01`<br>`;35:*.ogm=01;35:*.mp4=01;`<br>`35:*.m4v=01;35:*.mp4v=01;`<br>`35:*.vob=01;35:*.qt=01;35`<br>`:*.nuv=01;35:*.wmv=01;35:`<br>`*.asf=01;35:*.rm=01;35:*.`<br>`rmvb=01;35:*.flc=01;35:*.`<br>`avi=01;35:*.fli=01;35:*.f`<br>`lv=01;35:*.gl=01;35:*.dl=`<br>`01;35:*.xcf=01;35:*.xwd=0`<br>`1;35:*.yuv=01;35:*.cgm=01`<br>`;35:*.emf=01;35:*.ogv=01;`<br>`35:*.ogx=01;35:*.aac=00;3`<br>`6:*.au=00;36:*.flac=00;36`<br>`:*.m4a=00;36:*.mid=00;36:`<br>`*.midi=00;36:*.mka=00;36:`<br>`*.mp3=00;36:*.mpc=00;36:*`<br>`.ogg=00;36:*.ra=00;36:*.w`<br>`av=00;36:*.oga=00;36:*.op`<br>`us=00;36:*.spx=00;36:*.xs`<br>`pf=00;36: TERM=xterm USER`<br>`=42user SHLVL=3 LC_CTYPE=`<br>`en_US.UTF-8 PATH=/usr/loc`<br>`al/sbin:/usr/local/bin:/u`<br>`sr/sbin:/usr/bin:/sbin:/b`<br>`in DEBIAN_FRONTEND=nonint`<br>`eractive _=/usr/bin/expec`<br>`t OLDPWD=/app/test_ls_pip`<br>`e_wc MAIL=mlermo-j@studen`<br>`t.42malaga.com _MSDIR=/ap`<br>`p HOME=/home/42user DQTES`<br>`T=expanded C=3 a=== b=o c`<br>`=lala=kaka a3=l NUEVA=xte`<br>`rm                       ` |
| ❌ | `env lalal                ` | `                         ` | `env: ‘lalal’: No such fil`<br>`e or directory           ` |
| ❌ | `env directorio           ` | `                         ` | `env: ‘directorio’: No suc`<br>`h file or directory      ` |
| ❌ | `echo *.c                 ` | `                         ` | `foo.c                    ` |
| ❌ | `echo *.h                 ` | `                         ` | `foo.h                    ` |
| ❌ | `echo *.txt               ` | `                         ` | `bar.txt                  ` |
| ❌ | `ls *.c                   ` | `                         ` | `foo.c                    ` |
| ❌ | `ls *.h                   ` | `                         ` | `foo.h                    ` |
| ❌ | `echo *                   ` | `                         ` | `bar.txt foo.c foo.h      ` |
| ❌ | `cat < colors.txt         ` | `                         ` | `red green blue yellow    ` |
| ❌ | `cat copia.txt            ` | `                         ` | `red green blue yellow    ` |
| ❌ | `cat colors.txt \| wc     ` | `                         ` | ` 4 4 22                  ` |
| ❌ | `echo $?hcudshfuewrf ew  w`<br>`r 4ew""                  ` | `                         ` | `0hcudshfuewrf ew wr 4ew  ` |
| ❌ | `echo "ho   $USER"  "la   `<br>`$LESS"   $USER$TERM      ` | `                         ` | `ho 42user la 42userxterm ` |
| ❌ | `echo "ho   $USER"        ` | `                         ` | `ho 42user                ` |
| ❌ | `echo"ho   $USER"         ` | `                         ` | `shell: echoho 42user: com`<br>`mand not found           ` |
| ❌ | `e"cho" "ho   $USER"      ` | `                         ` | `ho 42user                ` |
| ❌ | `echo "ho   $USER"        ` | `                         ` | `ho 42user                ` |
| ❌ | `echo "$HOME" "$USER"     ` | `                         ` | `/home/42user 42user      ` |
| ❌ | `pwd                      ` | `                         ` | `/tmp/ms_user42_test/dir_e`<br>`xiste                    ` |
| ❌ | `cd directorio_no_existe  ` | `                         ` | `shell: cd: directorio_no_`<br>`existe: No such file or d`<br>`irectory                 ` |
| ❌ | `echo $?                  ` | `                         ` | `1                        ` |
| ❌ | `cd file_existe           ` | `                         ` | `shell: cd: file_existe: N`<br>`o such file or directory ` |
| ❌ | `echo $?                  ` | `                         ` | `1                        ` |
| ❌ | `pwd                      ` | `                         ` | `/home/42user             ` |
| ❌ | `ls \| wc                 ` | `                         ` | ` 2 2 19                  ` |
| ❌ | `ls\|wc                   ` | `                         ` | ` 2 2 19                  ` |
| ❌ | `cat colors.txt \| sort -r`<br>` \| wc                   ` | `                         ` | ` 1 1 12                  ` |
| ❌ | `cd -                     ` | `                         ` | `/tmp/ms_user42_test      ` |
| ❌ | `pwd                      ` | `                         ` | `/tmp/ms_user42_test      ` |
| ❌ | `pwd                      ` | `                         ` | `/home/42user             ` |
| ❌ | `ls                       ` | `                         ` | `shell: ls: No such file o`<br>`r directory              ` |
| ❌ | `echo $?                  ` | `                         ` | `127                      ` |
| ❌ | `/bin/ls                  ` | `                         ` | `colors.txt manual_tests r`<br>`esults test_exit_codes_si`<br>`gnals.sh compare_interact`<br>`ive_results.py minishell `<br>`run_noninteractive_tests.`<br>`py tester.exp interactive`<br>` non_interactive run_test`<br>`s.sh                     ` |
| ❌ | `echo $?                  ` | `                         ` | `0                        ` |
| ❌ | `ls noexiste              ` | `                         ` | `ls: cannot access 'noexis`<br>`te': No such file or dire`<br>`ctory                    ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `echo $?                  ` | `                         ` | `0                        ` |
| ❌ | `echo $?                  ` | `                         ` | `0                        ` |
| ❌ | `echo $?                  ` | `                         ` | `42                       ` |
| ❌ | `echo $?                  ` | `                         ` | `214                      ` |
| ❌ | `echo $?                  ` | `                         ` | `255                      ` |
| ❌ | `echo $?                  ` | `                         ` | `0                        ` |
| ❌ | `echo $?                  ` | `                         ` | `255                      ` |
| ❌ | `echo $?                  ` | `                         ` | `0                        ` |
| ❌ | `exit 9223372036854775808 ` | `                         ` | `shell: exit: 922337203685`<br>`4775808: numeric argument`<br>` required                ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `exit -9223372036854775809` | `                         ` | `shell: exit: -92233720368`<br>`54775809: numeric argumen`<br>`t required               ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `echo $?                  ` | `                         ` | `100                      ` |
| ❌ | `exit ++100               ` | `                         ` | `shell: exit: ++100: numer`<br>`ic argument required     ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `exit +++100              ` | `                         ` | `shell: exit: +++100: nume`<br>`ric argument required    ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `exit --100               ` | `                         ` | `shell: exit: --100: numer`<br>`ic argument required     ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `exit exit                ` | `                         ` | `shell: exit: exit: numeri`<br>`c argument required      ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `exit 42 53 64            ` | `                         ` | `shell: exit: too many arg`<br>`uments                   ` |
| ❌ | `echo $?                  ` | `                         ` | `1                        ` |
| ❌ | `exit hola mundo          ` | `                         ` | `shell: exit: hola: numeri`<br>`c argument required      ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `exit 42hola              ` | `                         ` | `shell: exit: 42hola: nume`<br>`ric argument required    ` |
| ❌ | `echo $?                  ` | `                         ` | `2                        ` |
| ❌ | `ls \|   \| wc            ` | `                         ` | `shell: syntax error near `<br>`unexpected token `\|'    ` |
| ❌ | `\| ls \| wc              ` | `                         ` | `shell: syntax error near `<br>`unexpected token `\|'    ` |
| ❌ | `ls \| wc \|              ` | `                         ` | `shell: syntax error near `<br>`unexpected token `newline`<br>`'                        ` |
| ❌ | `echo "Tests finished"    ` | `                         ` | `Tests finished           ` |
