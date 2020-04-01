#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    counter=0
    for _ in range(i,j+1):
        n=str(_)
        m=int(n[::-1])
        c=abs(_-m)
        if(c%k==0):
            counter+=1
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
