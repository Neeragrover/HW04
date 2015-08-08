#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import math
# Body
def eval_loop():
	eval_result=""
	while True:
		input=raw_input("Please enter the expression to be evaluated: ")
		if (input == "done"):
			if (eval_result == ""):
				print "No prior evaluations"
			else:
				print "The last expression evaluated to: ",eval_result
			return
		else:
			eval_result = eval(input)
			print "The expression evaluates to: ",eval_result
			print(type(eval_result))
			

################################################################################
def main():
	print "Hello"
	eval_loop()
	

if __name__ == '__main__':
    main()