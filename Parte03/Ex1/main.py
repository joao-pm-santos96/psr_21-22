#!/usr/bin/env python3
"""
***DESCRIPTION***
"""

"""
IMPORTS
"""
from time import time, ctime
from colorama import Fore, Back, Style
import math

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
def compute_sqrts(begin, end):
    """Computed the square root from number 'begin' to number 'end'

    Args:
        begin (int): Start number
        end (int): End number
    """    

    for i in range(int(begin), int(end)):
        math.sqrt(i)

"""
MAIN
"""
if __name__ == '__main__':

    tic = time()
    compute_sqrts(0, 50e6)
    toc = time() - tic

    print("This is {}Ex1{} and the current date is {}{}{}".format(Fore.RED, 
    Style.RESET_ALL,
    Back.YELLOW + Fore.BLUE,
    ctime(),
    Style.RESET_ALL))

    print("Elapsed time is {} seconds.".format(toc))