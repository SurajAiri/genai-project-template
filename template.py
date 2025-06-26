from pathlib import Path

def create_genai_project_structure(base_dir: Path):
    """
    Create a GenAI project structure using cookiecutter template variables.
    Only creates files/directories if they don't already exist.
    """
    
    directories = [
        "{{cookiecutter.repo_name}}/configs",
        "{{cookiecutter.repo_name}}/docs", 
        "{{cookiecutter.repo_name}}/src/prompts",
        "{{cookiecutter.repo_name}}/src/agents",
        "{{cookiecutter.repo_name}}/src/chains",
        "{{cookiecutter.repo_name}}/src/tools",
        "{{cookiecutter.repo_name}}/src/memory",
        "{{cookiecutter.repo_name}}/src/utils",
        "{{cookiecutter.repo_name}}/scripts",
        "{{cookiecutter.repo_name}}/tests",
        "{{cookiecutter.repo_name}}/logs",
    ]
    
    files = {
        "{{cookiecutter.repo_name}}/LICENSE": "",
"{{cookiecutter.repo_name}}/AUTHORS.rst": "Authors\n=======\n\n* {{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}",
        "{{cookiecutter.repo_name}}/.gitignore": "",
        "{{cookiecutter.repo_name}}/.env.example": "",
        "{{cookiecutter.repo_name}}/ruff.toml": "",
        "{{cookiecutter.repo_name}}/README.md": "# {{cookiecutter.repo_name}}\n\n{{cookiecutter.description}}",
        "{{cookiecutter.repo_name}}/pyproject.toml": "",
        "{{cookiecutter.repo_name}}/src/__init__.py": "",
        "{{cookiecutter.repo_name}}/src/main.py": "# Entry point",
        "{{cookiecutter.repo_name}}/src/prompts/__init__.py": "",
        "{{cookiecutter.repo_name}}/src/agents/__init__.py": "",
        "{{cookiecutter.repo_name}}/src/chains/__init__.py": "",
        "{{cookiecutter.repo_name}}/src/tools/__init__.py": "",
        "{{cookiecutter.repo_name}}/src/memory/__init__.py": "",
        "{{cookiecutter.repo_name}}/src/utils/__init__.py": "",
        "{{cookiecutter.repo_name}}/configs/config.yaml": "# Configuration file",
        "{{cookiecutter.repo_name}}/scripts/__init__.py": "",
        "{{cookiecutter.repo_name}}/tests/__init__.py": "",
        "{{cookiecutter.repo_name}}/docs/architecture.md": "# {{cookiecutter.repo_name}} Architecture",
    }
    
    # Create directories
    for directory in directories:
        dir_path = base_dir / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {directory}")
    
    # Create files only if they don't exist
    for file_path, content in files.items():
        full_path = base_dir / file_path
        if not full_path.exists():
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding='utf-8')
            print(f"Created file: {file_path}")
        else:
            print(f"Skipped existing file: {file_path}")
    
    # Add .gitkeep to empty directories
    add_gitkeep_to_empty_dirs(base_dir, directories)

def add_gitkeep_to_empty_dirs(base_dir: Path, directories: list):
    """Add .gitkeep files to empty directories to ensure they're tracked by git."""
    for directory in directories:
        dir_path = base_dir / directory
        if dir_path.exists() and not any(dir_path.iterdir()):
            gitkeep_path = dir_path / ".gitkeep"
            gitkeep_path.write_text("", encoding='utf-8')
            print(f"Added .gitkeep to empty directory: {directory}")

if __name__ == "__main__":
    base_path = Path(".")
    create_genai_project_structure(base_path)
    print("\n✅ GenAI project structure created successfully!")