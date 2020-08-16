import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    
    res = [0, 0]
    i = 0
    j = 0
    len_arr = len(arr)
    while (i < len_arr):
        while (j < len_arr):
            res[0] = res[0] + arr[i][j]
            res[1] = res[1] + arr[i][len_arr - 1 - j]
            i += 1
            j += 1
    return (abs(res[0] - res[1]))

if __name__ == '__main__':
    arr = [[11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]]

    print(diagonalDifference(arr))
