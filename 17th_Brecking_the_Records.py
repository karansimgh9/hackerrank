#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
  minc=0
  maxc=0
  minl=scores[0]
  maxl=scores[0]
  for i in range(len(scores)):
    if minl > scores[i]:
      minc+=1
      minl=scores[i]
    if maxl< scores[i]:
      maxc +=1
      maxl=scores[i]
  return maxc,minc

      


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()