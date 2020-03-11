def planHouseSeating():
	print("The four houses are below\n\n (Gryffindor > G, Slytherin > S, HufflePuff > H, Ravenclaw > R)")
	input_string = (input("Enter Audience Seating plan: ")).upper()
	input_string = input_string.upper()
	arrInputList = list(input_string)
	counter = 0
	currentChar =arrInputList[0]
	print_string = "["
	for char in arrInputList:

		if char.lower() != 'g' and char.lower() != 'h' and char.lower() != 's' and char.lower() != 'r':
			continue

		if char == currentChar:
			counter += 1
		else:
			print_string += "(" + currentChar.upper() + f",{counter}), "
			counter = 1
			currentChar = char

	print_string += f"({currentChar},{counter})"
	print_string += "]"	
	print(print_string)

planHouseSeating()