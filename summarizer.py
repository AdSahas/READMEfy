import os
from concurrent.futures import ThreadPoolExecutor
from llm import summarize_file
from config import MAX_WORKERS

MAX_FILE_LENGTH = 4000


def read_file(file_path, max_length=MAX_FILE_LENGTH):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read(max_length)

    except Exception:
        return ""


def summarize_single_file(file_path):
    content = read_file(file_path)
    if not content:
        return None

    summary = summarize_file(file_path, content)
    if not summary:
        return None

    return {"file": file_path, "summary": summary.strip()}


def summarize_files(files):
    if not files:
        return []

    max_workers = min(MAX_WORKERS, len(files))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(summarize_single_file, files)

    return [r for r in results if r]


def group_by_directories(file_summaries):
    directory_map = {}

    for item in file_summaries:
        directory = os.path.dirname(item["file"])

        if directory not in directory_map:
            directory_map[directory] = []

        directory_map[directory].append(
            f"{os.path.basename(item['file'])}: {item['summary']}"
        )

    return directory_map
