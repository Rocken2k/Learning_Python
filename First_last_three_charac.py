# Challenge: First and Last Three Characters of a String

# Write a Python program that prints the first and last three characters of the string s as a single string.
# If the string has less than six characters, print an empty string (blank output).

def first_last_three_character():
    string = input()
    if len(string) > 6:
        first_three = string[:3]
        last_three = string[-3:]
        print(first_three +  last_three)
    else:
        print("")

first_last_three_character()

#echo "Wonderful" | python3 First_last_three_charac.py