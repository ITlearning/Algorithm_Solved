#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    min_num = sum(arr[:-1])
    max_num = sum(arr[1:])
    
    print(min_num, max_num)
    
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    
    miniMaxSum(arr)
