import math
import os 
import random


def aVeryBigSum(ar):

    i = 0
    res = 0
    while (i < len(ar)):
        res = ar[i] + res
        i += 1
    return (res)

if __name__ == '__main__':
    ar = [2, 2, 4]
    print(aVeryBigSum(ar))
