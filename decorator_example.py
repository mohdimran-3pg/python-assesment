import time
import requests
import json

def time_calculator(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__+f" took {(end-start)*1000} miliseconds")
		return result 
	return wrapper	


@time_calculator
def printNumbers(totalNumbers):
	
	counter = 1
	sumOfNumbers = 0
	while counter < totalNumbers:
		sumOfNumbers += counter
		counter += 1

	print(sumOfNumbers)	
	return sumOfNumbers		


@time_calculator
def get_yahoo_page():
	data = requests.get("https://in.yahoo.com/?p=us")
	
printNumbers(1000)
get_yahoo_page()

