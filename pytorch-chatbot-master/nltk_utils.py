import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

"""
tokenize(sentence) function takes a string input (a sentence) and tokenizes it, 
which means splitting the sentence into words. 
The function uses the word_tokenize function from the Natural Language Toolkit (nltk) library 
to split the sentence into words and returns the tokenized list of words.
"""
def tokenize(sentence):

    return nltk.word_tokenize(sentence)

"""
stem(word) function takes a word and returns its stem form. 
Stemming is the process of reducing a word to its base or root form. 
In this function, the Porter stemming algorithm is used to get the stem of the word.
"""
def stem(word):

    return stemmer.stem(word.lower())


"""
bag_of_words(tokenized_sentence, words) function takes a tokenized sentence and a list of unique words 
in the entire dataset. 
It then returns a bag of words, which is a vector representation of the sentence. 
The vector has the same length as the list of unique words. Each element in the vector represents 
whether the corresponding word in the unique words list appears in the sentence or not. 
If the word is present in the sentence, its corresponding element in the vector is 1, otherwise, it's 0. 
The function first stems each word in the sentence using the stem function defined above. 
It then initializes a vector with all zeros of the same length as the list of unique words. 
Finally, for each word in the tokenized sentence, the function checks whether 
the word is in the list of unique words. 
If it is, it sets the corresponding element in the vector to 1.
"""
def bag_of_words(tokenized_sentence, words):

    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag