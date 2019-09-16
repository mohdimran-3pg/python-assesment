def startBracketsComparison(brackets):
	brackets_list = list(brackets)

	open_round_brackets = 0
	open_square_brackets = 0
	open_curly_brackets = 0
	open_angle_brackets = 0

	close_round_brackets = 0
	close_square_brackets = 0
	close_curly_brackets = 0
	close_angle_brackets = 0

	for bracket in brackets_list:
		if bracket == "{":
			open_curly_brackets +=1
		elif bracket == "(":
			open_round_brackets +=1
		elif bracket == "[":
			open_square_brackets +=1
		elif bracket == "<":
			open_angle_brackets +=1
		elif bracket == "}":
			close_curly_brackets += 1
		elif bracket == ")":
			close_round_brackets += 1
		elif bracket == "]":
			close_square_brackets += 1
		elif bracket == ">":
			close_angle_brackets += 1

	is_matched = True
	if 	open_round_brackets != close_round_brackets:
		print(f"Rounded Brackets miss match   Open:{open_round_brackets}  Close:{close_round_brackets} \n")
		is_matched = False
	if open_square_brackets !=  close_square_brackets:
		print(f"Square Brackets miss match Open:{open_square_brackets}  Close:{close_square_brackets} \n")
		is_matched = False
	if open_curly_brackets != close_curly_brackets:
		print(f"Curly Brackets miss match Open:{open_curly_brackets}  Close:{close_curly_brackets} \n")
		is_matched = False
	if open_angle_brackets != close_angle_brackets:
		print(f"Angle Brackets miss match Open:{open_angle_brackets}  Close:{close_angle_brackets} \n")
		is_matched = False


	if is_matched == True:
		print("Congratulations Brackets matched")


brackets = "{}(>[][])"
startBracketsComparison(brackets)		



