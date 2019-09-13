def isPrime(number):
	counter = 2
	result = True
	if number <= 1:
	   result = False

	while counter < number:
		if number % counter == 0:
			result = False
			break


		counter += 1

	return result		
			  
primeNumber = 20
index = 1
primeNumberSum = 0
while index < primeNumber:

	if isPrime(index):
		primeNumberSum += index
		print("Prime Number:", index)

	index += 1	


print("isPrime---",isPrime(2), "Sum:", primeNumberSum)