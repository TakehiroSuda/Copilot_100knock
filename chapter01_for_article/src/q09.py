
import random
"""
This module provides functions to shuffle the middle characters of words in a sentence.

Functions:
    shuffle_middle(word: str) -> str:
        Shuffles the middle characters of a word, leaving the first and last characters in place.
        If the word length is 4 or less, it returns the word unchanged.

    shuffle_sentence(sentence: str) -> str:
        Shuffles the middle characters of each word in a sentence.
        Words are split by spaces and rejoined after shuffling.
"""

def shuffle_middle(word):
    if len(word) <= 4:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]

def shuffle_sentence(sentence):
    words = sentence.split()
    shuffled_words = [shuffle_middle(word) for word in words]
    return ' '.join(shuffled_words)

