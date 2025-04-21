#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andXorOr' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def andXorOr(a):
    max_val = 0
    stack = []

    for num in a:
        # Maintain decreasing stack
        while stack:
            top = stack[-1]
            max_val = max(max_val, num ^ top)
            if top > num:
                stack.pop()
            else:
                break
        stack.append(num)
    
    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')
    fptr.close()
