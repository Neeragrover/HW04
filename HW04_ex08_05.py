#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body
def count(string,letter):
	ctr=0
	for char in string:
		if char == letter:
			ctr=ctr+1
	print letter,"appears in",string,ctr,"times"

################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
	string=raw_input("Input a string: ")
	letter=raw_input("Input the letter: ")
	count(string,letter)
   

if __name__ == '__main__':
    main()