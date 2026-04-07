from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

query = "machine learning and neural networks for NLP"

docs  = [
    "Deep learning and neural networks are used in NLP systems",
    "Natural language processing uses machine learning models",
    "I love eating biryani and nihari in Lahore",
    "Python is a great programming language for AI",
    "Football and cricket are popular sports in Pakistan",
    "Transformers and BERT revolutionized natural language processing",
]

print(f"\nQuery: '{query}'")
print(f"\nDocuments to compare against:")
for i, d in enumerate(docs):
    print(f"  Doc {i}: '{d}'")

# # ── Cosine Similarity with TF-IDF ────────────────────────
all_texts  = [query] + docs
tfidf_sim  = TfidfVectorizer()
X_sim      = tfidf_sim.fit_transform(all_texts)

query_vec  = X_sim[0]
doc_vecs   = X_sim[1:]
scores     = cosine_similarity(query_vec, doc_vecs)[0]

# print(f"\n── Cosine Similarity Scores ──")
# print(f"  (1.0 = identical, 0.0 = completely unrelated)")
# print(f"\n  {'#':<4} {'Score':>6}  {'Bar':<25} Document")
# print(f"  {'-'*75}")

ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
for rank, (idx, score) in enumerate(ranked):
    bar  = "█" * int(score * 30)
    doc_preview = docs[idx][:45]
    print(f"  #{rank+1:<3} {score:>6.3f}  {bar:<25} '{doc_preview}...'")

print(f"\n  Best match → Doc {ranked[0][0]}: '{docs[ranked[0][0]]}'")