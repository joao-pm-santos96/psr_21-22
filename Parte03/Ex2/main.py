#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""

"""
METADATA
"""
__author__ = 'Joao Santos'
__copyright__ = 'Copyright October2021'
__credits__ = ['Joao Santos']
__version__ = '1.0.0'
__maintainer__ = 'Joao Santos'
__email__ = 'joao.pm.santos96@gmail.com'
__status__ = 'Production'
# __license__ = 'GPL'

"""
TODO
"""

"""
CLASS DEFINITIONS
"""

"""
FUNCTIONS DEFINITIONS
"""
def addComplex(x, y):
    """Add complex number

    Args:
        x (tuple): complex A
        y (tuple): complex B
    """    
    return((x[0]+y[0], x[1]+y[1]))

def multiplyComplex(x, y):
    # add code here ...
    return((x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]))

def printComplex(x):
    """Print complex

    Args:
        x (tuple): complex to print
    """    
    print("{}+{}i".format(x[0],x[1]))

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

"""
MAIN
"""
if __name__ == '__main__':
    main()