from pathlib import Path
import zipfile
import shutil

from backend.app.parser.scanner import scan_repository
from backend.app.services.code_processing_service import process_repository

from backend.app.config.settings import (
    UPLOAD_DIR,
    REPOSITORY_DIR,
)
REPOSITORY_DIR = Path("backend/app/repositories")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
REPOSITORY_DIR.mkdir(parents=True, exist_ok=True)


def extract_repository(zip_filename: str):

    zip_path = UPLOAD_DIR / zip_filename

    extract_folder = REPOSITORY_DIR / zip_filename.replace(".zip", "")

    if extract_folder.exists():
        shutil.rmtree(extract_folder)

    extract_folder.mkdir(parents=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_folder)

    files = scan_repository(extract_folder)

    processed_files = process_repository(files)

    return {
        "repository": str(extract_folder),
        "files": files,
        "processed_files": processed_files
    }