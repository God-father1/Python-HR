#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c=zip(a,h)
    c=zip(*c)
    height=0
    for _ in word:
        b=a.index(_)
        height=h[b]
        for __ in word:
            d=a.index(__)
            if h[d]>height:
                height=h[d]
    width=len(word)
    return height*width

        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
