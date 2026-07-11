"""
Repository Index Builder

Builds a FAISS index for an entire repository.
"""

from pathlib import Path

from backend.app.parser.scanner import scan_repository
from backend.app.parser.file_reader import read_file
from backend.app.parser.chunker import chunk_text
from backend.app.parser.language_detector import detect_language

from backend.app.metadata.builder import build_metadata

from backend.app.embeddings.embedding_service import embedding_service
from backend.app.vectorstore.faiss_service import FAISSVectorStore


class RepositoryIndexer:

    def __init__(self):

        self.store = FAISSVectorStore()

    def build(self, repository_path: Path):

        repository_name = repository_path.name

        files = scan_repository(repository_path)

        total_chunks = 0

        for file in files:

            file_path = Path(file["path"])

            language = detect_language(file_path)

            content = read_file(file_path)

            if content is None:
                continue

            chunks = chunk_text(content)

            for chunk_id, chunk in enumerate(chunks):

                embedding = embedding_service.embed_text(chunk)

                metadata = build_metadata(
                    repository_name,
                    file_path,
                    language,
                    chunk_id,
                    chunk,
                )

                self.store.add(
                    embedding,
                    metadata,
                )

                total_chunks += 1

        return {

            "repository": repository_name,

            "files": len(files),

            "chunks": total_chunks,

            "vectors": self.store.stats()["vectors"],
        }