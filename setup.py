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
try:
	print "\n[+] Platform : %s"%(os_id[0])
	print "[+] Arch : %s"%(os_id[4])

	try:
		import requests
		from termcolor import colored
		from colorama import init
		init()
		if os_id[0] == "Windows":
			if os.path.exists("cpp/bin") == False:
				quest_1 = raw_input("[?] Do want install compillers to C++ [Y/N] : ")
				if quest_1 == "N" or quest_1 == "n":
					sys.exit()
				else:
					print "\n---------------- This may take a while :( ----------------\n"
					print "[+] Creating dirs"
					os.system("mkdir cpp")
					print "[+] Download compilers, don't close the window !"
					r=requests.get("https://eternallybored.org/misc/wget/current/wget.exe")
					with open("wget.exe", "wb") as code:
						code.write(r.content)
					print ""
					os.system('move "wget.exe" "cpp/" > null && del null && cd cpp && wget -O mingw.rar https://sourceforge.net/p/mingw32/code/ci/master/tree/mingw.rar?format=raw && wget -O unrar.exe https://sourceforge.net/p/mingw32/code/ci/master/tree/UnRAR.exe?format=raw')
					os.system('cd cpp && unrar x mingw.rar && del mingw.rar && del unrar.exe && del wget.exe')
					print "[+] Download complete !"
					print "[+] Decompressing MinGW"
		elif os_id[0] == "Linux":
			print "[+] Creating dirs"
			print "[+] Download compilers"
			os.system("sudo apt-get install g++ cpp gcc mingw32")
		sys.stdout.write(colored("\n[+]", "green"))
		sys.stdout.write(colored(" BatSploit 2.0 is installed !\n", "white"))
		sys.stdout.write(colored("\n[+]", "green"))
		sys.stdout.write(colored(" Setup finalized, try run setup.py again !\n", "white"))
		sys.stdout.flush()
		sys.exit()
	except ImportError:
		quest = raw_input("\n[?] Do you want install modules needed [Y/N] : ")
		if quest == "N" or quest == "n":
			sys.stdout.write("\n[X] Saindo ...\n")
			sys.exit()
		elif quest == "Y" or quest == "y" or quest == "":
			sys.stdout.write("\n[+] Installing modules\n")
			os.system("pip install colorama && pip install termcolor && pip install requests")
			sys.stdout.write("\n[+] Setup finalized, try run setup.py now\n")
			sys.stdout.flush()
except KeyboardInterrupt:
	sys.stdout.write("\n[X] Saindo ...\n")
	sys.exit()

