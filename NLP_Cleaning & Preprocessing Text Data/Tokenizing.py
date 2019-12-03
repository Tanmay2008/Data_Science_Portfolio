#import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
text1 = "It's true that the chicken was smart."
tokens = word_tokenize(text1)
print(tokens)
