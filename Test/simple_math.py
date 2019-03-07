# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:16:22 2019
@author: soohl254
A collection of simple math operations.  
"""


def simple_add(a,b):
    """
    Simple addition of a and b.  

    Parameters
    ----------
    a : object supporting addition
    b : object supporting addition

    Examples
    --------
    c=simple_add(a,b)
    """
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
