#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
			return 'False'

def any_lowercase3(s):
	"""Explain what is wrong, if anything, here.
	"""
	for c in s:
		flag = c.islower()
	return flag

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
	return flag

def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():
            return False
    return True

def any_lowercase6(s):
	for c in s:
		if c.islower():
			return True
	return False

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
	#print("Hello World!")
	#print any_lowercase1("Neera")
	"""The Flaw with this function is that it returns True/False without iterating 
	through the entire string. So, if the first letter of the string happens to be 
	an upper case letter, it will go to the else part and return false although the
	following letters might be lowercase"""
	#print any_lowercase2("NEERA")
	"""The Flaw with this function is the quotes around 'c' which makes it the
	character c rather than an iterator of the for loop to iterate through the 
	string"""
	#print any_lowercase3("NEeRA")
	"""The Flaw with this function is that the value of flag being returned has
	lower case check result for the last letter(from the last iteration). So, if 
	there were lowercase letters at positions other than the last one, it would 
	get overwritten with each iteration of the for loop and not show the correct response."""
	#print any_lowercase4("NEeRA")
	"""The Flaw with this function is also that the value of the flag being returned is 
	the indicative of the lower case check on the last letter. So, if there
	were lowercase letters at positions other than the last one, it would 
	get overwritten with each iteration of the for loop and not show the correct response."""
	#print any_lowercase5("neera")
	"""The Flaw with this function is that if it encounters an upper case character, it 
	evaluates False and returns while there could be lowercase letters later in the string.
	It will return true only if all the letters in the string are lowercase."""
	#print any_lowercase6("NEErA")
	""""This function would return the required result"""
	
if __name__ == '__main__':
    main()