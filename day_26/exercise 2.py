# ============================================================
#   NLP LECTURE DEMO 
#   Topics: Tokenization, Segmentation, Stemming, Normalization,
#           Regex, POS, NER, Chunking, Lemmatization, WordNet,
#           BoW, TF-IDF, Feature Selection, Embeddings, Similarity
#
#   INSTALL FIRST (run in terminal):
#   pip install nltk spacy scikit-learn gensim
#   python -m spacy download en_core_web_sm
# ============================================================

import nltk
# nltk.download('punkt',            quiet=True)
# nltk.download('punkt_tab',        quiet=True)
# nltk.download('stopwords',        quiet=True)
# nltk.download('averaged_perceptron_tagger',     quiet=True)
# nltk.download('averaged_perceptron_tagger_eng', quiet=True)
# nltk.download('maxent_ne_chunker',  quiet=True)
# nltk.download('maxent_ne_chunker_tab', quiet=True)
# nltk.download('words',            quiet=True)
# nltk.download('wordnet',          quiet=True)
# nltk.download('omw-1.4',          quiet=True)


# ============================================================
# SECTION 1: WORD & SENTENCE TOKENIZATION
# ============================================================

from nltk.tokenize import word_tokenize, sent_tokenize, TweetTokenizer

print("=" * 60)
print("SECTION 1: WORD & SENTENCE TOKENIZATION")
print("=" * 60)

text = "Ali is learning NLP at university. He loves Python! Can he build a chatbot? Yes, he can."

# ── Sentence Tokenization ─────────────────────────────────
print("\n── Sentence Tokenization ──")
sentences = sent_tokenize(text)
for i, s in enumerate(sentences):
    print(f"  Sentence {i+1}: {s}")

# ── Word Tokenization ─────────────────────────────────────
print("\n── Word Tokenization ──")
words = word_tokenize(text)
print(f"  Tokens ({len(words)}): {words}")

# ── Tweet Tokenizer (handles social media text) ───────────
print("\n── Tweet Tokenizer (for social media text) ──")
tweet = "OMG!! I LOVE #NLP sooo much 😊😊 @AI_class check this out!!!"
tweet_tokenizer = TweetTokenizer()
tweet_tokens = tweet_tokenizer.tokenize(tweet)
print(f"  Input : {tweet}")
print(f"  Tokens: {tweet_tokens}")

# ── Comparison: Word boundaries matter ───────────────────
print("\n── Why tokenization matters ──")
examples = [
    "don't",
    "New York",
    "state-of-the-art",
    "Ph.D.",
    "U.S.A.",
]
for ex in examples:
    tokens = word_tokenize(ex)
    print(f"  '{ex}' → {tokens}")


# ============================================================
# SECTION 2: WORD SEGMENTATION
# ============================================================

print("\n" + "=" * 60)
print("SECTION 2: WORD SEGMENTATION")
print("=" * 60)

# ── English edge cases ────────────────────────────────────
print("\n── English Segmentation Edge Cases ──")
tricky = [
    "I'm going to the state-of-the-art lab.",
    "The U.S.A. won 100 gold medals.",
    "She's been running since 6 a.m.",
]
for t in tricky:
    tokens = word_tokenize(t)
    print(f"\n  Input : '{t}'")
    print(f"  Tokens: {tokens}")

# ── Subword segmentation concept (used in GPT/BERT) ──────
print("\n── Subword Segmentation Concept (BPE style) ──")
print("  In modern LLMs, words are split into subword units:")
subword_examples = {
    "unbelievable" : ["un", "believ", "able"],
    "tokenization" : ["token", "ization"],
    "ChatGPT"      : ["Chat", "G", "PT"],
    "preprocessing": ["pre", "process", "ing"],
}
for word, parts in subword_examples.items():
    print(f"  '{word}' → {parts}")
print("\n  This reduces vocabulary size while handling unknown words.")


# ============================================================
# SECTION 3: STEMMING
# ============================================================

from nltk.stem import PorterStemmer, SnowballStemmer

print("\n" + "=" * 60)
print("SECTION 3: STEMMING")
print("=" * 60)

porter   = PorterStemmer()
snowball = SnowballStemmer("english")

