import argparse as ap
import math


def main(array):
    mean = 0
    variance = 0
    # Write to compute the variance and the mean of a given list of numbers
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    mean = sum(array) / len(array)

    variance = sum((x-mean)**2 for x in array) / len(array)

    print("mean = " + str(mean))
    print("variance = " + str(variance))

    return


if __name__ == "__main__":
    argParse = ap.ArgumentParser("Variance and Mean Calculator")
    argParse.add_argument("--array", nargs="+", type=int,
                          help="Input a list of numbers to compute the variance and mean of")
    parsedArgs = argParse.parse_args()
    main(parsedArgs.array)
