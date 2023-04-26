import pytest
from task2 import sort_sentences_by_info_density


def test_sort_sentences_by_info_density():
    text = "I like turtles. Turtles are awesome."
    expected_output = ["Turtles are awesome.", "I like turtles."]
    assert sort_sentences_by_info_density(text) == expected_output

