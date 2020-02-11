input_string = (input("Enter a string: ")).upper()
input_string = input_string.upper()
arrInputList = list(input_string)
counter = 0
currentChar =arrInputList[0]
print_string = "["
print("[")
for char in arrInputList:
	if char == currentChar:
		counter += 1
	else:
		print_string += currentChar.upper()+ counter
		print(f"{currentChar.upper()}[{counter}]")
		counter = 1
		currentChar = char

	
print(f"{currentChar.upper()}[{counter}]")
print("]")