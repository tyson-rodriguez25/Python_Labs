import argparse
import numpy as np

def main(digit_array):
    index = len(digit_array) - 1

    # while the index is valid and the value at [index] ==
    # 9 set it as 0
    while index >= 0 and digit_array[index] == 9:
        digit_array[index] = 0
        index -= 1

    # if index < 0 (if all digits were 9)
    if index < 0:

        # insert an one at the beginning of the vector
        digit_array.insert(0, 1)

    # else increment the value at [index]
    else:
        digit_array[index] += 1

    print(digit_array)

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Digit Incrementer")
    parser.add_argument("--digits", nargs="+", type=int, help="Name of the file to be read in")
    args = parser.parse_args()
    main(args.digits)