words_to_stem = [
    "running", "studies", "happily", "connection",
    "caring", "wolves", "better", "flies", "arguing",
    "beautiful", "learning", "computed", "generously"
]

print(f"\n{'Word':<20} {'Porter':<20} {'Snowball':<20}")
print("-" * 60)
for word in words_to_stem:
    p = porter.stem(word)
    s = snowball.stem(word)
    print(f"  {word:<18} {p:<20} {s:<20}")

print("\n  Notice: Sometimes stems are NOT real English words.")
print("  This is the tradeoff — fast but rough.")

# ── Stemming reduces vocabulary ───────────────────────────
print("\n── How stemming reduces vocabulary size ──")
sentences_stem = [
    "The runner is running in the race",
    "He runs faster than all other runners",
    "Running is his favorite sport",
]
all_words_before = set()
all_words_after  = set()

for s in sentences_stem:
    tokens = word_tokenize(s.lower())
    all_words_before.update(tokens)
    all_words_after.update([porter.stem(t) for t in tokens])

print(f"  Vocabulary BEFORE stemming: {len(all_words_before)} words → {sorted(all_words_before)}")
print(f"  Vocabulary AFTER  stemming: {len(all_words_after)} words → {sorted(all_words_after)}")
print(f"  Reduction: {len(all_words_before) - len(all_words_after)} words removed")


# ============================================================
# SECTION 4: TEXT NORMALIZATION
# ============================================================

import re, string

print("\n" + "=" * 60)
print("SECTION 4: TEXT NORMALIZATION")
print("=" * 60)

raw = "HELLO!!!  I'm gonna check ur msg @ 9 AM... the URL is https://example.com 😊 #nlp #AI"
print(f"\nRaw input:\n  '{raw}'")

# Step by step normalization
step1 = raw.lower()
print(f"\nStep 1 - Lowercase:\n  '{step1}'")

step2 = re.sub(r'http\S+|www\S+', '', step1)
print(f"\nStep 2 - Remove URLs:\n  '{step2}'")

step3 = re.sub(r'[^\x00-\x7F]+', '', step2)
print(f"\nStep 3 - Remove emojis/unicode:\n  '{step3}'")

step4 = re.sub(r'#\w+|@\w+', '', step3)
print(f"\nStep 4 - Remove hashtags and mentions:\n  '{step4}'")

step5 = re.sub(r'[^a-z\s]', '', step4)
print(f"\nStep 5 - Remove punctuation and numbers:\n  '{step5}'")

step6 = re.sub(r'\s+', ' ', step5).strip()
print(f"\nStep 6 - Remove extra whitespace:\n  '{step6}'")

# Contraction expansion
print("\n── Contraction Expansion ──")
contractions = {
    "i'm"    : "i am",
    "don't"  : "do not",
    "won't"  : "will not",
    "it's"   : "it is",
    "can't"  : "cannot",
    "they're": "they are",
    "gonna"  : "going to",
    "wanna"  : "want to",
    "ur"     : "your",
    "u"      : "you",
}
sample = "i'm gonna learn nlp. u don't wanna miss it. it's amazing!"
print(f"  Before: '{sample}'")
for short, full in contractions.items():
    sample = sample.replace(short, full)
print(f"  After : '{sample}'")


# ============================================================
# SECTION 5: REGULAR EXPRESSIONS FOR STRING PARSING
# ============================================================

print("\n" + "=" * 60)
print("SECTION 5: REGULAR EXPRESSIONS")
print("=" * 60)

sample_text = """
Contact us at support@nlpclass.com or admin@university.edu
Visit: https://nlpclass.com or http://university.edu/nlp
Phone: +92-300-1234567 or 021-9876543
Date: 25/03/2024 and 2024-03-25
Price: $500 or PKR 150,000
"""
print(f"Sample text:{sample_text}")

# ── Email extraction ──────────────────────────────────────
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', sample_text)
print(f"Emails found:    {emails}")

# ── URL extraction ────────────────────────────────────────
urls = re.findall(r'https?://\S+', sample_text)
print(f"URLs found:      {urls}")

# ── Phone numbers ─────────────────────────────────────────
phones = re.findall(r'[\+\d][\d\-]{8,}', sample_text)
print(f"Phones found:    {phones}")

