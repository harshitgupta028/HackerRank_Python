#!/bin/python3

import math
import os
import random
import re
import sys
lst=list()
lst1=list()
def solve(s):
    lst=s.split(" ")

    for i in lst:
        lst1.append(i.capitalize())
    
    return(" ".join(lst1))    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
