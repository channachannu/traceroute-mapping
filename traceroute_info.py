import ipinfo
import pprint
import subprocess
import sys

def getDetails(ip):
	access_token = '08b7e0d032fc4d'
	handler = ipinfo.getHandler(access_token)
	details = handler.getDetails(ip)
	pprint.pprint(details.all)

def ipDetails(ip):
	access_token = '08b7e0d032fc4d'
	handler = ipinfo.getHandler(access_token)
	details = handler.getDetails(ip)
	#pprint.pprint(details.all)
	ip_info = {}
	if details.details['country_name']:
		ip_info['city'] = details.details['city']
		if details.details.get('org'):
			ip_info['org'] = details.details['org']
		elif details.details.get('hostname'):
			ip_info['org'] = details.details['hostname']
		else:
			ip_info['org'] = ''
		print(str(ip) + '\t' + ip_info['city'] + '\t'+ ip_info['org'])


if __name__ == '__main__':
	if sys.argv[1]:
		ip_address = str(sys.argv[1])
		#print(ip_address,type(ip_address))
		t = subprocess.Popen(('traceroute','-n',ip_address),stdout=subprocess.PIPE)
		v = subprocess.check_output(['grep','-o','[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'],stdin=t.stdout)
		v = v.decode('utf-8').split()
		for ip in v:
			ipDetails(ip)
	else:
		print("Please enter the ip address")
		print("Usage: python traceroute_info.py 8.8.8.8")
		exit()



