#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in s.lower(): 
            return "not pangram"
  
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
