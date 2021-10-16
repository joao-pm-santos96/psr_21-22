#!/usr/bin/env python

import my_functions as mf
import argparse

def main(value):   

    print("Starting to compute perfect numbers up to " + str(value))

    for i in range(0, value):
        # print("Checking " + str(i))
        if mf.isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--max_number", type=int, help="Max number")

    args = parser.parse_args()
    
    max = getattr(args, "max_number")

    main(max)