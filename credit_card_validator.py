
import re

def is16Length(creditcardnumber):
	if len(creditcardnumber.replace("-", "")) > 16:
		return False
	else:
		return True

def checkCreditCardStartandDigitValidation(creditcardnumber):

	regex = r"^[4-6][0-9-]*$"

	matches = re.search(regex, creditcardnumber)

	if matches:
		return True
	else:
		return False

def checkDuplicateDigits(creditcardnumber):

	arrCreditCardNumber = list(creditcardnumber.replace("-",""))
	counter = 0
	occurance = 0
	last_char = arrCreditCardNumber[0]
	while counter < len(arrCreditCardNumber):

		if last_char == arrCreditCardNumber[counter]:
			occurance += 1
		else:
			occurance = 1	

		if occurance == 4:
			occurance = 1
			return False	

		if arrCreditCardNumber[counter] == "-":
			if (counter != 4 and counter != 9 and counter != 14):
				return False

		last_char = arrCreditCardNumber[counter]		
		counter += 1		

def isValidCreditCard(credit_card):

	if is16Length(credit_card) == False:
		print("Invalid Credit Card 1")
	elif checkCreditCardStartandDigitValidation(credit_card) == False:
		print("Invalid Credit Card 2")
	elif checkDuplicateDigits(credit_card) == False:
		print("Invalid Credit Card 3")
	else:
		print("valid credit card")
	
isValidCreditCard("5114-4447-8901-0985")
