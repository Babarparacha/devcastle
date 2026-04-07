from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
# Slightly larger dataset for meaningful selection demo
corpus = [
    ("I love NLP and language processing", "positive"),
    ("NLP is amazing and powerful", "positive"),
    ("I enjoy learning about machine learning", "positive"),
    ("This is a great course on AI", "positive"),
    ("Wonderful lecture on deep learning today", "positive"),
    ("I hate bugs and broken code", "negative"),
    ("This error is very frustrating", "negative"),
    ("The program keeps crashing constantly", "negative"),
    ("I dislike this confusing documentation", "negative"),
    ("Terrible performance and slow results", "negative"),
]

texts  = [c[0] for c in corpus]
labels = [c[1] for c in corpus]

le     = LabelEncoder()
y      = le.fit_transform(labels)
# print(y)

# Vectorize first
vec    = TfidfVectorizer()
X      = vec.fit_transform(texts)
vocab_fs = vec.get_feature_names_out()

print(f"\nOriginal features: {X.shape[1]} words")
print("\n")
print(f"All words: {list(vocab_fs)}")

# ── Chi-Square Feature Selection ─────────────────────────
k = min(8, X.shape[1])
selector = SelectKBest(chi2, k=k)
X_selected = selector.fit_transform(X, y)

selected_mask  = selector.get_support()
selected_words = [vocab_fs[i] for i, m in enumerate(selected_mask) if m]
scores         = selector.scores_

print(f"\nAfter Chi-Square selection (top {k} features): {X_selected.shape[1]} words")
print(f"Selected words: {selected_words}")

print(f"\n── All Word Scores (Chi-Square) ──")
word_scores = sorted(zip(vocab_fs, scores), key=lambda x: x[1], reverse=True)
print(f"  {'Word':<20} {'Score':>10}  {'Importance'}")
print(f"  {'-'*50}")
for word, score in word_scores:
    bar = "█" * int(score / max(scores) * 20)
    print(f"  {word:<20} {score:>10.3f}  {bar}")

# ── Frequency-based filtering ─────────────────────────────
print("\n── Frequency-Based Filtering (min/max document frequency) ──")
vec_filtered = TfidfVectorizer(min_df=2, max_df=0.8)
X_filtered   = vec_filtered.fit_transform(texts)
print(f"  Original vocab size  : {len(vocab_fs)}")
print(f"  After freq filtering : {len(vec_filtered.get_feature_names_out())}")
print(f"  Kept words           : {list(vec_filtered.get_feature_names_out())}")
