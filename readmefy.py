from scanner import scan_files, build_directory_tree
from summarizer import summarize_files, group_by_directories
from llm import summarize_directories, generate_readme


def main():

    root_dir = input("Repository path: ").strip()
    print("Please answer these optional questions. It will help the LLM generate a more accurate README.")
    entrypoint = input("Main entrypoint file (optional): ").strip()
    project_flow = input("Project flow / purpose (optional): ").strip()

    print("\nScanning repository...")
    files = scan_files(root_dir)

    print(f"Found {len(files)} files.")

    print("\nBuilding directory tree...")
    directory_tree = build_directory_tree(root_dir)

    print("\nSummarizing files...")
    file_summaries = summarize_files(files)

    print(f"Generated {len(file_summaries)} file summaries.")

    print("\nGrouping directories...")
    directory_map = group_by_directories(file_summaries)

    print("\nSummarizing directories...")
    directory_summaries = summarize_directories(directory_map)

    if entrypoint:
        directory_summaries.append({
            "directory": "ENTRYPOINT",
            "summary": f"The main executable entrypoint of the project is `{entrypoint}`."
        })

    print("\nGenerating README...")
    readme = generate_readme(
        directory_summaries,
        directory_tree,
        project_flow
    )

    output_path = f"{root_dir}/README.generated.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme)

    print("\nREADME generated:")
    print(output_path)


if __name__ == "__main__":
    main()