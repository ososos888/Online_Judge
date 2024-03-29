#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
#단어의 길이 * 가장 큰 단어를 return
#알파벳을 ASCII로 치환 후 h list에 match
    d = []
    for i in range(0,len(word)):
        d.append(h[ord(word[i])-97])
    return (max(d)*len(word))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
