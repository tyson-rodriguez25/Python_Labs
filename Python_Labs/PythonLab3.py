import sys
import numpy
import math
import argparse
import os

parser = argparse.ArgumentParser(description='Cubes and Integer but only keeps evens')
parser.add_argument('--n', type=int, help="int to cube")
cubedNumber = 0
numberToCube = int(sys.argv[2])
total = 0
for i in range(1, numberToCube+1):
    n = math.pow(i, 3)
    originN = math.pow(i,3)
    if originN < 10 and originN % 2 == 0:
        cubedNumber += originN
    while n > 10:
        n = n//10
        if n % 2 == 0 and n < 10:
            cubedNumber += originN
        else:
            pass

print(cubedNumber)





