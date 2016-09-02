from sys import argv, exit
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
	"""if user_input_is_valid(key) == False:
			print("That is not a valid rotation")
			exit"""

	rotate = int(key)
	txtblk = list(text)
	newtxt = []
	for achar in txtblk:
		newchr = rotate_character(achar, rotate)
		newtxt.append(newchr)
	paste = ""
	encryption = paste.join(newtxt)
	return(encryption)
	
def user_input_is_valid(cl_args):
    #argstr = str(cl_args)
    if len(cl_args) < 2:
        return False
    if cl_args[1].isdigit():
        return True
    else:
        return False
		
#print(encrypt(input("Write a message:\n"), (input("Rotate by:\n"))))
#print(encrypt(input("Write a message:\n"), int(argv[1])))
#print(encrypt(input("Write a message:\n"),))

