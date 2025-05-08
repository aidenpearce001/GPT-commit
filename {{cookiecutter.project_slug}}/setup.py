#!/usr/bin/env python3
import os
import sys
import subprocess
import platform
from pathlib import Path

def check_command_exists(command):
    """Check if a command exists in the system."""
    try:
        subprocess.run([command, '--version'], capture_output=True, check=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def install_uv():
    """Install uv using pip."""
    print("Installing uv...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'uv'], check=True)

def install_dependencies():
    """Install project dependencies using uv or pip."""
    if check_command_exists('uv'):
        print("Using uv for installation...")
        subprocess.run(['uv', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    else:
        print("uv not found, installing uv...")
        install_uv()
        subprocess.run(['uv', 'pip', 'install', '-r', 'requirements.txt'], check=True)

def install_pre_commit_hooks():
    """Install pre-commit hooks."""
    print("Installing pre-commit hooks...")
    subprocess.run(['pre-commit', 'install'], check=True)
    subprocess.run(['pre-commit', 'install', '--hook-type', 'commit-msg'], check=True)

def check_openai_key():
    """Check if OpenAI API key is set."""
    if not os.getenv('OPENAI_API_KEY'):
        print("\nWarning: OpenAI API key is not set!")
        print("Please set your OpenAI API key using:")
        if platform.system() == 'Windows':
            print("set OPENAI_API_KEY=your-api-key-here")
        else:
            print("export OPENAI_API_KEY='your-api-key-here'")

def main():
    """Main setup function."""
    try:
        print("Starting setup...")
        install_dependencies()
        install_pre_commit_hooks()
        check_openai_key()
        print("\nSetup complete! You can now start using the GPT-powered commit message generator.")
    except subprocess.CalledProcessError as e:
        print(f"Error during setup: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
