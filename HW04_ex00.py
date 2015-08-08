#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

################################################################################
def main():
	print("Hello World!") # Remove this and replace with your function calls
	turn=0	
	x=random.randint(1,25)
	
	try:
		while(turn<5):
			input_num=raw_input('enter a number:')
			input_num_int=int(input_num)
			if(input_num_int==x):
				print "Congratulations, you got it!"
				break
			elif (input_num_int<x):
				print "Too Low, please guess again!"
				turn=turn+1
			elif (input_num_int>x):
				print "Too High,please guess again!"
				turn=turn+1
			else:
				print 'random'
							
			if turn==5:		
				print "Sorry, you ran out of turns. Please start over to guess again!!"
	except:
		print "Only numbers please, start over buddy!"

		

if __name__ == '__main__':
    main()