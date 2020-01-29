import requests
import json
import threading
import simplejson

# this file is used to communicate with the scanner (only for dev purposes)

ip_address = '127.0.0.1'
port = '12345'
endpoint = '/config'
# defining the api-endpoint
API_ENDPOINT = 'http://' + ip_address + ':' + port + endpoint

# your source code here
whitelistedFiles = ['asdfasdf', '3129872839-14']
interval = 2
path = r"C:\Users\DaneshLachman\Downloads"

dataToSend = {'whitelist': json.dumps(whitelistedFiles),
              'interval': json.dumps(interval),
              'path': json.dumps(path)
              }

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=dataToSend)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)