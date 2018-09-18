import requests
from requests.auth import HTTPBasicAuth
import json

print "\nSelamat datang di MyApps\nIni adalah informasi Topology Anda"

print "\nInformasi SWITCH"
print "---------------------"

url1 = 'http://127.0.0.1:8181/onos/v1/devices'
response = requests.get(url1, auth=HTTPBasicAuth('karaf','karaf'))

qu = json.loads(response.content)

for y in qu['devices']:
	y1 = (y['type'])
	y2 = (y['id'])
	y3 = (y['hw'])
	y4 = (y['mfr'])
	y5 = (y['annotations']['protocol'])
	y6 = (y['annotations']['channelId'])
	print ('\nDevices=' + y1)
	print ('ID=' + y2)
	print ('Hardware=' + y3)
	print ('Manufactur=' + y4)
	print ('Protocol=' + y5)
	print ('Channel=' + y6)

print "\nInformasi HOST"
print "--------------------"

url2 = 'http://127.0.0.1:8181/onos/v1/hosts'
response2 = requests.get(url2, auth=HTTPBasicAuth('karaf','karaf'))
qu2 = json.loads(response2.content)

for x in qu2['hosts']:
	x1 = (x['mac'])
	x2 = (x['ipAddresses'][0])
	x3 = (x['locations'][0]['port'])
	x4 = (x['locations'][0]['elementId'])
	x5 = (x['id'])
	x6 = (x['vlan'])
	print ('\nHost ID=' + x5)
	print ('IP Address=' + x2)
	print ('MAC Address=' + x1)
	print ('VLAN=' + x6)
	print ('Terkoneksi dengan SWITCH ID=' + x4)
	print ('Terkoneksi pada port=' + x3)

	


	

