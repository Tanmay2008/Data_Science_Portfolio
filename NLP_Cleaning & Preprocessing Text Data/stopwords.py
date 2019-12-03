# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words('english'))
print(stopwords)
with open("shakespeare.txt", 'rb') as f:
    content = f.read().decode('utf-8')
tokens = word_tokenize(content)
withoutStopwords = [w for w in tokens if w not in stopwords]
#print("WS::", withoutStopwords)
for w in tokens:
    if w not in stopwords:
        withoutStopwords.append(w)
        print(withoutStopwords)

