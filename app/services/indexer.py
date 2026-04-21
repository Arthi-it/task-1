from app.utils.file_loader import load_documents
from app.services.processor import preprocess
from app.services.vectorizer import TFIDFVectorizer

class Indexer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.vectorizer = TFIDFVectorizer()
        self.doc_vectors = {}
        self.raw_docs = {}

    def build_index(self):
        self.raw_docs = load_documents(self.folder_path)

        tokenized_docs = [preprocess(text) for text in self.raw_docs.values()]

        self.vectorizer.build_vocab(tokenized_docs)
        self.vectorizer.compute_idf(tokenized_docs)

        for filename, text in self.raw_docs.items():
            tokens = preprocess(text)
            self.doc_vectors[filename] = self.vectorizer.transform(tokens)