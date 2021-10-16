#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 100

def isPrime(value):
    # Based on https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/

    for i in range(2, value):
        if (value % i) == 0:
            return(False)

    return(True)

def computeDividers(value):
    dividers = []

    for i in range(2, maximum_number):
        if (value % i) == 0:
            dividers.append(i)

    return(dividers)

def main():
    print("Starting to compute prime numbers up {}".format(maximum_number))
    counter = 0

    for i in range(2, maximum_number):
        if isPrime(i):
            counter = counter  + 1
            print(Fore.GREEN + "Number {} is prime.".format(i) + Style.RESET_ALL)
        else:
            print("Dividers: {}".format(computeDividers(i)))

    print("There are {} prime numbers from 1 to {}".format(counter, maximum_number))

if __name__ == "__main__":
    main()