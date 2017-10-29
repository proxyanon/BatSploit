#-*-coding: utf8-*-
'''
@Author : Daniel Victor Freire Feitosa
@Version : 2.0
@Name : BatSploit
@Language : Python 2.7

<danielfreire56@hotmail.com>

Tool Open-Source, qualquer mudança pra melhor é bem vinda, os textos estão em inglês pq é mais simples não ter
que acentuar tudo, e também é uma língua universal, mas os comentários estão em pt-br 
'''
import os, sys, platform
os_id = platform.uname()

if os_id[0] == "Windows":
	os.system("cls")
elif os_id[0] == "Linux":
	os.system("clear")
sys.stdout.write("\n[+] Setup BatSploit 2\n")

def install_libs(so):
	if so == "Windows":
		os.system("pip install requests && pip install termcolor && pip install colorama && pip install pyinstaller")
	elif so == "Linux":
		os.system("pip install requests && pip install termcolor && pip install colorama")

def check_and_install_libs(so):
	try:
		# verifica as bibliotecas necessarias
		import requests
		from termcolor import colored
		from colorama import init
		init()
		return 0
	except ImportError:
		install_libs(so)

def check_dependencies(so):
	# verifica se existem os compiladores de c++
	if so == "Windows":
		if os.path.exists("cpp/bin") == True:
				return 0
		else:
				return 1
	elif so == "Linux":
		cmd = os.popen("i586-mingw32msvc-gcc --version")
		if 'Copyright' in cmd.read():
			return 0
		else:
			return 1

def check_and_install_dependencies(so, quest):
	# verifica e instala se necessário os compiladores de c++
	if os.path.exists("compiled") == False:
		try:
			if so == "Linux":
				os.makedirs("compiled")
				os.system("sudo chmod 777 compiled")
			elif so == "Windows":
				os.makedirs("compiled")
		except WindowsError:
			pass
	else:
		pass
	# verifica os compiladores de c++
	if so == "Windows":
		if os.path.exists("cpp/bin") == False:
			if quest == "N" or quest == "n":
				return 0
			else:
				os.makedirs("cpp")
				r=requests.get("https://eternallybored.org/misc/wget/current/wget.exe")
				with open("wget.exe", "wb") as code:
					code.write(r.content)
				os.system('move "wget.exe" "cpp/" > null && del null && cd cpp && wget -O mingw.rar https://sourceforge.net/p/mingw32/code/ci/master/tree/mingw.rar?format=raw && wget -O unrar.exe https://sourceforge.net/p/mingw32/code/ci/master/tree/UnRAR.exe?format=raw')
				os.system('cd cpp && unrar x mingw.rar && del mingw.rar && del unrar.exe && del wget.exe')
	elif so == "Linux":
		cmd = os.popen("i586-mingw32msvc-gcc --version")
		if 'Copyright' in cmd.read():
			return 0
		else:
			os.system("sudo apt-get install g++ gcc cpp aptitude && aptitude install mingw32")


try:
	print "\n[+] Platform : %s"%(os_id[0])
	print "[+] Arch : %s"%(os_id[4])
	if check_and_install_libs(os_id[0]) == 0:
		print "\n[+] All dependencies are installed"
	else:
		print "\n[+] Downloading and installing dependencies"
		check_and_install_libs(os_id[0])
	if check_dependencies(os_id[0]) == 0:
		print "\n[+] BatSploit 2 is complete, run : batsploit.py"
		sys.exit()
	else:
		quest = raw_input("[?] Do want install compillers to C++ [Y/N] : ")
		if quest == "N" or quest == "n":
			sys.exit()
		else:
			print "\n---------------- This may take a while :( ----------------\n"
			print "[+] Creating dirs"
			print "[+] Download compilers, don't close the window !"
			if check_and_install_dependencies(os_id[0], quest) == 0:
				from termcolor import colored
				from colorama import init
				init()
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored(" All requisists are satisfied\n, run batsploit.py", "white", attrs='blink'))
				sys.stdout.flush()
				sys.exit()
			else:
				print "[+] Download complete !"
				print "\n[+] Setup finalized, try run setup.py now\n"
				sys.stdout.flush()
except KeyboardInterrupt:
	sys.stdout.write("\n[X] Saindo ...\n")
	sys.exit()