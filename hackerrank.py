#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    i=0
    l=[]
    while i<=len(n):
        j=i+1
        while j<=len(n):
            l.append(int(n[i:j]))
            j+=1
        i+=1
    return sum(l)
    
print(substrings("972698438521"))
