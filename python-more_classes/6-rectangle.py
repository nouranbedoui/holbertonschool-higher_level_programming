#!/usr/bin/python3
"""
This module defines a Rectangle class with instance counting.
"""


class Rectangle:
    """
    A class that defines a rectangle with instance counting.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string of a rectangle using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([
            "#" * self.__width for _ in range(self.__height)
        ])

    def __repr__(self):
        """Returns a string of a rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Returns a string of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
