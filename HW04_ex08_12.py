# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function


def encrypt_by_rot(string, num):
	new_string = ""
	base_seq_lower = "abcdefghijklmnopqrstuvwxyz"
	base_seq_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for char in string:
		if char.islower():
			base_seq = base_seq_lower
		else:
			base_seq = base_seq_upper
		position_in_seq = base_seq.find(char)
		new_position = position_in_seq + num
		if (new_position >=25):	
			new_position -= 26
		char = base_seq[new_position]
		new_string = new_string + char
	return new_string

def main():
	print "hello"
	print encrypt_by_rot("cheer",7)
	print encrypt_by_rot("melon",-10)
	print encrypt_by_rot("abxyz",1)
	print encrypt_by_rot("AbcXYZ",1)
	#print ord('[')
	
if __name__ == '__main__':
    main()
	
	