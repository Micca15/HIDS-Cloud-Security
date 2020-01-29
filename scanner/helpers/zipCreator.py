from zipfile import ZipFile

zipObj = ZipFile('sample.zip', 'w')

# Add multiple files to the zip
zipObj.write('sample_file.csv')
zipObj.write('test_1.log')
zipObj.write('test_2.log')

# close the Zip File
zipObj.close()