# ── Dates ─────────────────────────────────────────────────
dates = re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2}', sample_text)
print(f"Dates found:     {dates}")

# ── Prices ────────────────────────────────────────────────
prices = re.findall(r'\$[\d,]+|PKR [\d,]+', sample_text)
print(f"Prices found:    {prices}")

# ── Common cleaning patterns ─────────────────────────────
print("\n── Common Cleaning Patterns ──")
dirty = "Hello!!!   This  is  SOOOOO   great... Click http://spam.com #ad"
patterns = [
    (r'http\S+',           '',  "Remove URLs"),
    (r'#+\w+',             '',  "Remove hashtags"),
    (r'[^a-zA-Z\s]',       '',  "Keep letters only"),
    (r'(.)\1{2,}',        r'\1',"Fix repeated chars (sooo→so)"),
    (r'\s+',               ' ', "Normalize whitespace"),
]
result = dirty
print(f"  Input: '{dirty}'")
for pattern, replacement, desc in patterns:
    result = re.sub(pattern, replacement, result).strip()
    print(f"  → {desc}: '{result}'")


# ============================================================
# SECTION 6: POS TAGGING
# ============================================================

print("\n" + "=" * 60)
print("SECTION 6: POS TAGGING")
print("=" * 60)

pos_legend = {
    'NN' :'Noun singular',    'NNS':'Noun plural',
    'NNP':'Proper noun',      'NNPS':'Proper noun plural',
    'VB' :'Verb base',        'VBD':'Verb past tense',
    'VBG':'Verb gerund',      'VBN':'Verb past participle',
    'VBZ':'Verb 3rd person',  'JJ' :'Adjective',
    'JJR':'Adjective comp.',  'JJS':'Adjective super.',
    'RB' :'Adverb',           'DT' :'Determiner',
    'IN' :'Preposition',      'PRP':'Personal pronoun',
    'CC' :'Conjunction',      'CD' :'Number',
}

sentences_pos = [
    "Ali built an amazing NLP system in Python.",
    "The fast red car crashed badly yesterday.",
    "She will be learning machine learning tomorrow.",
]

for sentence in sentences_pos:
    print(f"\nSentence: '{sentence}'")
    tokens   = word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    print(f"  {'Word':<15} {'Tag':<8} {'Meaning'}")
    print(f"  {'-'*45}")
    for word, tag in pos_tags:
        meaning = pos_legend.get(tag, tag)
        print(f"  {word:<15} {tag:<8} {meaning}")

# ── POS for disambiguation ────────────────────────────────
print("\n── POS Tagging for Word Disambiguation ──")
ambiguous = [
    "I will bank the money.",
    "He sat by the river bank.",
    "She can can the vegetables.",
]
for s in ambiguous:
    tokens = word_tokenize(s)
    tags   = nltk.pos_tag(tokens)
    print(f"\n  '{s}'")
    print(f"  Tags: {[(w, t) for w, t in tags]}")


# ============================================================
# SECTION 7: NER TAGGING
# ============================================================

import spacy
nlp_spacy = spacy.load("en_core_web_sm")

print("\n" + "=" * 60)
print("SECTION 7: NAMED ENTITY RECOGNITION (NER)")
print("=" * 60)

ner_texts = [
    "Elon Musk founded SpaceX in 2002 in California.",
    "Google was established in Menlo Park by Larry Page and Sergey Brin.",
    "The Pakistani team won the match in Karachi on Friday.",
    "Apple announced a $3 trillion market cap in January 2024.",
]

for text in ner_texts:
    doc = nlp_spacy(text)
    print(f"\nText: '{text}'")
    if doc.ents:
        print(f"  {'Entity':<25} {'Label':<12} {'Explanation'}")
        print(f"  {'-'*55}")
        for ent in doc.ents:
            print(f"  {ent.text:<25} {ent.label_:<12} {spacy.explain(ent.label_)}")
    else:
        print("  No entities found.")

# ── NER with NLTK (alternative) ──────────────────────────
print("\n── NER with NLTK ──")
nltk_sentence = "Barack Obama was born in Hawaii and became the President of the United States."
tokens_ner    = word_tokenize(nltk_sentence)
pos_ner       = nltk.pos_tag(tokens_ner)
tree          = nltk.ne_chunk(pos_ner)
print(f"  Sentence: '{nltk_sentence}'")
print("  Named Entities (NLTK):")
for subtree in tree:
    if hasattr(subtree, 'label'):
        entity = " ".join([token for token, pos in subtree.leaves()])
        print(f"    '{entity}' → {subtree.label()}")


