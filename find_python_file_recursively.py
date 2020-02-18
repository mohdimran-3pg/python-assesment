import os
import glob


otherFileCounter = 0
pythonFileCounter = 0
def findAllPythonFiles(dirPath):

	global pythonFileCounter, otherFileCounter

	arrContents = glob.glob(dirPath)
	
	for content in arrContents:
		if os.path.isdir(f"./{content}") == True:
			findAllPythonFiles(f"{content}/*")
		else:
			if content.find(".py") != -1:
				pythonFileCounter += 1
			else:
				otherFileCounter += 1	
					
	
	return (f"Total Python Files:{pythonFileCounter}", f"Total Other Files:{otherFileCounter}")	
		



output = findAllPythonFiles("*")	

print(output[0], "\n", output[1])



		

