import os
import hashlib
import time
from scanner.helpers.fileProcessor import readfile
import requests
import json
import pdb


class Scanner:
    def __init__(self):
        self.FileToCompare = []
        self.HashToCompare = []
        self.error_files = []
        self.whitelist = []
        self.path = ''
        self.interval = 30
        self.number_of_scans = 0

    def start_scanning(self, path, interval, whitelist):
        self.path = path
        self.interval = interval
        self.whitelist = whitelist
        self.scan_directories()

    def scan_directories(self):
        files = []
        for rootDir, dirs, filess in os.walk(self.path):
            if self.check_dirname_in_whitelist(rootDir):
                continue
            for file in filess:
                if file in self.whitelist or self.check_extension_in_whitelist(file):
                    continue
                file_and_hash_obj = {}
                current_file = os.path.join(rootDir, file)
                current_modified_date = os.path.getmtime(current_file)
                hash_content = (str(readfile(current_file)) + str(current_modified_date))
                hash_as_bytestream = hashlib.md5(hash_content.encode('UTF-8')).digest()
                file_and_hash_obj.update({"path": rootDir})
                file_and_hash_obj.update({"file": file})
                file_and_hash_obj.update({"hash": hash_as_bytestream.hex()})
                files.append(file_and_hash_obj)
        send_data_to_logger(files)
        self.number_of_scans += 1
        print('Number of scans: ', self.number_of_scans)
        time.sleep(self.interval)
        self.scan_directories()

    def check_dirname_in_whitelist(self, directory):
        for whitelist_element in self.whitelist:
            if whitelist_element[0:1] == '\\':
                if whitelist_element == directory[-len(whitelist_element):]:
                    return True

    def check_extension_in_whitelist(self, file):
        for whitelist_element in self.whitelist:
            if whitelist_element[0] == '.':
                if file.endswith(whitelist_element):
                    return True


def send_data_to_logger(files):
    with open('config.json') as json_config:
        data = json.load(json_config)
        request_data = {
            "uuid": data['uuid'],
            "computer": data['computer_name'],
            "files": files
        }
    url = 'http://' + data['logger_url']
    response = requests.post(url=url, json=request_data)
