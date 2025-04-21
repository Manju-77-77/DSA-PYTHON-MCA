#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    total_fuel = 0
    current_fuel = 0
    start_index = 0

    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        fuel_diff = petrol - distance

        total_fuel += fuel_diff
        current_fuel += fuel_diff

        # If current fuel is less than 0, cannot start from this point
        if current_fuel < 0:
            start_index = i + 1
            current_fuel = 0

    return start_index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')
    fptr.close()
