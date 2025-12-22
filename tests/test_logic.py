import pytest
from logic import *
def test_palindrome():
    assert is_palindrome("kajak")
    assert is_palindrome("Kobyła ma mały bok")
    assert not is_palindrome("python")


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5

    with pytest.raises(ValueError):
        fibonacci(-1)


def test_vowels():
    assert count_vowels("Python") == 2
    assert count_vowels("AEIOUY") == 6
    assert count_vowels("") == 0


def test_discount():
    assert calculate_discount(100, 0.2) == 80
    assert calculate_discount(50, 0) == 50

    with pytest.raises(ValueError):
        calculate_discount(100, 2)


def test_flatten():
    assert flatten_list([1, [2, 3]]) == [1, 2, 3]
    assert flatten_list([[1]]) == [1]


def test_words():
    assert word_frequencies("Hello hello") == {"hello": 2}


def test_prime():
    assert is_prime(2)
    assert not is_prime(4)
