#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    minus = 0
    plus = 0
    zero = 0
    for i in arr:
        if i < 0:
            minus += 1
        elif i == 0:
            zero += 1
        else:
            plus += 1
            
    print("{:.6f}".format(plus/len(arr)))
    print("{:.6f}".format(minus/len(arr)))
    print("{:.6f}".format(zero/len(arr)))
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
