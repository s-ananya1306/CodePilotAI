from pathlib import Path

from backend.app.embeddings.embedding_service import embedding_service
from backend.app.vectorstore.faiss_service import FAISSVectorStore

store = FAISSVectorStore()

text = "FastAPI is a backend framework."

embedding = embedding_service.embed_text(text)

store.add(
    embedding,
    {
        "file": "main.py",
        "content": text,
    },
)

print(store.stats())

results = store.search(embedding)

print(results)

store.save(
    Path("backend/app/storage/indexes")
)

print("Index saved successfully.")