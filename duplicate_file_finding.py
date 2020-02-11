import json
import os
import glob
import hashlib


def findDuplicateFiles(filesDir):

	unique = dict()
	for filename in filesDir:
	    if os.path.isfile(filename):
	        filehash = hashlib.md5(open(filename, 'rb').read()).hexdigest()

	        fileSize = os.path.getsize(filename)
	        fileSizeString = ""

	        sizeUnit = ""
	        if fileSize > 1023:
	        	fileSizeString = (fileSize/1024)
	        	sizeUnit = " KB"
	        else:
	        	fileSizeString = fileSize
	        	sizeUnit = " bytes"		
	        

	        if filehash not in unique: 
	            unique[filehash] = filename
	        else:
	            print (filename , ' is a duplicate of ' , unique[filehash], ' and size is %0.0f' % (fileSizeString), sizeUnit)


findDuplicateFiles(glob.glob("jsonDir/*.json"))




		
	