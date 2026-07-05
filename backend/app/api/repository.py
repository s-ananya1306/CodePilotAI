from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from backend.app.services.repository_service import extract_repository

router = APIRouter()

UPLOAD_DIR = Path("backend/app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_repository(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = extract_repository(file.filename)

    return {
    "filename": file.filename,
    "saved_to": str(file_path),
    "repository_path": result["repository"],
    "files_found": len(result["files"]),
    "processed_files": len(result["processed_files"])
}