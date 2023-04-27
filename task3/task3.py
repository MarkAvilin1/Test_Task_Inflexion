"""
Task 3 **Communication Abilities**

Sentence Combination
Implement a program in Python that combines two sentences into one, retaining the information from both sentences. The combined sentence should preserve the meaning and context of both input sentences.
**Difficulty: Hard**
"""
import spacy

nlp = spacy.load('en_core_web_sm')


def combine_sentences(s1, s2):
    doc1 = nlp(s1)
    doc2 = nlp(s2)

    # Find the root verb of the first sentence
    root1 = None
    for token in doc1:
        if token.head == token:
            root1 = token
            break

    # Find the root verb of the second sentence
    root2 = None
    for token in doc2:
        if token.head == token:
            root2 = token
            break
            
    # Capitalize the first sent. and make the 2nd sent. lower-case 
    s1 = s1.capitalize()
    s2 = s2.lower()
    
    # Combine the sentences based on their roots
    if root1 == root2:
        return f"{s1[:-len(root1.text)].replace('.', '')}," \
               f" {s2[root2.idx + len(root2.text):].replace('.', '')}.".replace(' i ', ' I ')
    elif root1.pos_ == 'VERB' and root2.pos_ == 'VERB':
        return f"{s1.replace('.', '')}, but {s2.replace('.', '')}.".replace(' i ', ' I ') \
            if root1.lemma_ != root2.lemma_ else f"{s1.replace('.', '')} " \
                                                 f"and {s2.replace('.', '')}.".replace(' i ', ' I ')
    else:
        return f"{s1.replace('.', '')}, and {s2.replace('.', '')}.".replace(' i ', ' I ')

