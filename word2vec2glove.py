# coding=utf-8

"""
Convert Word2Vec model to GloVe format (text format)
"""

import argparse
import os

from gensim.models import KeyedVectors

__author__ = 'Masaya Suzuki'
__version__ = '1.0'


def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-w', '--word2vec', type=str, required=True, help='Word2Vec model')
    args = parser.parse_args()

    tmp_file_name = '.tmp.txt'
    word2vec_model_file_name = args.word2vec

    for _ in range(2):
        try:
            with open(word2vec_model_file_name) as word2vec_model_file:
                i = 0
                for r in word2vec_model_file:
                    if 0 < i:
                        print(r.strip())

                    i += 1

            break
        except UnicodeDecodeError:
            word2vec_model_file_name = tmp_file_name
            KeyedVectors.load_word2vec_format(args.word2vec, binary=True).save_word2vec_format(word2vec_model_file_name)

    if os.path.exists(tmp_file_name):
        os.remove(tmp_file_name)


if __name__ == '__main__':
    main()