# ============================================================
# SECTION 8: CHUNKING AND CHINKING
# ============================================================

print("\n" + "=" * 60)
print("SECTION 8: CHUNKING AND CHINKING")
print("=" * 60)

# ── Noun Phrase Chunking ──────────────────────────────────
print("\n── Noun Phrase (NP) Chunking ──")
sentence_chunk = "The quick brown fox jumps over the lazy old dog."
tokens_c  = word_tokenize(sentence_chunk)
pos_c     = nltk.pos_tag(tokens_c)

# Grammar: optional DT, any number of JJ, then NN or NNS
grammar_np = "NP: {<DT>?<JJ>*<NN.*>+}"
parser_np  = nltk.RegexpParser(grammar_np)
result_np  = parser_np.parse(pos_c)

print(f"  Sentence: '{sentence_chunk}'")
print(f"  POS Tags: {pos_c}")
print(f"\n  Noun Phrase Chunks found:")
for subtree in result_np.subtrees():
    if subtree.label() == 'NP':
        chunk = " ".join([word for word, tag in subtree.leaves()])
        print(f"    NP → '{chunk}'")

# ── Verb Phrase Chunking ──────────────────────────────────
print("\n── Verb Phrase (VP) Chunking ──")
grammar_vp = "VP: {<VB.*><RB>?<DT>?<NN.*>*}"
parser_vp  = nltk.RegexpParser(grammar_vp)
result_vp  = parser_vp.parse(pos_c)

for subtree in result_vp.subtrees():
    if subtree.label() == 'VP':
        chunk = " ".join([word for word, tag in subtree.leaves()])
        print(f"    VP → '{chunk}'")

# ── Chinking (removing from chunk) ───────────────────────
print("\n── Chinking (exclude verbs from NP chunks) ──")
grammar_chink = """
    NP: {<.*>+}       
        }<VB.*>+{     
"""
parser_chink = nltk.RegexpParser(grammar_chink)
sentence_chink = "The cat is sitting on the mat."
tokens_chink   = word_tokenize(sentence_chink)
pos_chink      = nltk.pos_tag(tokens_chink)
result_chink   = parser_chink.parse(pos_chink)

print(f"  Sentence: '{sentence_chink}'")
print(f"  Chunks after chinking (verbs removed):")
for subtree in result_chink.subtrees():
    if subtree.label() == 'NP':
        chunk = " ".join([word for word, tag in subtree.leaves()])
        print(f"    NP → '{chunk}'")

# ============================================================
# SECTION 9: LEMMATIZATION
# ============================================================

from nltk.stem import WordNetLemmatizer

print("\n" + "=" * 60)
print("SECTION 9: LEMMATIZATION")
print("=" * 60)

lemmatizer = WordNetLemmatizer()

# ── Stemming vs Lemmatization ─────────────────────────────
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

test_words = [
    ("running",    "v"),
    ("studies",    "v"),
    ("better",     "a"),
    ("wolves",     "n"),
    ("caring",     "v"),
    ("happily",    "r"),
    ("beautiful",  "a"),
    ("geese",      "n"),
    ("went",       "v"),
    ("mice",       "n"),
]

print(f"\n  {'Word':<15} {'Stemmed':<15} {'Lemmatized':<15} {'POS'}")
print(f"  {'-'*55}")
for word, pos in test_words:
    stemmed   = stemmer.stem(word)
    lemmatized = lemmatizer.lemmatize(word, pos=pos)
    print(f"  {word:<15} {stemmed:<15} {lemmatized:<15} ({pos})")

# ── SpaCy Lemmatization ───────────────────────────────────
print("\n── SpaCy Lemmatization (automatic, no POS needed) ──")
spacy_text = "The wolves were running faster than the geese and the mice."
doc_lem = nlp_spacy(spacy_text)
print(f"  Input: '{spacy_text}'")
print(f"\n  {'Token':<15} {'Lemma':<15}")
print(f"  {'-'*30}")
for token in doc_lem:
    if not token.is_punct and not token.is_space:
        print(f"  {token.text:<15} {token.lemma_:<15}")



