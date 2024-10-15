import pytest
from src.q09 import shuffle_middle, shuffle_sentence

def test_shuffle_middle_short_word():
    assert shuffle_middle("cat") == "cat"
    assert shuffle_middle("dog") == "dog"

def test_shuffle_middle_long_word():
    word = "shuffle"
    shuffled = shuffle_middle(word)
    assert shuffled[0] == 's'
    assert shuffled[-1] == 'e'
    assert sorted(shuffled[1:-1]) == sorted(word[1:-1])

def test_shuffle_sentence():
    sentence = "This is a test sentence"
    shuffled = shuffle_sentence(sentence)
    words = sentence.split()
    shuffled_words = shuffled.split()
    assert len(words) == len(shuffled_words)
    for original, shuffled in zip(words, shuffled_words):
        if len(original) > 4:
            assert original[0] == shuffled[0]
            assert original[-1] == shuffled[-1]
            assert sorted(original[1:-1]) == sorted(shuffled[1:-1])
        else:
            assert original == shuffled
