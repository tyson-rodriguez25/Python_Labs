import argparse
import math

import numpy as np


# DO NOT USE np.histogram

def main(arrayOfNumbers, numOfBins):
    numBins = numOfBins
    minofArray = min(arrayOfNumbers)
    maxofArray = max(arrayOfNumbers)

    intervalSize = (maxofArray - minofArray) / numBins
    outputList = []
    intervalMin = minofArray
    intervalMax = intervalMin + intervalSize

    for i in range(1, numBins + 1):
        lastBin = False
        if i == numBins:
            lastBin = True
        numMatches = 0
        for num in arrayOfNumbers:
            if num >= intervalMin and num < intervalMax:
                numMatches += 1
            elif num >= intervalMin and num <= intervalMax and lastBin:
                numMatches += 1
        outputList.append(numMatches)
        stuff_in_string = f"[{math.ceil(intervalMin * 10)/10}, {math.ceil(intervalMax * 10) /10}): {outputList[-1]} "
        intervalMin = intervalMax
        intervalMax += intervalSize

        print(stuff_in_string)

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Histogram Generator")
    parser.add_argument("--a", nargs="+", type=int, help="Input a list of numbers to generate a histogram with")
    parser.add_argument("--b", type=int, help="Input the number of bins to use")

    parsed_args = parser.parse_args()
    main(parsed_args.a, parsed_args.b)
