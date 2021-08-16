#Challenge: Reverse a String

# Write a Python Program that prints the reversed version of a string.
# The program must preserve uppercase and lowercase letters.
# If the string is empty, print it intact.

def print_reverse_string():
    string = input()[::-1]
    print(string)

print_reverse_string()

#echo "Test" | python3 Reverse_String.py