import argparse
import math

import numpy
import csv
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances


# DO NOT USE scipy.spatial.cdist
# DO NOT USE THE FUNCTION np.lingalg.norm

def main(my2DList):
    # Write the code to compute the Distance Matrix
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.

    old_array = [list(map(int, i)) for i in my2DList]
    x = np.array(old_array)

    dd = pairwise_distances(x, x, metric="euclidean")
    print(dd)

    return None


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser("Distance Matrix Calculator")
    argument_parser.add_argument("--fpath", type=str, help="Name of the .csv file to be read in")
    parsed_args = argument_parser.parse_args()
    main(list(csv.reader(open(parsed_args.fpath))))
