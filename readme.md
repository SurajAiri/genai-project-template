# GenAI Project Template

A comprehensive cookiecutter template for building modern GenAI applications with LangChain, LangGraph, and Python best practices.

## 🚀 Features

- **Modern Python Setup**: Uses `uv` for fast dependency management and `ruff` for linting/formatting
- **Modular Architecture**: Clean separation of agents, chains, tools, memory, and utilities
- **GenAI Ready**: Pre-configured structure for LangChain/LangGraph applications
- **Best Practices**: Includes testing, documentation, and development tools
- **Flexible Configuration**: YAML-based configuration with environment variable support
- **Production Ready**: Docker support and proper logging setup

## 📁 Project Structure

```
your-project/
├── .env.example              # Environment variables template
├── .gitignore               # Git ignore patterns
├── LICENSE                  # Project license
├── AUTHORS.rst             # Project contributors
├── README.md               # Project documentation
├── pyproject.toml          # Dependencies and project metadata
├── ruff.toml              # Code formatting and linting config
├── configs/
│   └── config.yaml        # Application configuration
├── docs/
│   └── architecture.md    # Detailed architecture documentation
├── src/
│   ├── main.py           # Application entry point
│   ├── agents/           # AI agent implementations
│   ├── chains/           # Processing chains and workflows
│   ├── tools/            # Custom tools and integrations
│   ├── memory/           # Memory and context management
│   ├── prompts/          # Prompt template management
│   └── utils/            # Utility functions
├── scripts/              # Automation scripts
├── tests/               # Test suite
├── playground/           # code playground
└── logs/                # Application logs
```

## 🛠 Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for dependency management
- [cookiecutter](https://github.com/cookiecutter/cookiecutter) for template generation

## 🚀 Quick Start

### 1. Install cookiecutter

```bash
pip install cookiecutter
```

### 2. Generate your project

```bash
cookiecutter https://github.com/your-username/genai-project-template.git
```

### 3. Configure your project

You'll be prompted to provide:

- `project_name`: Your project name (e.g., "My GenAI Assistant")
- `project_slug`: URL-friendly version (auto-generated)
- `description`: Brief project description
- `author_name`: Your name
- `author_email`: Your email
- `version`: Initial version (default: 0.0.1)
- `license`: License type (default: MIT)
- `python_version`: Python version (default: 3.12)

### 4. Setup your new project

```bash
cd your-project-name
cp .env.example .env
# Edit .env with your API keys and configuration
```

### 5. Install dependencies

```bash
uv sync
```

### 6. Run your application

```bash
uv run python {{cookiecutter.module_name}}
```

## 📖 Architecture Overview

The generated project follows a modular architecture designed for GenAI applications:

### Core Components

- [**Agents**]({{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/agents/): AI agents that orchestrate conversations and workflows
- [**Chains**]({{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/chains/): Sequential processing pipelines for specific tasks
- [**Tools**]({{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/tools/): External integrations and custom functionality
- [**Memory**]({{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/memory/): Conversation history and context management
- [**Prompts**]({{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/prompts/): Centralized prompt template management
- [**Utils**]({{cookiecutter.project_slug}}/src/{{cookiecutter.module_name}}/utils/): Common utilities and helper functions

### Key Features

- **Async Support**: Built for asynchronous processing
- **Configuration Management**: YAML-based configuration with environment variables
- **Logging**: Structured logging with configurable levels
- **Testing**: pytest-based testing with async support
- **Code Quality**: Automated formatting and linting with ruff

For detailed architecture information, see the generated [`docs/architecture.md`]({{cookiecutter.project_slug}}/docs/architecture.md).

## 🔧 Development Tools

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Fix linting issues
uv run ruff check --fix
```

### Testing

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 TODO / Roadmap

- [ ] Add LangGraph integration templates
- [ ] Include MCP (Model Context Protocol) server templates
- [ ] Add vector database integration options
- [ ] Include Streamlit/FastAPI web interface templates
- [ ] Add monitoring and observability tools
- [ ] Include deployment templates (Docker Compose, Kubernetes)
- [ ] Add more example agents and chains
- [ ] Include prompt engineering utilities

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **Suraj Airi** - [surajairi.ml@gmail.com](mailto:surajairi.ml@gmail.com)

## 🙏 Acknowledgments

- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) for the templating framework
- [LangChain](https://github.com/langchain-ai/langchain) for the GenAI framework
- [uv](https://github.com/astral-sh/uv) for fast Python package management
- [Ruff](https://github.com/astral-sh/ruff) for Python linting and formatting

## 📞 Support

If you encounter any issues or have questions:

1. Search existing [issues](https://github.com/SurajAiri/genai-project-template/issues)
2. Create a new issue with detailed information

---

⭐ **Star this repository if you find it helpful!**
