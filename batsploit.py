#-*-coding: utf8-*-
import sys, platform
from core import BatSploit
'''
@Author : Daniel Victor Freire Feitosa
@Version : 2.0
@Name : BatSploit
@Language : Python 2.7

<danielfreire56@hotmail.com>

Tool Open-Source, qualquer mudança pra melhor é bem vinda, os textos estão em inglês pq é mais simples não ter
que acentuar tudo, e também é uma língua universal, mas os comentários estão em pt-br 
'''
batsploit = BatSploit('BatSploit', '2.0', platform.system())
batsploit.banner()
if len(sys.argv) < 2:
	batsploit.usage(sys.argv[0])
else:
	if len(sys.argv) == 2:
		if sys.argv[1] == "-list":
			batsploit.list_payloads() # lista todos os payloads do script
		elif sys.argv[1] == "-bind":
			batsploit.usage_bind(sys.argv[0]) # mostra como o bind é usado
		elif sys.argv[1] == "-payload":
			batsploit.usage_payload(sys.argv[0]) # mostra como o create payloads é usado
	elif len(sys.argv) >= 4:
		if sys.argv[1] == "-bind":
			lhost = sys.argv[2] # local host para escutar a conexão dos payloads
			lport = sys.argv[3] # local port para escutar a conexão dos payloads
			if "=" not in lhost or "=" not in lport:
				batsploit.usage_bind(sys.argv[0]) # mostra como o bind é usad
			else:
				batsploit.bind(lhost, lport)
		if sys.argv[1] == "-payload":
			if len(sys.argv) == 6:
				payload = sys.argv[2]
				lhost = sys.argv[3] # local host para o payload se conectar
				lport = sys.argv[4] # local port para o pauload se conectar
				name = sys.argv[5] # nome do payload
				if "=" not in lhost or "=" not in lport:
					batsploit.usage_payload(sys.argv[0])  # mostra como o create payloads é usado
				else:
					batsploit.create_payload(payload, lhost, lport, name)
					if payload == 'python/batsploit_reverse_tcp':
						quest = raw_input("\n[?] Do you want start handler [Y/N] : ") # pergunta se quer que inicie o handler automáticamente
						if quest == "N" or quest == "n":
							sys.exit()
						else:
							batsploit.bind(lhost, lport)
					elif 'meterpreter' in payload:
						sys.exit()
					else:
						quest = raw_input("\n[?] Do you want start handler [Y/N] : ") # pergunta se quer que inicie o handler automáticamente
						if quest == "N" or quest == "n":
							sys.exit()
						else:
							batsploit.nc_bind(lhost, lport)
			else:
				batsploit.usage_payload(sys.argv[0])  # mostra como o create payloads é usado
