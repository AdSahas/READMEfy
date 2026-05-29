import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import build_file_prompt, build_directory_prompt, build_readme_prompt

load_dotenv()
GROQ_MODEL = "llama-3.3-70b-versatile"
client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"], base_url="https://api.groq.com/openai/v1"
)


def call_llm(prompt, temperature=0.2):
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are a precise software documentation assistant.

Rules:
- Do not invent features.
- Do not hallucinate architecture.
- Only describe functionality supported by the provided code.
- Prefer conservative summaries over speculative ones.
- Pay attention to imports, comments, docstrings, function names, and control flow.
- Ensure that you explain in detail how to run the project, including what .env parameters are needed, any required environment setup, and the steps to execute the application.
- Be detailed in your explanations, providing enough context so that someone reading the documentation can understand the purpose and usage of each component without needing to ask for additional clarification.
                """.strip(),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def summarize_file(file_path, content):
    prompt = build_file_prompt(file_path, content)
    return call_llm(prompt)


def summarize_directories(directory_map):
    directory_summaries = []

    for directory, summaries in directory_map.items():
        prompt = build_directory_prompt(directory, summaries)
        summary = call_llm(prompt)

        if summary:
            directory_summaries.append(
                {"directory": directory, "summary": summary.strip()}
            )

    return directory_summaries


def generate_readme(directory_summaries, directory_tree, project_flow=""):
    prompt = build_readme_prompt(directory_summaries, directory_tree, project_flow)
    return call_llm(prompt, temperature=0.3)
