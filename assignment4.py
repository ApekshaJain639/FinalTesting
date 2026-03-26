import nltk
nltk.download('all')  # Or download specific packages

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag



text = "Hello, welcome to NLP."
tokens = word_tokenize(text)
print(tokens)