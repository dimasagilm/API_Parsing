import requests
from requests.auth import HTTPBasicAuth
import json
import urllib

src = raw_input('Masukkan Source: ')
dst = raw_input('Masukkan Destination: ')

src1 = urllib.quote_plus(src)
dst1 = urllib.quote_plus(dst)
urla1 = 'http://127.0.0.1:8181/onos/v1/paths/'+src1+'/'+dst1+'/disjoint'

output = requests.get(urla1, auth=HTTPBasicAuth('karaf','karaf'))
data = json.loads(output.content)

for t in data['paths']:
	t1 = (t['primary']['cost'])
	print ('Total links primary= %d') %(t1)
	t3 = (t['primary']['links'][0]['src']['host'])
	t4 = (t['primary']['links'][0]['dst']['device'])
	t5 = (t['primary']['links'][1]['dst']['device'])
	t6 = (t['primary']['links'][2]['dst']['device'])	
	print ('Host asal =' + t3)
	print ('Device pertama yang dilewati =' +t4)
	print ('Device kedua yang dilewati =' +t5)
	print ('Device ketiga yang dilewati=' +t6)


	t2 = (t['backup']['cost'])
	print ('\nTotal links backup= %d') %(t2)


	

	
	

