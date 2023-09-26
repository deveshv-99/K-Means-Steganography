import os
import nltk
from nltk.tree import Tree
from nltk.draw.tree import TreeView
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = "the little yellow dog barked at the cat"
grammar = ('''NP: {<DT>?<JJ>*<NN>} # NP''')
chunkParser = nltk.RegexpParser(grammar)
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
print(tagged)
tree = chunkParser.parse(tagged)
for subtree in tree.subtrees():
    print(subtree)
tree.draw()