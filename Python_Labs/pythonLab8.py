import argparse
import math
import csv

import numpy as np


def cov_value(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    sub_x = [i - mean_x for i in x]
    sub_y = [i - mean_y for i in y]

    sum_value = sum([sub_y[i] * sub_x[i] for i in range(len(x))])
    denom = len(x) - 1

    cov = sum_value / denom
    return cov


def check_vectors(arr):
    length = len(arr[0])
    x = [1 for a in arr if len(a) != length]

    if (sum(x) > 0):
        raise Exception(f'length of vectors not same')


def covariance(arr):
    check_vectors(arr)
    c = [[cov_value(a, b) for a in arr] for b in arr]
    return c

def main(my2DList):
    for i in range(0, len(my2DList)):
        for j in range(0, len(my2DList[i])):
            my2DList[i][j] = float(my2DList[i][j])

    print(covariance(my2DList))
    # Write the code to compute the Covariance Matrices
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.


    return None

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser("Covariance Matrix Calculator")
    argument_parser.add_argument("--fpath", type=str, help="Name of the .csv file to be read in")
    parsed_args = argument_parser.parse_args()
    main(list(csv.reader(open(parsed_args.fpath))))