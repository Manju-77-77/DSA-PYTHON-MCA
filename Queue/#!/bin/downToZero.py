#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque  # Required for queue

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    visited = [False] * (n + 1)
    queue = deque()
    
    queue.append((n, 0))  # (current number, steps taken)
    visited[n] = True
    
    while queue:
        current, steps = queue.popleft()
        
        if current == 0:
            return steps
        
        # Operation 2: Decrement by 1
        if not visited[current - 1]:
            visited[current - 1] = True
            queue.append((current - 1, steps + 1))
        
        # Operation 1: Replace with a factor < current
        for i in range(2, int(current**0.5) + 1):
            if current % i == 0:
                j = current // i
                if not visited[j]:
                    visited[j] = True
                    queue.append((j, steps + 1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
