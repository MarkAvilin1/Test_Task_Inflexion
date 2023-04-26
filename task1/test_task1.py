import pytest

from task1 import length_of_longest_substring


@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("abcdefg", 7),
    ("aab", 2),
    ("", 0),
    ("abcdefghijklmnopqrstuvwxyz", 26),
    ("abcdabcefghijklmn", 12),
])
def test_length_of_longest_substring(s, expected):
    assert length_of_longest_substring(s) == expected


def test_length_of_longest_substring_edge_cases():
    # Test with input that has only one character
    s = "a"
    assert length_of_longest_substring(s) == 1

    # Test with input that has only repeated characters
    s = "aaaaa"
    assert length_of_longest_substring(s) == 1

    # Test with input that has all unique characters
    s = "abcdefghijklmnopqrstuvwxyz"
    assert length_of_longest_substring(s) == 26

    # Test with input that has repeated characters in the middle
    s = "abcdefghijkklmnopqrstuvwxyz"
    assert length_of_longest_substring(s) == 25

    # Test with input that has repeated characters at the end
    s = "abcdefghijklmnopqrstuvwxyzz"
    assert length_of_longest_substring(s) == 26

    # Test with input that has repeated characters at the beginning
    s = "aabcdefghijklmnopqrstuvwxyz"
    assert length_of_longest_substring(s) == 26


def test_length_of_longest_substring_unicode():
    # Test with input that contains unicode characters
    s = "Привет"
    assert length_of_longest_substring(s) == 6

    # Test with input that contains unicode characters and repeated characters
    s = "مرحبا"
    assert length_of_longest_substring(s) == 5

