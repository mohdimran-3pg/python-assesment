class SmallStringException(Exception):
   """Raised when the input string is small"""
   pass
class LargeStringException(Exception):
   """Raised when the input string is large"""
   pass
class NotSameStringException(Exception):
   """Raised when the input string is not same to predefined string"""
   pass   

answerString = "imran"
while True:
   try:
       input_string = (input("Enter a string: ")).lower()
       if len(input_string) < len(answerString):
           raise SmallStringException
       elif len(input_string) > len(answerString):
           raise LargeStringException
       elif input_string != answerString:
           raise NotSameStringException 

       break
   except SmallStringException:
       print("This string is too small, try again!")
       print()
   except LargeStringException:
       print("This string is too large, try again!")
       print()
   except NotSameStringException:
       print("This string is not to predefined string , try again!")
       print()    
print("Congratulations! You guessed it correctly.")