# ============================================================
# SECTION 10: WORDNET
# ============================================================

from nltk.corpus import wordnet

print("\n" + "=" * 60)
print("SECTION 10: WORDNET")
print("=" * 60)

# ── Synsets ───────────────────────────────────────────────
print("\n── Synsets for 'car' ──")
for syn in wordnet.synsets('car'):
    print(f"  {syn.name():<20} → {syn.definition()}")
    print(f"    Lemmas   : {[l.name() for l in syn.lemmas()]}")

# ── Hypernyms and Hyponyms ────────────────────────────────
print("\n── Hierarchy for 'dog' (hypernyms = broader, hyponyms = narrower) ──")
dog = wordnet.synset('dog.n.01')
print(f"  Word     : dog")
print(f"  Hypernyms: {[h.name() for h in dog.hypernyms()]}")
print(f"  Hyponyms : {[h.name() for h in dog.hyponyms()[:5]]} ...")

# ── Semantic Similarity ───────────────────────────────────
print("\n── Semantic Similarity between words ──")
word_pairs = [
    ('dog',   'cat'),
    ('dog',   'car'),
    ('car',   'automobile'),
    ('man',   'woman'),
    ('king',  'queen'),
    ('nlp',   'python'),
]

print(f"  {'Word 1':<12} {'Word 2':<12} {'Similarity'}")
print(f"  {'-'*40}")
for w1, w2 in word_pairs:
    syn1 = wordnet.synsets(w1)
    syn2 = wordnet.synsets(w2)
    if syn1 and syn2:
        score = syn1[0].wup_similarity(syn2[0])
        bar   = "█" * int((score or 0) * 20)
        print(f"  {w1:<12} {w2:<12} {score:.2f}  {bar}")
    else:
        print(f"  {w1:<12} {w2:<12} N/A")

# ── Synonyms and Antonyms ─────────────────────────────────
print("\n── Synonyms and Antonyms for 'good' ──")
synonyms, antonyms = [], []
for syn in wordnet.synsets("good"):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

print(f"  Synonyms (first 10): {list(set(synonyms))[:10]}")
print(f"  Antonyms           : {list(set(antonyms))}")


# ============================================================
# SECTION 11: BAG OF WORDS (BoW)
# ============================================================

from sklearn.feature_extraction.text import CountVectorizer

print("\n" + "=" * 60)
print("SECTION 11: BAG OF WORDS MODEL")
print("=" * 60)

documents = [
    "I love NLP and machine learning",
    "NLP is used in chatbots and search engines",
    "Machine learning powers artificial intelligence",
    "I hate spam emails and junk messages",
    "Spam detection uses machine learning algorithms",
]

print("\nDocuments:")
for i, d in enumerate(documents):
    print(f"  Doc {i}: '{d}'")

vectorizer_bow = CountVectorizer()
X_bow = vectorizer_bow.fit_transform(documents)
vocab = vectorizer_bow.get_feature_names_out()

print(f"\nVocabulary ({len(vocab)} words):")
print(f"  {list(vocab)}")

print(f"\nBag of Words Matrix (rows=docs, cols=words):")
header = f"  {'Doc':<6}" + "".join(f"{w[:6]:>8}" for w in vocab)
print(header)
print("  " + "-" * (6 + 8 * len(vocab)))
for i, row in enumerate(X_bow.toarray()):
    line = f"  Doc {i}:" + "".join(f"{v:>8}" for v in row)
    print(line)

print("\n  Each row is a document. Each number = word count.")
print("  This matrix is your training data (X).")

# ── BoW limitation demo ───────────────────────────────────
print("\n── BoW Limitation: Word Order Is Lost ──")
s1 = "Dog bites man"
s2 = "Man bites dog"
X_lim = CountVectorizer().fit_transform([s1, s2]).toarray()
print(f"  '{s1}' → {X_lim[0]}")
print(f"  '{s2}' → {X_lim[1]}")
print("  Both produce IDENTICAL vectors even though meaning is different!")


# ============================================================
# SECTION 12: TF-IDF
# ============================================================

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

print("\n" + "=" * 60)
print("SECTION 12: TF-IDF")
print("=" * 60)

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

