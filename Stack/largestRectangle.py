#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack = []
    max_area = 0
    index = 0
    n = len(h)
    
    while index < n:
        # Push the current bar to stack if it is higher than the bar at stack top
        if not stack or h[index] >= h[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Calculate area with the top of stack as the smallest bar
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = h[top] * width
            max_area = max(max_area, area)
    
    # Now pop the remaining bars from stack and calculate area
    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        area = h[top] * width
        max_area = max(max_area, area)
    
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')
    fptr.close()
