#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX(a, b):
  a_factor=[]
  b_factor=[]
  coman_num=[]
  max_length=(a+b)
  for i in range(1, 101):
    for number in a:
      if i % number==0:
        a_factor.append(i)
  for i in range(1, 101):
    for number in b:
      if number%i==0:
        print(b_factor.append(i))
  tem_list= a_factor +b_factor
  for number in tem_list:
    if tem_list.count(number) == max_length:
      coman_num.append(number)
  return len(set(coman_num))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
