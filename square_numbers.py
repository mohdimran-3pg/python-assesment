
def findSquare(ofElements):
	for element in ofElements:
		if type(element) == int:
			print(f'Square of {element} is: ', element*element, "\n") 
		else:
			print(f'{element} is not number\n')


findSquare([2,3,3.98,4,5,6,7,8,9, "a"])