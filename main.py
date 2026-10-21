from nltk.tokenize import sent_tokenize
text = "NLTK is a great NLP toolkit. It makes processing text easy!"
#splits a string into a list of sentences, handling punctuation and abbreviations.
sentences = sent_tokenize(text)
print(sentences)

from nltk.tokenize import word_tokenize

sentence = "Tokenization is easy with NLTK's word_tokenize."
words = word_tokenize(sentence)
print(words)