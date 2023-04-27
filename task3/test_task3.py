import pytest

from task3 import combine_sentences


def test_combine_sentences_simple():
    sentence1 = "I like pizza."
    sentence2 = "Pizza is my favorite food."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "I like pizza, and pizza is my favorite food."


def test_combine_sentences_with_common_words():
    sentence1 = "The book was on the table."
    sentence2 = "The table was made of wood."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "The book was on the table, and the table was made of wood."


def test_combine_sentences_with_conjunction():
    sentence1 = "I went to the store."
    sentence2 = "I forgot my wallet."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "I went to the store, but I forgot my wallet."


def test_combine_sentences_with_preposition():
    sentence1 = "I studied for the test."
    sentence2 = "The test was very difficult."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "I studied for the test, and the test was very difficult."


def test_combine_sentences_with_same_word():
    sentence1 = "The cat was black."
    sentence2 = "Black cats are considered lucky."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "The cat was black, and black cats are considered lucky."


def test_combine_sentences_capitalization():
    sentence1 = "the sun is shining."
    sentence2 = "the sky is blue."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "The sun is shining, and the sky is blue."


def test_combine_sentences_with_two_sentences_same():
    sentence1 = "The cat was black."
    sentence2 = "The cat was sleeping."

    combined_sentence = combine_sentences(sentence1, sentence2)

    assert combined_sentence == "The cat was black, and the cat was sleeping."
