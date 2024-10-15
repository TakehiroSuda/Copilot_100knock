import sys
sys.path.append('..')
from q05 import generate_n_grams
"""
This module provides functions to create and manipulate bigram sets from strings.

Functions:
    create_bigram_set(s: str) -> set:
        Generates a set of bigrams from the input string `s`.

    union_bigrams(set1: set, set2: set) -> set:
        Returns the union of two bigram sets `set1` and `set2`.

    intersection_bigrams(set1: set, set2: set) -> set:
        Returns the intersection of two bigram sets `set1` and `set2`.

    difference_bigrams(set1: set, set2: set) -> set:
        Returns the difference of two bigram sets `set1` and `set2`.

    contains_bigram(bigram_set: set, bigram: str) -> bool:
        Checks if a bigram `bigram` is present in the bigram set `bigram_set`.

Usage example:


        print("Union:", union_bigrams(X, Y))
        print("Intersection:", intersection_bigrams(X, Y))
        print("Difference:", difference_bigrams(X, Y))
        print("Contains 'se' in X:", contains_bigram(X, 'se'))
        print("Contains 'se' in Y:", contains_bigram(Y, 'se'))
"""

def create_bigram_set(s):
    return set(generate_n_grams(s, 2))

def union_bigrams(set1, set2):
    return set1.union(set2)

def intersection_bigrams(set1, set2):
    return set1.intersection(set2)

def difference_bigrams(set1, set2):
    return set1.difference(set2)

def contains_bigram(bigram_set, bigram):
    return bigram in bigram_set

# 使用例
if __name__ == "__main__":
    string1 = "paraparaparadise"
    string2 = "paragraph"

    X = create_bigram_set(string1)
    Y = create_bigram_set(string2)

    print("X:", X)
    print("Y:", Y)
    print("和集合:", union_bigrams(X, Y))
    print("積集合:", intersection_bigrams(X, Y))
    print("差集合:", difference_bigrams(X, Y))
    print("'se'がXに含まれるか:", contains_bigram(X, 'se'))
    print("'se'がYに含まれるか:", contains_bigram(Y, 'se'))