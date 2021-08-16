# Challenge: Print the Character at a Specific Index

# Write a Python program that prints the character at index i in the string s.
# If the index is out of range, the program should print "i is out of range"
# If the INDEX is empty, the program should print "Empty INDEX"


def print_chacracter():
    vals = input().split()
    s = vals[0]
    
    try:
        if int(vals[1]) >= len(s):
            print("i is out of range")
        else:
            print(s[int(vals[1])])
    except IndexError:
        print("Empty INDEX")
    
print_chacracter()

#echo "test 1 " | python3 Print_character_specifc_index.py