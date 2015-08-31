#!/usr/bin/env python3

from itertools import *
from pprint import pprint
import sys


def lowercase_words():
    for line in sys.stdin.readlines():
        yield line.rstrip('\n').lower()

def good_words():
    def only_a_to_z(word):
        for char in word:
            if char not in "abcdefghijklmnopqrstuvwzyz":
                return False
        return True

    def is_good_word(word):
        return len(word) > 2 and \
               len(word) < 8 and \
               only_a_to_z(word)

    return (word for word in lowercase_words() if is_good_word(word))

def not_enough_words(num_words):
    sys.stderr.write("Not enough words! After filtering we " +
            "only have %d\n" % num_words)
    sys.stderr.write("We need at least 7776 for 12.9 bits of entropy per word\n")
    sys.exit(1)

def words_for_diceware():
    unique_good_words = []
    for word in good_words():
        if word not in unique_good_words:
            unique_good_words.append(word)
        if len(unique_good_words) == 7776:
            return unique_good_words
    not_enough_words(len(unique_good_words))

def number_list():
    for number_tuple in product(range(1,7), repeat=5):
        yield ''.join(str(i) for i in number_tuple)

for num, word in zip(number_list(), words_for_diceware()):
    print(num + ' ' + word)
