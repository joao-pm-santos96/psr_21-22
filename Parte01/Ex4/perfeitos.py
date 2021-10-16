#!/usr/bin/python3

maximum_number = 100

def isPerfect(value):
    if(sum(computeDividers(value)) == value):
        return True
    return False

def computeDividers(value):
    dividers = []

    for i in range(2, maximum_number):
        if (value % i) == 0:
            dividers.append(i)

    return(dividers)

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()