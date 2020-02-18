import os
import glob

def getNumberofLines(totalLines):
	
	contentCounter = 0
	lines = ""
	while contentCounter < totalLines:
		lines = lines + "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\r\n\r\n"
		contentCounter += 1

	return lines	


def createMultipleFiles():
	
	numberofLines = int(input("Please enter number of lines:"))
	userFilename = str(input("Please enter file name:"))

	fileCounter = 0
	while fileCounter < 3:
		fileCounter += 1
		filename = f"dummyFiles/{fileCounter}-{userFilename}"
		fileContent = "This is content"
		file = open(filename, "w+")
		file.write(getNumberofLines(numberofLines))



createMultipleFiles()		


		

