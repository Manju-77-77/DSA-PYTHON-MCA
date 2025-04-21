#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    stack = []
    max_days = 0

    for pesticide in p:
        days = 0

        # Remove all elements in the stack that have higher or equal pesticide level
        while stack and pesticide <= stack[-1][0]:
            days = max(days, stack[-1][1])
            stack.pop()

        if not stack:
            days = 0  # no plant to its left with less pesticide
        else:
            days += 1  # it will die because there is a left plant with lower pesticide

        max_days = max(max_days, days)
        stack.append((pesticide, days))

    return max_days


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')
    fptr.close()
