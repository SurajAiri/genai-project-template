from pathlib import Path

def create_genai_project_structure(base_dir: Path):
    """
    Create a GenAI project structure using cookiecutter template variables.
    Only creates files/directories if they don't already exist.
    """
    
    directories = [
        "{{cookiecutter.project_slug}}/configs",
        "{{cookiecutter.project_slug}}/docs", 
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/prompts",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/agents",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/chains",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/tools",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/memory",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/utils",
        "{{cookiecutter.project_slug}}/scripts",
        "{{cookiecutter.project_slug}}/tests",
        "{{cookiecutter.project_slug}}/logs",
    ]
    
    files = {
        "{{cookiecutter.project_slug}}/LICENSE": "",
"{{cookiecutter.project_slug}}/AUTHORS.rst": "Authors\n=======\n\n* {{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}",
        "{{cookiecutter.project_slug}}/.gitignore": "",
        "{{cookiecutter.project_slug}}/.env.example": "",
        "{{cookiecutter.project_slug}}/ruff.toml": "",
        "{{cookiecutter.project_slug}}/README.md": "# {{cookiecutter.project_slug}}\n\n{{cookiecutter.description}}",
        "{{cookiecutter.project_slug}}/pyproject.toml": "",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/__init__.py": "",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/main.py": "# Entry point",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/prompts/__init__.py": "",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/agents/__init__.py": "",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/chains/__init__.py": "",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/tools/__init__.py": "",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/memory/__init__.py": "",
        "{{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/utils/__init__.py": "",
        "{{cookiecutter.project_slug}}/configs/config.yaml": "# Configuration file",
        "{{cookiecutter.project_slug}}/scripts/__init__.py": "",
        "{{cookiecutter.project_slug}}/tests/__init__.py": "",
        "{{cookiecutter.project_slug}}/docs/architecture.md": "# {{cookiecutter.project_slug}} Architecture",
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