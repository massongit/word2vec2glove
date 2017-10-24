# coding=utf-8

"""
Convert Word2Vec model from binary format to text format
"""

import argparse

from gensim.models import KeyedVectors

__author__ = 'Masaya Suzuki'
__version__ = '1.0'


def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b', '--binary', type=str, required=True, help='binary format word2vec model (input)')
    parser.add_argument('-t', '--text', type=str, required=True, help='text format word2vec model (output)')
    args = parser.parse_args()

    KeyedVectors.load_word2vec_format(args.binary, binary=True).save_word2vec_format(args.text)


if __name__ == '__main__':
    main()
