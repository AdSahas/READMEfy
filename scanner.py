import os
import re
from config import (
    IGNORE_DIRS,
    IGNORE_FILES,
    ALLOWED_EXTENSIONS,
    ENV_VAR_PATTERN,
    ENV_HINTS,
)


# directories to ignore
def should_ignore_dir(dirname):
    return dirname in IGNORE_DIRS


# files to ignore
def should_ignore_file(filename):
    if filename in IGNORE_FILES:
        return True

    unused, ext = os.path.splitext(filename)
    return ext not in ALLOWED_EXTENSIONS


def scan_files(root_dir):
    files = []

    for current_dir, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not should_ignore_dir(d)]

        for filename in filenames:
            if should_ignore_file(filename):
                continue

            file_path = os.path.join(current_dir, filename)
            files.append(file_path)

    return files


def build_directory_tree(root_dir):
    lines = []

    for current_dir, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not should_ignore_dir(d)]
        level = current_dir.replace(root_dir, "").count(os.sep)
        indent = "  " * level
        dirname = os.path.basename(current_dir)

        if level == 0:
            lines.append(f"{dirname}/")
        else:
            lines.append(f"{indent}{dirname}/")
        file_indent = "  " * (level + 1)

        for filename in filenames:
            if should_ignore_file(filename):
                continue

            lines.append(f"{file_indent}{filename}")

    return "\n".join(lines)


def line_mentions_env(line):
    lower = line.lower()
    for hint in ENV_HINTS:
        if hint in lower:
            return True

    return False


def detect_env_vars(files):
    env_vars = set()

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()

        except Exception:
            continue

        filename = os.path.basename(file_path)
        for line in lines:
            if filename.startswith(".env"):
                matches = re.findall(ENV_VAR_PATTERN, line)
                env_vars.update(matches)
                continue

            if not line_mentions_env(line):
                continue

            matches = re.findall(ENV_VAR_PATTERN, line)
            env_vars.update(matches)

    return sorted(env_vars)
