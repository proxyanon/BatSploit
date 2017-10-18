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
import os, sys
os.system("cls") # if windows
#os.system("clear") # if linux or mac
sys.stdout.write("\n[+] Setup BatSploit 2\n")
try:
	try:
		from termcolor import colored
		from colorama import init
		init()
		sys.stdout.write(colored("\n[+]", "green"))
		sys.stdout.write(colored(" BatSploit 2.0 is installed !\n", "white"))
		sys.stdout.flush()
		sys.exit()
	except ImportError:
		quest = raw_input("\n[?] Do you want install modules needed [Y/N] : ")
		if quest == "N" or quest == "n":
			sys.stdout.write("\n[X] Saindo ...\n")
			sys.exit()
		elif quest == "Y" or quest == "y" or quest == "":
			sys.stdout.write("\n[+] Installing modules\n")
			os.system("pip install colorama && pip install termcolor")
			sys.stdout.flush()
except KeyboardInterrupt:
	sys.stdout.write("\n[X] Saindo ...\n")
	sys.exit()

