from nltk import skipgrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import itertools

stopwords = list(stopwords.words('english'))
numbers = list(range(0, 100))
forumSpecificWords = ['>', '<', '?', '[', ']', '*'] + numbers
stopwords += forumSpecificWords

with open("shakespeare.txt", 'rb') as f:
    content = f.read().decode('utf-8')
    tokens = word_tokenize(content)
    withoutStopwords = [w for w in tokens if w not in stopwords]

    for w in tokens:
        if w not in stopwords:
            withoutStopwords.append(w.strip())

            print("\n-----2,2:", list(skipgrams(itertools.islice(withoutStopwords, 100, 2, 2))))
            print("\n-----2,3:", list(skipgrams(itertools.islice(withoutStopwords, 100, 2, 3))))
            print("\n-----3,2:", list(skipgrams(itertools.islice(withoutStopwords, 100, 3, 2))))