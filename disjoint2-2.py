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
	print ('\n::>Primary-links cost= %d') %(t1)
	t3 = (t['primary']['links'][0]['dst']['device'])
	t5 = (t['primary']['links'][1]['dst']['device'])
	t7 = (t['primary']['links'][2]['dst']['device'])	
	print ('Switch pertama =' +t3)
	print ('Switch kedua=' +t5)
	print ('Swicth ketiga=' +t7)
	t2 = (t['backup']['cost'])
	print ('\n::>Backup-links cost= %d') %(t2)
	t4 = (t['backup']['links'][0]['dst']['device'])
	t6 = (t['backup']['links'][1]['dst']['device'])
	t8 = (t['backup']['links'][2]['dst']['device'])	
	print ('Switch pertama =' +t4)
	print ('Switch kedua=' +t6)
	print ('Swicth ketiga=' +t8)

volumedata= input('\n::>Masukkan besar data yang akan ditransfer (kByte)=')

primer = (volumedata * 8) / 10000 
bekap =  (volumedata * 8) / 10000

print ('Waktu jalur primer= %d detik') %(primer)
print ('Waktu jalur backup= %dclear detik') %(bekap)



	

	
	

