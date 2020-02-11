import json
import os
import glob

customTotal = 0

def countDictKeys(customDict):

	global customTotal
	arrKeys = customDict.keys()
	customTotal += len(arrKeys)
	for key in arrKeys:
		if type(customDict[key]) == dict:
			countDictKeys(customDict[key])

	return customTotal			


def getJsonKeyCount(file_path):

	with open (file_path) as json_file:
		data = json.load(json_file)
		return countDictKeys(data)

		
value = getJsonKeyCount("jsonDir/nested-json.json")
print("Total Score:::",value)
	   