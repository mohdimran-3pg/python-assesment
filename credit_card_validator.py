
import re

class creditCardValidator:


	def is16Length(self, creditcardnumber):
		if len(creditcardnumber.replace("-", "")) == 16:
			return True
		else:
			return False

	def checkCreditCardStartandDigitValidation(self, creditcardnumber):

		regex = r"^[4-6][0-9-]*$"

		matches = re.search(regex, creditcardnumber)

		if matches:
			return True
		else:
			return False

	def checkDuplicateDigits(self, creditcardnumber):

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
		return True			

	def isValidCreditCard(self, credit_card):

		if self.is16Length(credit_card) == False:
			return f"{credit_card} is Invalid Credit Card"
		elif self.checkCreditCardStartandDigitValidation(credit_card) == False:
			return f"{credit_card} is Invalid Credit Card"
		elif self.checkDuplicateDigits(credit_card) == False:
			return f"{credit_card} is Invalid Credit Card"
		else:
			return f"{credit_card} is Valid Credit Card"


objCCValidator = creditCardValidator()
credit_card = "4114-4247-8901-0985"	
print(objCCValidator.isValidCreditCard(credit_card))