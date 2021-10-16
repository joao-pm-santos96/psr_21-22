#!/usr/bin/python3

maximum_number = 10000

def isPrime(value):
    # Based on https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/

    for i in range(2, value):
        if (value % i) == 0:
            return(False)

    return(True)


def main():
    print("Starting to compute prime numbers up {}".format(maximum_number))
    counter = 0

    for i in range(2, maximum_number):
        if isPrime(i):
            counter = counter  + 1
            print("Number {} is prime.".format(i))
        else:
            # print("Number {} is not prime.".format(i))
            pass

    print("There are {} prime numbers from 1 to {}".format(counter, maximum_number))

if __name__ == "__main__":
    main()