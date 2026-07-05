from pathlib import Path

from backend.app.parser.file_reader import read_file
from backend.app.parser.chunker import chunk_text
from backend.app.parser.language_detector import detect_language


def process_repository(files):

    processed_files = []

    for file in files:

        file_path = Path(file["path"])

        language = detect_language(file_path)

        content = read_file(file_path)

        if content is None:
            continue

        chunks = chunk_text(content)

        print(
            f"{file['name']} -> {language} -> {len(chunks)} chunks"
        )

        processed_files.append(
            {
                "name": file["name"],
                "language": language,
                "chunks": chunks,
                "chunk_count": len(chunks),
            }
        )

    return processed_files