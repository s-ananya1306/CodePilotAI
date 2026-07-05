from backend.app.embeddings.embedding_service import generate_embedding
from backend.app.vectorstore.faiss_service import FAISSVectorStore

vector_store = FAISSVectorStore()


def build_index(processed_files):

    total_chunks = 0

    for file in processed_files:

        for chunk in file["chunks"]:

            embedding = generate_embedding(chunk)

            metadata = {

                "file": file["name"],

                "language": file["language"],

                "content": chunk

            }

            vector_store.add(
                embedding,
                metadata
            )

            total_chunks += 1

    return total_chunks