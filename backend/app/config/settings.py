from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parents[3]

# Storage folders
UPLOAD_DIR = BASE_DIR / "backend" / "app" / "uploads"
REPOSITORY_DIR = BASE_DIR / "backend" / "app" / "repositories"

# Create folders automatically
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
REPOSITORY_DIR.mkdir(parents=True, exist_ok=True)

# Embedding model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# Chunking
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200