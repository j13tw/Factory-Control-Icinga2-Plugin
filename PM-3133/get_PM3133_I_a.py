#!/usr/bin/python3.6
import requests
import json
import os, sys
import socket


hostname = '10.20.0.68'					#chang to your service IP
port = '3001'							#chang to your service Port

localOS = os.system('uname 2>&1 >/var/tmp/os.txt')
if(localOS == 0):
	response = os.system('ping -c 1 ' + hostname + ' &>/var/tmp/ping.txt')
else:
	response = os.system('ping -n 1 ' + hostname + ' 2>&1 >ping.txt')

if response == 0:						# check network sevice & server is on
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((hostname, int(port)))
	if result == 0:
		sock.close()
		distance = 'http://' + hostname + ':' + port
		r = requests.get(distance)
		value = r.content.decode('utf-8')	# get return json value
		key = json.loads(value)
		PM3133_A_Json = key['PM3133_A_Json']
		I_a = PM3133_A_Json['I_a']
		print ('PM3133_I_a = ' + I_a + ' A')																								#
		sys.exit(0)
	else:
	   	print ('http://' + hostname +':' + port + ' Service Port Found !')
	   	sys.exit(1)   
else:
  	print ('http://', hostname, ' Server IP Not Found !')
  	sys.exit(1)