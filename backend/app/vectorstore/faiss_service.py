import faiss
import numpy as np


class FAISSVectorStore:

    def __init__(self, dimension=384):

        self.index = faiss.IndexFlatIP(dimension)

        self.documents = []

    def add(self, embedding, metadata):

        vector = np.array([embedding]).astype("float32")

        self.index.add(vector)

        self.documents.append(metadata)

    def search(self, embedding, k=5):

        vector = np.array([embedding]).astype("float32")

        scores, indices = self.index.search(vector, k)

        results = []

        for idx, score in zip(indices[0], scores[0]):

            if idx == -1:
                continue

            results.append({

                "score": float(score),

                "metadata": self.documents[idx]

            })

        return results