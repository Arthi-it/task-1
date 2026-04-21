import math
from collections import Counter

class TFIDFVectorizer:
    def __init__(self):
        self.vocab = {}
        self.idf = {}

    def build_vocab(self, documents):
        vocab_set = set()
        for tokens in documents:
            vocab_set.update(tokens)

        self.vocab = {word: idx for idx, word in enumerate(vocab_set)}

    def compute_tf(self, tokens):
        tf = Counter(tokens)
        total = len(tokens)
        return {word: count / total for word, count in tf.items()}

    def compute_idf(self, documents):
        N = len(documents)
        df = Counter()

        for tokens in documents:
            unique_words = set(tokens)
            for word in unique_words:
                df[word] += 1

        self.idf = {word: math.log(N / (df[word] + 1)) for word in df}

    def transform(self, tokens):
        tf = self.compute_tf(tokens)
        vector = [0] * len(self.vocab)

        for word, val in tf.items():
            if word in self.vocab:
                vector[self.vocab[word]] = val * self.idf.get(word, 0)

        return vector