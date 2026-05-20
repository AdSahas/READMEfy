def build_file_prompt(file_path, content):

    return f"""
You are analyzing a single source-code file for automatic README generation.

Your task:
Write exactly TWO sentences summarizing this file.

Rules that you MUST FOLLOW:
- Sentence 1: explain the file's main purpose.
- Sentence 2: explain how this file contributes to the larger project.
- Focus on purpose, dependencies, configuration, and project role.
- Ignore low-level implementation details unless they affect setup, execution, or architecture.
- Pay attention to imports, comments, docstrings, function names, class names, constants, and control flow.
- Identify external services, SDKs, frameworks, APIs, databases, CLIs, or runtime tools used by this file.
- Explicitly mention required environment variables, config files, credentials, or setup assumptions if the code shows them.
- If the code uses an OpenAI-compatible client with a non-OpenAI base URL, describe the actual provider when visible.
- Do not invent functionality that is not present.
- Do not guess setup requirements unless the code strongly supports them.

File path:
{file_path}

File content:
{content}

Summary:
""".strip()


def build_directory_prompt(directory, file_summaries):

    joined_summaries = "\n".join(file_summaries)

    return f"""
You are summarizing a software project directory for automatic README generation.

Directory:
{directory}

File summaries:
{joined_summaries}

Write a short explanation of the purpose of this directory.

Rules:
- Write 2 to 4 sentences.
- Focus on this directory's architectural responsibility.
- Explain how the files in this directory work together.
- Mention important frameworks, services, APIs, databases, CLIs, or configuration requirements if they appear in the file summaries.
- Preserve concrete setup details from the file summaries, such as environment variables or required config files.
- Do not invent functionality that is not supported by the summaries.
- Avoid vague phrases like "collaborates with other files" unless you explain how.

Directory summary:
""".strip()


def build_readme_prompt(directory_summaries, directory_tree, project_flow=""):

    summaries_text = ""

    for item in directory_summaries:
        summaries_text += f"{item['directory']} : {item['summary']}\n"

    return f"""
Generate a README for this project.

Directory summaries:
{summaries_text}

Directory tree:
{directory_tree}

User-provided project flow / purpose:
{project_flow}

The README should include:
- Project overview
- Project structure and layout
- Key components
- How the project works
- Setup requirements
- How to use the project

Rules:
- Write in clean markdown.
- Be concise but useful.
- Explain the operational flow clearly.
- Prefer concrete explanations over vague statements.
- Mention detected frameworks, SDKs, databases, APIs, CLIs, and external services.
- Mention detected environment variables, config files, credentials, or setup requirements.
- If the project uses an OpenAI-compatible client with another provider, name the actual provider if the summaries show it.
- Do not invent features.
- Do not mention files or folders that are not shown.
- Do not fabricate installation commands unless dependency files or summaries support them.
- If setup requirements are partially unclear, say what is known and what must be configured by the user.

README:
""".strip()