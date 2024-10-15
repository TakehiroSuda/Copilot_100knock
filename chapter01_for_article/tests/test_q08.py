import pytest
from src.q08 import cipher

def test_cipher_lowercase():
    assert cipher("abc") == "zyx"
    assert cipher("xyz") == "cba"

def test_cipher_mixed_case():
    assert cipher("aBcXyZ") == "zBxXbZ"

def test_cipher_non_alpha():
    assert cipher("123!@#") == "123!@#"

def test_cipher_empty_string():
    assert cipher("") == ""

def test_cipher_sentence():
    assert cipher("Hello, World!") == "Hvool, Wliow!"