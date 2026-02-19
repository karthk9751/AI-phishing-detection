import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

# input text
text = input("Paste your article:\n")

# clean text
stop_words = set(stopwords.words("english"))
words = word_tokenize(text.lower())

# word frequency
freq = {}
for word in words:
    if word.isalnum() and word not in stop_words:
        freq[word] = freq.get(word,0)+1

# sentence tokenize
sentences = sent_tokenize(text)

# sentence scoring
scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in freq:
            scores[sentence] = scores.get(sentence,0)+freq[word]

# top sentences selection
summary_sentences = heapq.nlargest(3, scores, key=scores.get)

# summary output
summary = " ".join(summary_sentences)

print("\n--- SUMMARY ---\n")
print(summary)
