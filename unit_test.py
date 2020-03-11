import unittest
from credit_card_validator import creditCardValidator

def testAddNumbers(a, b):
	return (a + b)


class TestStringMethods(unittest.TestCase):

    def test_16Digit(self):
    	objCCValidator = creditCardValidator()
    	self.assertEqual(objCCValidator.is16Length("4114-4247-8901-0985"), True)
    	self.assertEqual(objCCValidator.is16Length("4114-4247-8901-098"), False)
    	self.assertEqual(objCCValidator.is16Length("4114-4247-8901-09908"), False)

    def test_DigitandStartValidation(self):
    	objCCValidator = creditCardValidator()
    	self.assertTrue(objCCValidator.checkCreditCardStartandDigitValidation("6114-4247-8901-0985"))
    	self.assertTrue(objCCValidator.checkCreditCardStartandDigitValidation("5114-4247-8901-0985"))
    	self.assertTrue(objCCValidator.checkCreditCardStartandDigitValidation("4114-4247-8901-0985"))
    	self.assertFalse(objCCValidator.checkCreditCardStartandDigitValidation("411a-4247-8901-0985"))
    	self.assertFalse(objCCValidator.checkCreditCardStartandDigitValidation("211a-4247-8901-0985"))
    
    def test_DuplicateDigitPattern(self):
    	objCCValidator = creditCardValidator()
    	self.assertTrue(objCCValidator.checkDuplicateDigits("6114-4247-8901-0985"))
    	self.assertFalse(objCCValidator.checkDuplicateDigits("1111-4247-8901-0985"))
    	self.assertFalse(objCCValidator.checkDuplicateDigits("4111-1247-8901-0985"))
    	self.assertFalse(objCCValidator.checkDuplicateDigits("4111-3277-7701-0985"))
    	self.assertFalse(objCCValidator.checkDuplicateDigits("4111-3276-7201-1111"))
    		
    def test_addnumbers(self):
        s = 1
        t = 2
        self.assertEqual((2+1), 3)
  
print(testAddNumbers(1,2))

#assertEqual(3,3)

if __name__ == '__main__':
    unittest.main()





