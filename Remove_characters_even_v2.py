# Challenge: Remove Characters at Even Indices

# Write a Python program that prints the string s without the characters located at even indices.
# If the string is empty or only has one character, print it intact.

def print_even():
    s = input()
    x = ""
    for i in range(1,len(s),2):
        x += s[i]
    print(x)

print_even()

#echo "Coding" | python3 Remove_characters_even_v2.py