
def getSortedLowerandUppercaseLetters(lowerstr):
	lowerstr.sort()
	temp_arr = []
	for char in lowerstr:
		temp_arr.append(chr(char))
	return temp_arr

def getSortedDigits(digits):
	digits.sort()
	return digits
		

def sortAlphanumericString():
	alphanumeric_string = input('Please enter alphanumeric string:')

	arr_alphanumeric_string = list(alphanumeric_string)

	arr_uppercase = []
	arr_lowercase = []
	arr_odd = []
	arr_even = []

	for char in arr_alphanumeric_string:
		if char.isdigit() == False:
			if ord(char) >= 97:
				arr_lowercase.append(ord(char))
			else:
				arr_uppercase.append(ord(char))	
		elif char.isdigit() == True:
			if int(char) % 2 == 0:
				arr_even.append(char)
			else:
				arr_odd.append(char)


	arr_final = getSortedLowerandUppercaseLetters(arr_lowercase) + getSortedLowerandUppercaseLetters(arr_uppercase) + getSortedDigits(arr_odd) + getSortedDigits(arr_even)
	print('Sorted AlphanumericString:',''.join(map(str, arr_final)))
	

sortAlphanumericString()
