from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwords = list(stopwords.words('english'))
numbers = list(range(0, 100))       #numbers that is identifiers of pages
forumSpecificWords = ['>', '<', '?', '[', ']', '*'] + numbers #special signs
stopwords += forumSpecificWords
print('All tokens in English alphabet:', stopwords)

with open("shakespeare.txt", 'rb') as f:
    content = f.read().decode('utf-8')
    tokens = word_tokenize(content)
    withoutStopWords = [w for w in tokens if w not in stopwords]

    for w in tokens:
        if w not in stopwords:
            withoutStopWords.append(w.strip().lower())     #clean white spaces
          #  withoutStopWords.append(w.strip().lower())
print(withoutStopWords)
