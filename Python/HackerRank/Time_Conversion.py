#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    meridiem = s[-2:]
    time = s[:2]
    if meridiem == "AM":
        if time == "12":
            return "".join("00"+s[2:-2])
        return "".join(s[:-2])
    else:
        if int(time) < 12:
            replace = int(time) + 12
        else:
            replace = time
        return "".join(str(replace)+s[2:-2])
    return "".join(s[2:-2])
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