# ── Top keywords per document ─────────────────────────────
print("\n── Top 3 Keywords Per Document ──")
for i, doc in enumerate(documents):
    row   = X_tfidf.toarray()[i]
    top3  = np.argsort(row)[::-1][:3]
    kws   = [(vocab_tfidf[j], round(row[j], 3)) for j in top3 if row[j] > 0]
    print(f"  Doc {i}: '{doc[:35]}...' → {kws}")

print("\n  Common words (like 'and', 'is') score low.")
print("  Unique, specific words score high.")


# ============================================================
# SECTION 13: FEATURE SELECTION
# ============================================================

from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder

print("\n" + "=" * 60)
print("SECTION 13: FEATURE SELECTION")
print("=" * 60)

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

# Vectorize first
vec    = TfidfVectorizer()
X      = vec.fit_transform(texts)
vocab_fs = vec.get_feature_names_out()

print(f"\nOriginal features: {X.shape[1]} words")
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


# ============================================================
# SECTION 14: FEATURE EXTRACTION — WORD EMBEDDINGS
# ============================================================

print("\n" + "=" * 60)
print("SECTION 14: FEATURE EXTRACTION — WORD EMBEDDINGS")
print("=" * 60)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# Train a simple Word2Vec model on our small corpus
try:
    from gensim.models import Word2Vec

    sentences_w2v = [
        "king rules the kingdom with power",
        "queen rules beside the king",
        "man is a human being",
        "woman is a human being",
        "doctor treats patients in hospital",
        "nurse works alongside the doctor",
        "python is a programming language",
        "java is also a programming language",
        "nlp processes natural language text",
        "machine learning trains models on data",
        "deep learning uses neural networks",
        "neural networks learn from training data",
    ]

    tokenized = [word_tokenize(s.lower()) for s in sentences_w2v]

    model_w2v = Word2Vec(
        sentences   = tokenized,
        vector_size = 10,    # small for demo (real models use 100-300)
        window      = 3,
        min_count   = 1,
        epochs      = 200,
        seed        = 42,
    )

    print("\nWord2Vec trained on small corpus (vector_size=10 for demo)")
    print("Real models use vector_size=100-300 trained on billions of words.")

    demo_words = ["king", "queen", "man", "woman", "python", "nlp"]
    print(f"\n── Word Vectors (first 5 dimensions) ──")
    for word in demo_words:
        if word in model_w2v.wv:
            vec = model_w2v.wv[word][:5]
            print(f"  {word:<10} → [{', '.join(f'{v:>6.3f}' for v in vec)}, ...]")

    print(f"\n── Most Similar Words ──")
    for word in ["king", "python", "nlp"]:
        if word in model_w2v.wv:
            similar = model_w2v.wv.most_similar(word, topn=3)
            print(f"  Words similar to '{word}': {similar}")

    print(f"\n── Word Similarity Scores ──")
    pairs = [("king", "queen"), ("man", "woman"), ("python", "java"), ("king", "python")]
    for w1, w2 in pairs:
        if w1 in model_w2v.wv and w2 in model_w2v.wv:
            sim = model_w2v.wv.similarity(w1, w2)
            bar = "█" * int(sim * 20)
            print(f"  '{w1}' vs '{w2}': {sim:.3f}  {bar}")

except ImportError:
    print("\n  gensim not installed. Run: pip install gensim")
    print("  Showing concept only:")
    print("\n  Word2Vec maps each word to a dense vector:")
    print("  'king'   → [0.82, -0.31,  0.54, ...]  (100+ numbers)")
    print("  'queen'  → [0.79, -0.28,  0.51, ...]  (very similar!)")
    print("  'python' → [-0.12, 0.88, -0.43, ...]  (very different)")

# ── SpaCy embeddings (pre-trained) ───────────────────────
print("\n── SpaCy Pre-trained Embeddings ──")
words_emb = ["king", "queen", "man", "python", "language"]
print(f"  {'Word':<12} {'Vector dim':<15} {'First 5 values'}")
print(f"  {'-'*55}")
for word in words_emb:
    doc_emb = nlp_spacy(word)
    token   = doc_emb[0]
    preview = [round(float(v), 3) for v in token.vector[:5]]
    print(f"  {word:<12} {len(token.vector):<15} {preview} ...")


