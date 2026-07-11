import pickle
from pathlib import Path

import faiss
import numpy as np


class FAISSVectorStore:

    def __init__(self, dimension=384):

        self.dimension = dimension

        self.index = faiss.IndexFlatIP(dimension)

        self.metadata = []

    def add(self, embedding, metadata):

        vector = np.array([embedding]).astype("float32")

        self.index.add(vector)

        self.metadata.append(metadata)

    def search(self, embedding, k=5):

        vector = np.array([embedding]).astype("float32")

        scores, indices = self.index.search(vector, k)

        results = []

        for idx, score in zip(indices[0], scores[0]):

            if idx == -1:
                continue

            results.append(
                {
                    "score": float(score),
                    "metadata": self.metadata[idx],
                }
            )

        return results

    def save(self, folder: Path):

        folder.mkdir(parents=True, exist_ok=True)

        faiss.write_index(
            self.index,
            str(folder / "codepilot.faiss"),
        )

        with open(folder / "metadata.pkl", "wb") as f:

            pickle.dump(self.metadata, f)

    def load(self, folder: Path):

        self.index = faiss.read_index(
            str(folder / "codepilot.faiss")
        )

        with open(folder / "metadata.pkl", "rb") as f:

            self.metadata = pickle.load(f)

    def stats(self):

        return {

            "vectors": self.index.ntotal,

            "metadata": len(self.metadata),

        }