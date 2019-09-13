inputString = "123456"
startIndex = 0
inputString = list(inputString)
endIndex = len(inputString) - 1
for index in inputString:
	startChar = inputString[startIndex]
	endChar = inputString[endIndex]
	inputString[startIndex] = endChar
	inputString[endIndex] = startChar
	endIndex -= 1
	startIndex += 1
	if endIndex <= startIndex:
		break

inputString = "".join(inputString)
print(inputString)		


number = 12
reverse = 0
while number > 0:
	reminder = number % 10
	reverse = (reverse * 10) + reminder
	number = number //10
print("Reverse:::",reverse)	

print(29 // 10)