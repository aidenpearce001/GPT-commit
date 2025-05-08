# GPT-Powered Commit Message Generator

A cookiecutter template that adds GPT-powered commit messages to any repository.

## Quick Start

### For New Projects

1. Install cookiecutter:
```bash
pip install cookiecutter
```

2. Create a new project with GPT commit support:
```bash
cookiecutter https://github.com/yourusername/gpt-commit-cookiecutter
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

4. That's it! Now you can use `gptcommit` instead of `git commit`:
```bash
git add .  # Stage your changes
gptcommit  # Let GPT generate and commit with an appropriate message
```

### For Existing Repositories

1. Install cookiecutter:
```bash
pip install cookiecutter
```

2. Run cookiecutter in your repository:
```bash
cd /path/to/your/repo
cookiecutter https://github.com/yourusername/gpt-commit-cookiecutter --directory . --no-input
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

4. That's it! Now you can use `gptcommit` instead of `git commit`.

## Features

- GPT-powered commit messages
- Automatic conventional commit format
- Cross-platform support (Windows, Linux, macOS)

## Requirements

- Python 3.9+
- OpenAI API key
- Git

## License

MIT
