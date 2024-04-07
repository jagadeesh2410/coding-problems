import re

def nonnumerical(sentence):
    word=re.findall(r'\b[a-zA-Z]+\b',sentence)
    return' '.join(word)

sentence="hello 23bhg perfect"

print(nonnumerical(sentence))
