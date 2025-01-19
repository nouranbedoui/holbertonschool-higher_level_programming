#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert to uppercase by adjusting ASCII value
            print(chr(ord(char) - 32), end="")
        else:
            # Print the character as is (for non-lowercase characters)
            print(char, end="")
    print()  # Print the newline at the end
