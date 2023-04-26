"""
Task 2 **Professional Aptitude**.

Information Density Sentence Sorting.
Implement a program in Python that sorts sentences in a given text by their information density.
The sentences should be sorted in descending order, with the most information-dense sentence appearing first.
**Difficulty: Medium**
"""

import nltk
from operator import itemgetter


def calculate_info_density(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(tokens)
    num_nouns = len([token for token, pos in tagged_tokens if pos.startswith('NN')])
    num_verbs = len([token for token, pos in tagged_tokens if pos.startswith('VB')])
    num_adjectives = len([token for token, pos in tagged_tokens if pos.startswith('JJ')])
    total_words = len(tokens)
    info_density = (num_nouns + num_verbs + num_adjectives) / total_words
    return info_density


def sort_sentences_by_info_density(text):
    sentences = nltk.sent_tokenize(text)
    info_densities = [(sentence, calculate_info_density(sentence)) for sentence in sentences]
    sorted_sentences = sorted(info_densities, key=itemgetter(1), reverse=True)
    return [sentence for sentence, info_density in sorted_sentences]
