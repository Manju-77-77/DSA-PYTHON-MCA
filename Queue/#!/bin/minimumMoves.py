#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    queue = deque()
    
    # Each element in queue: (x, y, move_count)
    queue.append((startX, startY, 0))
    visited[startX][startY] = True

    # 4 directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, moves = queue.popleft()

        if x == goalX and y == goalY:
            return moves

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Keep going in the current direction until blocked or edge
            while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, moves + 1))
                nx += dx
                ny += dy

    return -1  # In case no path is found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
