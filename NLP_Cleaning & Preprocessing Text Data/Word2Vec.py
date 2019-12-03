from gensim.test.utils import common_texts
from gensim.models import word2vec, Word2Vec

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

            model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
            inputTooMLModel = model.train(itertools.islice(withoutStopwords, 10_000), total_examples=len(withoutStopwords), epochs=1)
            print(inputTooMLModel)
