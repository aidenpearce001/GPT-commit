# GPT-Powered Commit Message Generator

This cookiecutter template helps you set up a project with GPT-powered commit messages.

## Features

- Pre-commit hooks for code quality
- GPT-powered commit message generation
- Cross-platform support (Windows, Linux, macOS)

## Quick Start

1. Install cookiecutter:
```bash
pip install cookiecutter
```

2. Create a new project:
```bash
cookiecutter https://github.com/yourusername/gpt-commit-cookiecutter
```

3. Follow the prompts to configure your project.

4. Set up your OpenAI API key:
```bash
# Linux/macOS
export OPENAI_API_KEY='your-api-key-here'

# Windows
set OPENAI_API_KEY=your-api-key-here
```

5. Install dependencies using uv (recommended) or pip:
```bash
# Install uv
pip install uv

# Install dependencies
uv pip install -r requirements.txt
```

6. Make the GPT commit script executable:
```bash
chmod +x scripts/gptcommit
```

7. Add the scripts directory to your PATH or create a symlink:
```bash
# Option 1: Add to PATH (add this to your .bashrc or .zshrc)
export PATH=$PATH:/path/to/your/project/scripts

# Option 2: Create a symlink
ln -s /path/to/your/project/scripts/gptcommit /usr/local/bin/gptcommit
```

## Usage

Instead of using `git commit -m "message"`, simply stage your changes and run:

```bash
git add .  # Stage your changes
gptcommit  # Let GPT generate and commit with an appropriate message
```

The script will:
1. Analyze your staged changes
2. Generate an appropriate conventional commit message using GPT
3. Create the commit with the generated message

## Requirements

- Python 3.9+
- OpenAI API key
- Git

## Development

If you're developing this template:

1. Clone the repository
2. Install dependencies:
```bash
pip install -e .
```

3. Make your changes
4. Test the changes by creating a new project:
```bash
cookiecutter .
```

## License

MIT
