import pytest

from task3 import combine_sentences


def test_combine_sentences_simple():
    sentence1 = "I like pizza."
    sentence2 = "Pizza is my favorite food."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "I like pizza. Pizza is my favorite food."


def test_combine_sentences_with_conjunction():
    sentence1 = "I went to the store."
    sentence2 = "I forgot my wallet."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "I went to the store. I forgot my wallet."


def test_combine_sentences_with_preposition():
    sentence1 = "I studied for the test."
    sentence2 = "The test was very difficult."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "I studied for the test. The test was very difficult."
