import nltk
from nltk.tokenize import sent_tokenize
text="Hello Miss.Vanita, what are you doin today k? The weather is great, and city is awesome. The sky is pinkish.blue."
print(text)
tokenize_sent=sent_tokenize(text)
print(tokenize_sent)
from nltk.tokenize import word_tokenize
tokenize_word=word_tokenize(text)
print(tokenize_word)

from nltk.probability import FreqDist
fdist=FreqDist(tokenize_word)
print(fdist)

import matplotlib.pyplot as plt
fdist.plot()
plt.show()

from nltk.corpus import stopwords
stop_words=set(stopwords.word('english'))
print(stop_words)

filtered_words=[]
for w in tokenize_word:
    if w not in stop_words:
        filtered_words.append(w)
print(w)

print(filtered_words)
print(tokenize_words)
