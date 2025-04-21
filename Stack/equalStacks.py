#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def build_heights(stack):
    heights = []
    total = 0
    for h in reversed(stack):
        total += h
        heights.append(total)
    return set(heights)

def equalStacks(h1, h2, h3):
    # Build possible heights for each stack (from top to bottom)
    s1 = build_heights(h1)
    s2 = build_heights(h2)
    s3 = build_heights(h3)

    # Find intersection of all three sets
    common = s1 & s2 & s3

    if not common:
        return 0
    return max(common)

# Input/output handling
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')
    fptr.close()
