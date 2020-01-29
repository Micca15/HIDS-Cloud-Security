from testMain import ScannerClass
from time import sleep
import os
import hashlib
from helpers.fileProcessor import readfile
import json

files = []
timeStampsLastModified = []
hashes = []
whitelistedFiles = ['randomtext.txt']
combinedPathAndHash = {}
interval = 1
path = r"C:\Users\Danesh\Documents\Pythontestfolder"

print("starting...")
scanner_object = ScannerClass(path, interval, whitelistedFiles) # it auto-starts, no need of rt.start()
scanner_object.stop()  # better in a try/finally block to make sure the program ends!


# path = input("Enter the to be scanned path ")


print(combinedPathAndHash)
print('Number of files: ', len(files))
print('Number of timestamps: ', len(timeStampsLastModified))
print('Number of hashes: ', len(hashes))
