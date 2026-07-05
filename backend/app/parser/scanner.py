from pathlib import Path

# Folders to ignore
IGNORE_DIRS = {
    ".git",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
    ".pytest_cache"
}

# Supported file extensions
SUPPORTED_EXTENSIONS = {
    ".py",
    ".java",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".cpp",
    ".c",
    ".cs",
    ".go",
    ".rs",
    ".html",
    ".css",
    ".json",
    ".yaml",
    ".yml",
    ".md"
}


def scan_repository(repository_path: Path):
    """
    Scan repository recursively and return supported files.
    """

    files = []

    for path in repository_path.rglob("*"):

        if path.is_dir():
            continue

        # Ignore folders
        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        # Ignore unsupported extensions
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        files.append({
            "name": path.name,
            "extension": path.suffix,
            "path": str(path),
            "size": path.stat().st_size
        })

    return files