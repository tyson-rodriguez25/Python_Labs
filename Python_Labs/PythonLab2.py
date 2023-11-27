import json
import string
import argparse
import sys


parser = argparse.ArgumentParser(description='Sort Strings')
parser.add_argument("--string", type=str, help="string to analyze")
word_frequency = {}
stringToSplit = sys.argv[2]
new_text = stringToSplit.translate(str.maketrans('', '', string.punctuation))
x = [word.lower() for word in new_text.split()]

for i in x:
    if i in word_frequency:
        word_frequency[i] += 1

    else:
        word_frequency[i] = 1

jsonVersion = json.dumps(word_frequency)

with open("jsonFile.json", 'w') as f:
    f.write(jsonVersion)

print(jsonVersion)



