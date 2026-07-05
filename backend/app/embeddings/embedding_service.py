"""
Embedding Service

Loads the embedding model once during application startup
and provides methods to generate embeddings.
"""

from sentence_transformers import SentenceTransformer
from backend.app.config.settings import EMBEDDING_MODEL


class EmbeddingService:
    def __init__(self):
        print("Loading embedding model...")

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print("Embedding model loaded successfully.")

    def embed_text(self, text: str):
        return self.model.encode(
            text,
            normalize_embeddings=True
        )

    def embed_batch(self, texts):
        return self.model.encode(
            texts,
            normalize_embeddings=True
        )

    def model_info(self):
        return {
            "model": EMBEDDING_MODEL,
            "dimension": self.model.get_embedding_dimension()
        }


embedding_service = EmbeddingService()