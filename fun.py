"""
Fun email-address-making utilities
"""

from random import choice


def word_lines(filename):
    """Reads a one-word-per-line file into a list of words"""
    return list(open(filename).read().splitlines())

# Read in the data. This is a little messy, but will do for this fun file
names = word_lines('words/names.txt')
adverbs = word_lines('words/adverbs.txt')
adjectives = word_lines('words/adjectives.txt')


def cool_email():
    """Combine random name, adverb and adjective into an email address.

    e.g. Malky.the.properly.scientific@example.com
    """
    return '{0}.the.{1}.{2}@example.com'.format(
        choice(names),
        choice(adverbs),
        choice(adjectives),
    )
