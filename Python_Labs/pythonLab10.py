import argparse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from scipy.sparse import csr_matrix


def main(documentsTxt):
    # Write the code to compute the One Hot Encodings for various "documents"
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    #mystr = documentsTxt.splitlines()
    #input = mystr
    #vectorizer = CountVectorizer()
    #X = vectorizer.fit_transform(input)
    #vectorizer.get_feature_names_out()
    #print(X.toarray())


    mystr = documentsTxt.splitlines()
    unique_words = set()

    for each_sentence in mystr:
        for each_word in each_sentence.split(' '):
            if len(each_word) > 0:
                unique_words.add(each_word.lower())

    sorted_list = sorted(unique_words)

    vocab = {}
    for index, word in enumerate(sorted_list):
        vocab[word] = index

    row, col, val = [],[],[]

    for idx, sentence in enumerate(mystr):
        count_word = dict(Counter(sentence.split(' ')))

        for word, count in count_word.items():
            col_index = vocab.get(word.lower())
            if col_index >= 0:
                row.append(idx)
                col.append(col_index)
                val.append(count)
    finished_array = (csr_matrix((val, (row, col)), shape=(len(mystr), len(vocab)))).toarray()
    print("Features: \n", finished_array)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())