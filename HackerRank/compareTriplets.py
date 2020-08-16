import math
import os
import random
import re

def compareTriplets(a, b):

    i = 0
    res = [0, 0]
    while (i < 3):
        if a[i] < b[i]:
            res[1] += 1
        elif a[i] > b[i]:
            res[0] += 1
        else:
            pass
        i += 1
    return (res)

if __name__ == '__main__':
    a = [17, 28, 30]
    b = [99, 16, 8]
    result = compareTriplets(a , b)
    print(result)







