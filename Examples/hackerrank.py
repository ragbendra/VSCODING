#!/bin/python3

import math
import os
import random
import re
import sys

from main import frpt

#
# Complete the 'ashtonString' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def ashtonString(s, k):
    # Write your code here

    if __name__ == '__main__':
        fib = open(os.environ['OUTPUT_PATH'], 'w')

        t = int(input().strip())

        for t_itr in range(t):
            s = input()

            k = int(input().strip())

            res = ashtonString(s, k)

            fib.write(str(res) + '\n')

        fib.close()
