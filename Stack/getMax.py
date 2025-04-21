#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    max_stack = []
    result = []

    for op in operations:
        if op.startswith('1 '):  # Push operation
            _, value = op.split()
            value = int(value)
            stack.append(value)
            if not max_stack or value >= max_stack[-1]:
                max_stack.append(value)
        elif op == '2':  # Pop operation
            popped = stack.pop()
            if popped == max_stack[-1]:
                max_stack.pop()
        elif op == '3':  # Print max
            result.append(max_stack[-1])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
