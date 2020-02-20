def splitMultipleFiles():
	
	numberofLines = int(input("Please enter number of lines:"))
	userFilename = ""
	file = ""
	while True:
		try:
			userFilename = str(input("Please enter file name:"))
			filename = f"dummyFiles/{userFilename}.txt"
			with open(filename, "r") as file:
				noOfLinesCnt = 0
				loop = 1
				for line in file:

					if noOfLinesCnt >= numberofLines:
						loop += 1
						noOfLinesCnt = 0
						
					newfilename = f"dummyFiles/{(loop)}-{userFilename}.txt"
					newFile = open(newfilename, "a+")
					newFile.write(line)
					noOfLinesCnt += 1
		except FileNotFoundError:
			print("There is no file, please try again")
		else:
			break

splitMultipleFiles()