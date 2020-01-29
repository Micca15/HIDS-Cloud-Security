import json
import os
import pdb
from threading import Thread
from scanner.main import Scanner
import uuid

Scanner_object = Scanner()


def create_standard_config():
    config = {
        'computer_name': os.environ['COMPUTERNAME'],
        'uuid': str(uuid.uuid1()),
        'interval': 30,
        'path': r'C:\Users\Danesh\Desktop',
        'whitelist': [],
        'logger_url': '192.168.123.123:5000'
    }
    print('Creating config file with the following data: ', config)

    with open('config.json', 'w') as json_object:
        json.dump(config, json_object)


# check if config.json file exists, else create a default one, then start the scanner.
def run_the_scanner():
    if os.path.exists('config.json'):
        with open('config.json') as json_file:
            data = json.load(json_file)
        Scanner_object.start_scanning(data['path'], data['interval'], data['whitelist'])
    else:
        print('No config.json found, creating a new default config.....')
        create_standard_config()
        with open('config.json') as json_file:
            data = json.load(json_file)
        Scanner_object.start_scanning(data['path'], data['interval'], data['whitelist'])


if __name__ == '__main__':
    Thread(target=run_the_scanner()).start()
