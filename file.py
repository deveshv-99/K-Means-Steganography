import nltk
import math

nltk.download('punkt')
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
porter = PorterStemmer()
sentence = "Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
words = word_tokenize(sentence)
print(" Output of Stemming in NLP")
print("Given Sentence: ", sentence)
for w in words: 
  print(w, ": ", porter.stem(w))
