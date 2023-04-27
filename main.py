from task1.task1 import length_of_longest_substring
from task2.task2 import sort_sentences_by_info_density
from task3.task3 import combine_sentences


# Some examples for task1
s = "abcabcbb"
print(length_of_longest_substring(s))
# The answer is 3

s = "bbbbb"
print(length_of_longest_substring(s))
# The answer 1

s = "pwwkew"
print(length_of_longest_substring(s))
# The answer is 3


# An example for task 2
text = "The quick brown fox jumps over the lazy dog. The dog barks at the fox. The cat sleeps on the mat."
sorted_sentences = sort_sentences_by_info_density(text)
print(sorted_sentences)
# The answer is 'The quick brown fox jumps over the lazy dog.', 'The dog barks at the fox.', 'The cat sleeps on the mat.


# Some Examples for task 3
# Example 1
sentence1 = "The cat sat on the mat."
sentence2 = "The mat was soft and comfortable."
combined_sentence = combine_sentences(sentence1, sentence2)
print(combined_sentence)

# Example 2
sentence1 = "I went to the store to buy some milk."
sentence2 = "I also needed to get some bread."
combined_sentence = combine_sentences(sentence1, sentence2)
print(combined_sentence)

# Example 3
sentence1 = 'I went to the store.'
sentence2 = 'I bought some milk and eggs.'
merged_sentence = combine_sentences(sentence1, sentence2)
print(merged_sentence)
