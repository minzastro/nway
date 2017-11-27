from __future__ import print_function, division

def checkupdates(current_version=None):
	try:
		import os
		if current_version is None:
			current_version = open(os.path.join(os.path.abspath(
				os.path.dirname(__file__)), 'VERSION')).read().strip()
		import json
		from StringIO import StringIO
		import urllib3
		import certifi
		http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
		r = http.request('GET', 'https://pypi.python.org/pypi/nway/json')
		j = json.load(StringIO(r.data))
		version = j['info']['version']
		if current_version != version:
			print()
			print('A newer version of NWAY seems to be available.')
			print('Please update because it may fix bugs.')
			print()
	except Exception as e:
		pass
	except ImportError as e:
		pass
	except IOError as e:
		pass
	
