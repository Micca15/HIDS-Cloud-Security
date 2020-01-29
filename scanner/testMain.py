import threading
import os
import hashlib
from helpers.fileProcessor import readfile


class ScannerClass(object):
    def __init__(self, path, interval, white_listed_files):
        self.path = path
        self.interval = interval
        self.whiteList = white_listed_files
        self.hashes = []
        self.combinedPathAndHash = []
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()

    def start(self):
        for r, d, f in os.walk(self.path):
            for file in f:
                if file in self.whiteList:
                    continue
                currentFile = os.path.join(r, file)
                currentModifiedDate = os.path.getmtime(self.path)
                hashContent = (str(readfile(currentFile)) + str(currentModifiedDate))
                self.hashes.append(hashlib.md5(hashContent.encode('utf-8')))
                self.combinedPathAndHash[currentFile] = hashlib.md5(hashContent.encode('utf-8')).digest()
