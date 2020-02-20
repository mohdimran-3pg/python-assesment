class reverse_iter:
	argList = []

	def __init__(self, objList):
		self.argList = objList

	
	def getReverseOrderofList(self):
			
			cnt = len(self.argList) - 1
			tempList = []
			index = 0
			while cnt >= 0:

				tempList.append(self.argList[cnt])
				cnt -= 1
				index += 1

			return (tempList)



arrList = [2,3,41,1,89,28,7]
iterator = reverse_iter(arrList)
print(iterator.getReverseOrderofList())