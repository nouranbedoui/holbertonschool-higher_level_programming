#!/usr/bin/python3

for i in range(0, 9):  # First digit from 0 to 8
    for j in range(i + 1, 10):  # Second digit from i + 1 to 9
        if i == 8 and j == 9:  # If it's the last combination (89)
            print("{:01d}{:01d}".format(i, j))  # Print without trailing comma
        else:
            print("{:01d}{:01d}".format(i, j), end=", ")
