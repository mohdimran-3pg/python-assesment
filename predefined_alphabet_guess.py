class SmallStringException(Exception):
   """Raised when the input string is small"""
   pass
class LargeStringException(Exception):
   """Raised when the input string is large"""
   pass
class NotSameStringException(Exception):
   """Raised when the input string is not same to predefined string"""
   pass

def startPredefinedAlphabetGuessProcess(alphabet):
  while True:
     try:
         input_string = (input("Enter a alphabet: ")).lower()
         if len(input_string) < len(alphabet):
             raise SmallStringException
         elif len(input_string) > len(alphabet):
             raise LargeStringException
         elif input_string != alphabet:
             raise NotSameStringException 

         break
     except SmallStringException:
         print("This alphabet is too small, try again!")
         print()
     except LargeStringException:
         print("This alphabet is too large, try again!")
         print()
     except NotSameStringException:
         print("This alphabet is not to predefined alphabet , try again!")
         print()    
  print("Congratulations! You guessed it correctly.")      


answerString = "imran"
startPredefinedAlphabetGuessProcess(answerString)
