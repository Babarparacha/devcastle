from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


documents = [
    "I love NLP and machine learning",
    "NLP is used in chatbots and search engines",
    "Machine learning powers artificial intelligence",
    "I hate spam emails and junk messages",
    "Spam detection uses machine learning algorithms",
]

tfidf_vec = TfidfVectorizer()
X_tfidf   = tfidf_vec.fit_transform(documents)
vocab_tfidf = tfidf_vec.get_feature_names_out()


print("\nTF-IDF Matrix (higher = more important in that doc):")
header = f"  {'Doc':<6}" + "".join(f"{w[:7]:>9}" for w in vocab_tfidf)
print(header)

print("  " + "-" * (6 + 9 * len(vocab_tfidf)))
for i, row in enumerate(X_tfidf.toarray()):
    line = f"  Doc {i}:" + "".join(f"{v:>9.2f}" for v in row)
    print(line)