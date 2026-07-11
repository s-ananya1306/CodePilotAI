from pathlib import Path

from backend.app.services.repository_indexer import RepositoryIndexer

indexer = RepositoryIndexer()

result = indexer.build(
    Path("backend/app/repositories/final_ai2thor")
)

print(result)