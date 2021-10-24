#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
from collections import namedtuple

Complex = namedtuple("Complex", ['r','i'])
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
    return(Complex(x.r+y.r, x.i+y.i))

def multiplyComplex(x, y):
    # add code here ...
    return(Complex(x.r*y.r-x.i*y.i,x.r*y.i+x.i*y.r))

def printComplex(x):
    """Print complex

    Args:
        x (tuple): complex to print
    """    
    print("{}+{}i".format(x.r,x.i))

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

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