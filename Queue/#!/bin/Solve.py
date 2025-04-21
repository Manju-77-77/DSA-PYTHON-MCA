#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    n = len(arr)
    
    def get_min_of_max_for_window_size(k):
        """Returns the minimum among the maximums of all subarrays of size k."""
        dq = deque()
        max_in_windows = []

        for i in range(n):
            # Remove elements smaller than current
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            
            # Remove out-of-window indices
            if dq[0] <= i - k:
                dq.popleft()
            
            if i >= k - 1:
                max_in_windows.append(arr[dq[0]])

        return min(max_in_windows)

    res = []
    for k in queries:
        res.append(get_min_of_max_for_window_size(k))

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
