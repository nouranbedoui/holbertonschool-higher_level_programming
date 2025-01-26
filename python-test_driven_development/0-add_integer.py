#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers (or floats), casting them to integers."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    # Cast to integers if a or b are floats
    a = int(a)
    b = int(b)

    return a + b
