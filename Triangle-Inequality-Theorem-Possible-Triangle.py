"""
Triangle Inequality Theorem

Given three length, determine if it
is a possible triangle.

CodeSkulptor: https://py3.codeskulptor.org/#user306_rPVDbJwiDt45jOU_1.py
Written in Python 3
"""

import math

def triangle_inequality_thm(a, b, c):
    """
    Take three length a, b, and c.
    
    Return True if it is a possible triangle, else False.
    """
    side_lst = [float(a), float(b), float(c)]
    
    # Get the max value and compare it the sum of the two smaller value.
    max_value = max(side_lst)
    side_lst.remove(max_value)
    
    # True: Short + Short > Long
    if sum(side_lst) > max_value:
        return True
    else:
        return False

    
print("Triangle Inequality Theorem\n")
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")

print("a = {}".format(side_a))
print("b = {}".format(side_b))
print("c = {}".format(side_c))

if triangle_inequality_thm(side_a, side_b, side_c):
    print("True, a possible triangle.")
else:
    print("False, not a possible triangle.")