# ============================================================
# SECTION 15: DOCUMENT SIMILARITY
# ============================================================

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

print("\n" + "=" * 60)
print("SECTION 15: DOCUMENT SIMILARITY")
print("=" * 60)

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

# ── Cosine Similarity with TF-IDF ────────────────────────
all_texts  = [query] + docs
tfidf_sim  = TfidfVectorizer()
X_sim      = tfidf_sim.fit_transform(all_texts)

query_vec  = X_sim[0]
doc_vecs   = X_sim[1:]
scores     = cosine_similarity(query_vec, doc_vecs)[0]

print(f"\n── Cosine Similarity Scores ──")
print(f"  (1.0 = identical, 0.0 = completely unrelated)")
print(f"\n  {'#':<4} {'Score':>6}  {'Bar':<25} Document")
print(f"  {'-'*75}")
ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
for rank, (idx, score) in enumerate(ranked):
    bar  = "█" * int(score * 30)
    doc_preview = docs[idx][:45]
    print(f"  #{rank+1:<3} {score:>6.3f}  {bar:<25} '{doc_preview}...'")

print(f"\n  Best match → Doc {ranked[0][0]}: '{docs[ranked[0][0]]}'")

# ── SpaCy Semantic Similarity (embedding-based) ───────────
print("\n── SpaCy Semantic Similarity (uses word vectors) ──")
query_doc = nlp_spacy(query)
print(f"\n  Query: '{query}'")
print(f"\n  {'Score':>6}  {'Document'}")
print(f"  {'-'*65}")
spacy_scores = []
for doc_text in docs:
    doc_nlp = nlp_spacy(doc_text)
    sim     = query_doc.similarity(doc_nlp)
    spacy_scores.append((sim, doc_text))

for score, doc_text in sorted(spacy_scores, reverse=True):
    bar = "█" * int(score * 20)
    print(f"  {score:>6.3f}  {bar:<20} '{doc_text[:45]}...'")

# ── Pairwise Document Similarity Matrix ──────────────────
print("\n── Pairwise Similarity Matrix (all docs vs all docs) ──")
short_docs = [
    "I love NLP",
    "I enjoy natural language processing",
    "Machine learning is great",
    "I love pizza",
]
X_pair = TfidfVectorizer().fit_transform(short_docs)
matrix = cosine_similarity(X_pair)

labels_short = [f"D{i}" for i in range(len(short_docs))]
print(f"\n  {'':>4}", end="")
for l in labels_short:
    print(f"  {l:>6}", end="")
print()
print(f"  {'':>4}" + "-" * (8 * len(labels_short)))
for i, row in enumerate(matrix):
    print(f"  {labels_short[i]:>4}", end="")
    for val in row:
        print(f"  {val:>6.2f}", end="")
    print()

print("\n  D0 vs D1 → very high (same meaning, different words)")
print("  D0 vs D3 → very low  (completely different topic)")


# ============================================================
# FULL RECAP
# ============================================================

print("\n" + "=" * 60)
print("FULL LECTURE RECAP")
print("=" * 60)
print("""
  Hour 1:
  ├── Tokenization     → split text into words and sentences
  ├── Segmentation     → handle edge cases and subword splits
  ├── Stemming         → chop words to root (fast, rough)
  ├── Normalization    → lowercase, remove noise, fix contractions
  └── Regex            → pattern matching for text cleaning

  Hour 2-3:
  ├── POS Tagging      → label each word's grammar role (Syntax)
  ├── NER Tagging      → find real-world names (Semantics)
  ├── Chunking         → group words into phrases
  ├── Chinking         → exclude words from chunks
  ├── Lemmatization    → smart root finding using dictionary
  └── WordNet          → meaning, synonyms, similarity for machines

  Hour 4:
  ├── Bag of Words     → count-based text to number conversion
  ├── TF-IDF           → smarter weighting by word importance
  ├── Feature Selection→ remove noise, keep what matters
  ├── Word Embeddings  → meaning-aware dense vectors (Word2Vec)
  └── Doc Similarity   → cosine similarity to find related texts

  Pipeline:
  Raw Text → Tokenize → Normalize → POS/NER → BoW/TF-IDF → Model
""")