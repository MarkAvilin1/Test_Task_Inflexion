"""
Task 3 **Communication Abilities**

Sentence Combination
Implement a program in Python that combines two sentences into one, retaining the information from both sentences. The combined sentence should preserve the meaning and context of both input sentences.
**Difficulty: Hard**
"""
import nltk
from nltk.tokenize import word_tokenize


def combine_sentences(sentence1, sentence2):
    # Tokenize the input sentences
    tokens1 = word_tokenize(sentence1)
    tokens2 = word_tokenize(sentence2)

    # Tag the tokens with their part-of-speech (POS) tags
    tagged1 = nltk.pos_tag(tokens1)
    tagged2 = nltk.pos_tag(tokens2)

    # Find the main verb in the first sentence
    main_verb1 = None
    for i in range(len(tagged1)):
        if tagged1[i][1].startswith('VB'):
            main_verb1 = tagged1[i][0]
            break

    # Find the main verb in the second sentence
    main_verb2 = None
    for i in range(len(tagged2)):
        if tagged2[i][1].startswith('VB'):
            main_verb2 = tagged2[i][0]
            break

    # Combine the sentences based on their main verbs
    if main_verb1 is not None and main_verb2 is not None:
        if main_verb1 == main_verb2:
            combined_sentence = sentence1.strip()[:-len(main_verb1)].strip() + ' ' + sentence2.strip()[
                                                                                     len(main_verb2):].strip()
        else:
            combined_sentence = sentence1.strip() + ' ' + sentence2.strip()
    else:
        combined_sentence = sentence1.strip() + ' ' + sentence2.strip()

    # Return the combined sentence
    return combined_sentence
