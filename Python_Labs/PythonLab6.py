import argparse


def main(number: int):
    if str(number) == str(number)[::-1]:
        print("True")

    else:
        print("False")

    return None


if __name__ == "__main__":
    arg = argparse.ArgumentParser("Pallindrome Checker")
    arg.add_argument("--x", type=int, help="Input a number to determine if it's a pallindrome")
    parsed = arg.parse_args()
    main(parsed.x)
