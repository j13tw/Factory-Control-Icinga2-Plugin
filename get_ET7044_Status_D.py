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
		ET7044_status = key['ET7044_status'].split('[')[1].split(']')[0].split(',')
		print('ET7044_status_D = ' + ET7044_status[3])																				#
		sys.exit(0)
	els