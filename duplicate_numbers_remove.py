
def removeDuplicate(fromList):
	numberList = []
	for element in fromList:
		if element not in numberList:
			numberList.append(element)

	return numberList		
		
print(removeDuplicate([1,2,3,4,5,5,6,2,3,4,5,9,8]))