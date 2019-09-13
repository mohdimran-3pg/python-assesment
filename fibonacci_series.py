def getFibonacciSeries(n):  
   if n <= 1:  
       return n  
   else:  
       return(getFibonacciSeries(n-1) + getFibonacciSeries(n-2))  

numberofTerms = int(input("How many terms? "))  

if numberofTerms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(numberofTerms):  
       print(getFibonacciSeries(i))  