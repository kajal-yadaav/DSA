#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    i=0
    j=n-1
    s1=[]
    s1=list(int(s))
    while i<=j:
        if s1[i]!=s1[j]:
            if s1[i]>s1[j]:
                s1[j]=s1[i]
            else:
                s1[i]=s1[j]
            k-=1
        i+=1
        j-=1
    if k<0:
        return "-1"
    i=0
    j=n-1
    while k>0 and i<=j:
        if s1[i]!='9':
            s1[i]=s1[j]='9'
        k-=1
        i+=1
        j-=1
    str1=""
    return str1.join(s1)

print(highestValuePalindrome(11331,5,4))
