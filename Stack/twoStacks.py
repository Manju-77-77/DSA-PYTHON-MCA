#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    sum = 0
    count = 0
    max_count = 0

    # First, remove from b as much as possible
    j = 0
    while j < len(b) and sum + b[j] <= maxSum:
        sum += b[j]
        j += 1
    max_count = j

    # Now try to include from a, and adjust b if necessary
    i = 0
    while i < len(a):
        sum += a[i]
        i += 1
        while sum > maxSum and j > 0:
            j -= 1
            sum -= b[j]
        if sum <= maxSum:
            max_count = max(max_count, i + j)
        else:
            break

    return max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
