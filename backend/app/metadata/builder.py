"""
Metadata Builder

Creates structured metadata for every code chunk.
"""

from pathlib import Path


def build_metadata(
    repository_name: str,
    file_path: Path,
    language: str,
    chunk_id: int,
    chunk: str,
):

    return {

        "repository": repository_name,

        "file_name": file_path.name,

        "relative_path": str(file_path),

        "language": language,

        "chunk_id": chunk_id,

        "content": chunk,

    }