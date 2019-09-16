import random

class GuessNotCorrectException(Exception):
  """Raised: when Your Guess was not correct"""
  pass

class TotalNumberOfAttemptException(Exception):
  """Raised: when Your Total Attempt Exceeds"""
  pass

def displayAnagramOf(correct_word):
  hidden_letters = ['_'] * len(correct_word)
  random_hint_index = random.choice(range(len(correct_word)))
  hidden_letters[random_hint_index] = correct_word[random_hint_index]
  print(f"{' '.join(hidden_letters)}")

def starttoGuessAnagram():
  index = 0
  numer_of_attempts = 0
  max_attempt = 5
  while True:
     try:
         input_string = (input("Enter a string: ")).lower()
         numer_of_attempts = numer_of_attempts + 1 
         if numer_of_attempts >= max_attempt:
             raise TotalNumberOfAttemptException 
         elif input_string != correct_word:
             raise GuessNotCorrectException
         break    
     except GuessNotCorrectException:
         print(f"Sorry! Your guess was not correct            Attempt(s) = {numer_of_attempts}")
         print()
         displayAnagramOf(correct_word)
     except TotalNumberOfAttemptException:
         if input_string != correct_word:
            print(f"Sorry! Your guess was not correct            Attempt(s) = {numer_of_attempts}.\n")
         else:
            print(f"Congratulations! Your guess was correct            Attempt(s) = {numer_of_attempts}.\n")    
         print()
         exit()    
  print("Congratulations! Your guess was correct.")  

  

correct_word = "zebra"
displayAnagramOf(correct_word)
starttoGuessAnagram()

      
