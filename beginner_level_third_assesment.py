def sortCSVFileData():
	companyA = {}
	companyB = {}
	companyC = {}	
	file = open('CompanySpreadsheet.csv')
	reader = file.read()
	data = reader.split("\n")
	header = data[0].split(",")
	index = 1
	while index < len(data):
		saleData = data[index].split(",")
		companyA[saleData[2]] = {"year":  saleData[0], "month":  saleData[1]}
		companyB[saleData[3]] = {"year":  saleData[0], "month":  saleData[1]}
		companyC[saleData[4]] = {"year":  saleData[0], "month":  saleData[1]}
		index += 1

	companyAKeys = sorted(companyA.keys())
	companyBKeys = sorted(companyB.keys())
	companyCKeys = sorted(companyC.keys())

	print(header[2])
	for key in companyAKeys:
		print("Year: ", companyA[key]["year"], "\t Month: ", companyA[key]["month"][:3], "\t Sale: ", key)

	print(f"\n\n{header[3]}")
	for key in companyBKeys:
		print("Year: ", companyB[key]["year"], "\t Month: ", companyB[key]["month"][:3], "\t Sale: ", key)

	print(f"\n\n{header[4]}")
	for key in companyCKeys:
		print("Year: ", companyC[key]["year"], "\t Month: ", companyC[key]["month"][:3], "\t Sale: ", key)


sortCSVFileData()	    