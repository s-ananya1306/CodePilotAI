from backend.app.embeddings.embedding_service import embedding_service

text = """
FastAPI is an excellent backend framework.
"""

embedding = embedding_service.embed_text(text)

print("Embedding Length:", len(embedding))

print(
    embedding[:10]
)

print(
    embedding_service.model_info()
)