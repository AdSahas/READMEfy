MAX_WORKERS = 2  #  Max number of concurrent workers (adjust to rate-limit GROQ calls and avoid being blocked)
MAX_FILE_LENGTH = 4000  # max length of a file to be processed
MODEL = "llama-3.3-70b-versatile"  #  use this model for the LLM
TEMPERATURE = (
    0.2  #  temperature for the LLM - lower values for more deterministic outputs
)

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".idea",
    ".vscode",
}

# files to ignore
IGNORE_FILES = {
    ".DS_Store",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    ".env",
}


#  the file extensions that the application will process
ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".html",
    ".css",
    ".json",
    ".md",
    ".yml",
    ".yaml",
    ".toml",
    ".txt",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".swift",
    ".kt",
    ".kts",
    ".sh",
    ".bash",
    ".zsh",
    ".sql",
}

#  patterns and hints for detecting environment variables
ENV_VAR_PATTERN = r"\b[A-Z][A-Z0-9_]{2,}\b"
ENV_HINTS = [
    "env",
    "dotenv",
    "environment",
    "process.env",
    "os.environ",
    "getenv",
]
