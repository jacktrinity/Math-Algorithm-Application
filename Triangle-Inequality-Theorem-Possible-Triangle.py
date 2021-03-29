"""
Triangle Inequality Theorem

Given three length, determine if it
is a possible triangle.

CodeSkulptor: https://py3.codeskulptor.org/#user306_U1W9B8gbNU_0.py
Written in Python 3
"""

import math

print("Triangle Inequality Theorem\n")
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
side_list = [float(side_a), float(side_b), float(side_c)]

max_value = max(side_list)
side_list.remove(max_value)

print("a = {}".format(side_a))
print("b = {}".format(side_b))
print("c = {}".format(side_c))

# True: Short + Short > Long
if sum(side_list) > max_value:
    print("True, a possible triangle.")
else:
    print("False, not a possible triangle.")
