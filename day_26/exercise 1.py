from sklearn.feature_extraction.text import CountVectorizer

# 1. Sample Data
corpus = [
    'student learn nlp',
    'nlp is fun',
    'student learn python'
]

# 2. Initialize the BoW model
vectorizer = CountVectorizer()

# 3. Fit and Transform (The Math)
X = vectorizer.fit_transform(corpus)

# 4. Show the "Vocabulary"
print("Vocabulary Index:\n", vectorizer.vocabulary_)
print("\n")
# 5. Show the resulting 0s and 1s
print("Sentence Vectors:\n", X.toarray())