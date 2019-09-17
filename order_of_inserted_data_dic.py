# random sales dictionary
data_dict = {}

def startAddingDataintoDict(data_dict):
	key = "key"
	index = 1
	while True:
		input_string = (input("Enter a string: ")).lower()
		data_dict[f"key_{index}"] = input_string
		index += 1 
		action = (input("Do you want to continue (y/n): ")).lower()
		if action == "y":
			continue
		else:
			break
	print(data_dict)		

startAddingDataintoDict(data_dict)	
