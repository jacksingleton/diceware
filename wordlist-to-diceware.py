#!/usr/bin/env python3

from itertools import *
from pprint import pprint
import sys

def lowercase_words(fp):
    for line in fp.readlines():
        yield line.rstrip('\n').lower()

def words_from_file(filename):
    with open(filename) as fp:
        return list(lowercase_words(fp))

def good_words():
    def only_a_to_z(word):
        for char in word:
            if char not in 'abcdefghijklmnopqrstuvwzyz':
                return False
        return True

    profanity = words_from_file('profanity.list')
    def profane(word):
        return word in profanity

    def good_size(word):
        return len(word) > 2 and len(word) < 8

    def is_good_word(word):
        return good_size(word) and \
               only_a_to_z(word) and \
               not profane(word)

    return (word for word in lowercase_words(sys.stdin)
            if is_good_word(word))

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
