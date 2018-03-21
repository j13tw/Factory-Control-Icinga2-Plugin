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
#		print (json.dumps(key , sort_keys=True, indent=4, separators=(',', ': ')))	# show on the all split json format
#		change the json key to local temp value
		DL303_co2 = key['DL303_co2']
		DL303_humi = key['DL303_humi']
		DL303_temp = key['DL303_temp']
		DL303_dewp = key['DL303_dewp']
		ET7044_status = key['ET7044_status'].split('[')[1].split(']')[0].split(',')
		PM3133_A_Json = key['PM3133_A_Json']
		V_a = PM3133_A_Json['V_a']
		I_a = PM3133_A_Json['I_a']
		kW_a = PM3133_A_Json['kW_a']
		kvar_a = PM3133_A_Json['kvar_a']
		kVA_a = PM3133_A_Json['kVA_a']
		PM3133_B_Json = key['PM3133_B_Json']
		V_b = PM3133_B_Json['V_b']
		I_b = PM3133_B_Json['I_b']
		kW_b = PM3133_B_Json['kW_b']
		kvar_b = PM3133_B_Json['kvar_b']
		kVA_b = PM3133_B_Json['kVA_b']
		PM3133_C_Json = key['PM3133_C_Json']
		V_c = PM3133_C_Json['V_c']
		I_c = PM3133_C_Json['I_c']
		kW_c = PM3133_C_Json['kW_c']
		kvar_c = PM3133_C_Json['kvar_c']
		kVA_c = PM3133_C_Json['kVA_c']
#####################################################################################################################################
		print('Service IP : http://' + hostname + ':' + port)																		#
		print('-----------------------------------------')																			#
		print ('DL303_co2 = ' + DL303_co2)																							#
		print ('DL303_humi = ' + DL303_humi)																						#
		print ('DL303_temp = ' + DL303_temp)																						#
		print ('DL303_dewp = ' + DL303_dewp)																						#
		print('-----------------------------------------')																			#
		print('ET7044_status_A = ' + ET7044_status[0])																				#
		print('ET7044_status_B = ' + ET7044_status[1])																				#
		print('ET7044_status_C = ' + ET7044_status[2])																				#
		print('ET7044_status_D = ' + ET7044_status[3])																				#
		print('ET7044_status_E = ' + ET7044_status[4])																				#
		print('ET7044_status_F = ' + ET7044_status[5])																				#
		print('ET7044_status_G = ' + ET7044_status[6])																				#
		print('ET7044_status_H = ' + ET7044_status[7])																				#
		print('-----------------------------------------')																			#
		print ('PM3133_V_a = ' + V_a)																								#
		print ('PM3133_I_a = ' + I_a)																								#
		print ('PM3133_kW_a = ' + kW_a)																								#
		print ('PM3133_kvar_a = ' + kvar_a)																							#
		print ('PM3133_kVA_a = ' + kVA_a)																							#
		print('-----------------------------------------')																			#
		print ('PM3133_V_b = ' + V_b)																								#
		print ('PM3133_I_b = ' + I_b)																								#
		print ('PM3133_kW_b = ' + kW_b)																								#
		print ('PM3133_kvar_b = ' + kvar_b)																							#
		print ('PM3133_kVA_b = ' + kVA_b)																							#
		print('-----------------------------------------')																			#
		print ('PM3133_V_c = ' + V_c)																								#
		print ('PM3133_I_c = ' + I_c)																								#
		print ('PM3133_kW_c = ' + kW_c)																								#
		print ('PM3133_kvar_c = ' + kvar_c)																							#
		print ('PM3133_kVA_c = ' + kVA_c)																							#
		print('-----------------------------------------') 																			#
#####################################################################################################################################
		sys.exit(0)
	else:
	   	print ('http://' + hostname +':' + port + ' Service Port Found !')
	   	sys.exit(1)   
else:
  	print ('http://', hostname, ' Server IP Not Found !')
  	sys.exit(1)