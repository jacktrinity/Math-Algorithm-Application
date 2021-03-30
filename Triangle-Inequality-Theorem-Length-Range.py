"""
Triangle Inequality Theorem

Given two side of a triangle, find the range of possible
length of the missing side.

CodeSkulptor: https://py3.codeskulptor.org/#user306_U1W9B8gbNU_1.py
Written in Python 3
"""

import math

def triangle_inequality_thm(a, b):
    """
    Take two side of a triangle a and b.
    
    Return two number: lower and upper bound of the missing range length.
    """
    a = float(a)
    b = float(b)
    
    # Upper bound: a + b > c
    upper_c = a + b
    
    # Lower bound: c > b - a or c > a - b
    # Take the upper bound of the lower limit
    lower_c1 = a - b
    lower_c2 = b - a
    lower_c = max(lower_c1, lower_c2)
    
    return lower_c, upper_c


print("Triangle Inequality Theorem\n")
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")

min_c, max_c = triangle_inequality_thm(side_a, side_b)

print("a = {}".format(side_a))
print("b = {}".format(side_b))
print("{lower} < c < {upper}".format(lower=str(min_c), upper=str(max_c)))
