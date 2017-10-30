#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#


def triangle(a, b, c):
    if a <=0 or b <= 0 or c <= 0:
        raise TriangleError(f"Non-positive value passed for sides:{a},{b},{c}")

    sum1 = a + b
    sum2 = a + c
    sum3 = b + c

    if sum1 <= c or sum2 <= b or sum3 <= a:
        raise TriangleError("Sum of any two sides must be greater than third one.")

    if a == b == c:
        return 'equilateral'

    if a == b or b == c or a == c:
        return 'isosceles'

    return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
   pass 
