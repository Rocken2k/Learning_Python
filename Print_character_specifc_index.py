# Challenge: Print the Character at a Specific Index

#Write a Python program that prints the character at index i in the string s.
#If the index is out of range, the program should print "i is out of range"
#If the string is empty, the program should print "Empty String"

def print_chacracter():
    s = "Hello"
    i = 1
    
    if not s:
        print("Empty String")
    elif i > len(s):
        print("i is out of rang")
    else:
        print(s[i])

print_chacracter()

#python3 Print_character_specifc_index.py