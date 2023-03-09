

"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Function to get the sum of two input values.

    Parameters
    ----------
    a: integer or float
    b: integer or float

    Returns
    --------
    a + b: integer or float depending on the input parameters

    See also
    --------
    simple_sub
    simple_mult
    simple_div
    poly_first
    poly_second

    Examples
    --------
    >>> simple_match.simple_add(2,3)
    5
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

