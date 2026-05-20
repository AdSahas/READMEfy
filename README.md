# Project Overview
This project is designed to automatically generate software documentation using a large language model (LLM) provided by the Groq API. The primary goal is to streamline the process of creating informative project documentation by scanning directory trees, detecting environment variables, generating prompts, and summarizing file contents.

## Project Structure and Layout
The project consists of the following key files and directories:
* `scanner.py`: responsible for scanning directory trees
* `llm.py`: interacts with the Groq API to utilize the large language model
* `prompts.py`: generates prompts for the LLM
* `readmefy.py`: the main executable entrypoint of the project
* `summarizer.py`: summarizes file contents
* `config.py`: contains configuration settings
* `requirements.txt`: lists dependencies required by the project

## Key Components
The project relies on the following key components:
* Groq API: provides the large language model used for generating documentation
* OpenAI's API: utilized by the Groq API
* `httpx` and `pydantic` libraries: external dependencies required by the project

## How the Project Works
The project works by:
1. Scanning directory trees using `scanner.py`
2. Detecting environment variables and generating prompts using `prompts.py`
3. Utilizing the Groq API to generate precise software documentation
4. Summarizing file contents using `summarizer.py`
5. Combining the results to create a comprehensive README file

## Setup Requirements
To set up the project, the following environment variables and configuration settings are required:
* Setup a .env with `GROQ_API_KEY=your_key_here`
* Configuration settings defined in `config.py`
* Dependencies specified in `requirements.txt`

## How to Use the Project
To use the project, follow these steps:
1. Install the required dependencies listed in `requirements.txt`
2. Set up the environment variables, including `GROQ_API_KEY`
3. Configure the settings in `config.py`
4. Run the project using the `readmefy.py` entrypoint
5. The project will generate a README file based on the scanned directory tree and detected environment variables

## Notes
1. This project is still in an MVP version. Optimizations will be released in the future
2. LLMs make mistakes - verify generated README for accuracy and correctness. 
