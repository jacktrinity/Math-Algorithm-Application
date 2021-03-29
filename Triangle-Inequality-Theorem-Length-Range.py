"""
Triangle Inequality Theorem

Given two side of a triangle, find the range of possible
length of the missing side.

CodeSkulptor: https://py3.codeskulptor.org/#user306_U1W9B8gbNU_0.py
Written in Python 3
"""

import math

print("Triangle Inequality Theorem\n")
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")

# Upper bound: a + b > c
upper_c = float(side_a) + float(side_b)

# Lower bound: c > b - a or c > a - b
# Take the upper bound of the lower limit
lower_c1 = float(side_a) - float(side_b)
lower_c2 = float(side_b) - float(side_a)
lower_c = max(lower_c1, lower_c2)

print("a = {}".format(side_a))
print("b = {}".format(side_b))
print("{lower} < c < {upper}".format(lower=str(lower_c), upper=str(upper_c)))
