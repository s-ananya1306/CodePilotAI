from sentence_transformers import SentenceTransformer
from backend.app.config.settings import EMBEDDING_MODEL

# Load once when the application starts
model = SentenceTransformer(EMBEDDING_MODEL)


def generate_embedding(text: str):
    """
    Generate embedding for a text chunk.
    """
    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding