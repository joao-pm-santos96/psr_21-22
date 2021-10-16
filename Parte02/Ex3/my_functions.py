#!/usr/bin/env python
# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, Setember 2020.
# --------------------------------------------------

def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    dividers = []

    for i in range(1, value):
        if (value % i) == 0:
            dividers.append(i)

    # print(dividers)
    return dividers


def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """

    if(sum(getDividers(value)) == value):
        return True
    return False