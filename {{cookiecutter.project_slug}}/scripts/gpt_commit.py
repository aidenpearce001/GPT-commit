#!/usr/bin/env python3
import os
import sys
import subprocess
from openai import OpenAI

def get_staged_changes():
    """Get the staged changes in the repository."""
    # Get the list of staged files
    files_result = subprocess.run(
        ["git", "diff", "--cached", "--name-status"],
        capture_output=True,
        text=True
    )

    # Get the actual diff content
    diff_result = subprocess.run(
        ["git", "diff", "--cached"],
        capture_output=True,
        text=True
    )

    return f"Changed files:\n{files_result.stdout}\n\nDiff:\n{diff_result.stdout}"

def get_unstaged_changes():
    """Get the unstaged changes in the repository."""
    # Get the list of unstaged files
    files_result = subprocess.run(
        ["git", "diff", "--name-status"],
        capture_output=True,
        text=True
    )

    # Get the actual diff content
    diff_result = subprocess.run(
        ["git", "diff"],
        capture_output=True,
        text=True
    )

    return f"Changed files:\n{files_result.stdout}\n\nDiff:\n{diff_result.stdout}"

def generate_commit_message(changes):
    """Generate a commit message using GPT."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Prepare the prompt
    prompt = f"""Please analyze these changes and write a conventional commit message.
    Follow the format: <type>(<scope>): <description>

    Types: feat, fix, docs, style, refactor, test, chore
    Scope: optional, what part of the codebase is affected
    Description: imperative, present tense, no period at the end

    Changes:
    {changes}

    Please provide only the commit message, nothing else."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes conventional commit messages."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating commit message: {str(e)}")
        sys.exit(1)

def main():
    """Main function."""
    try:
        # Check if there are any unstaged changes
        unstaged_changes = get_unstaged_changes()
        if unstaged_changes.strip():
            print("Found unstaged changes. Staging them...")
            # Stage all changes
            subprocess.run(["git", "add", "."], check=True)

        # Get staged changes
        changes = get_staged_changes()
        if not changes.strip():
            print("No changes to commit")
            sys.exit(0)

        # Generate commit message
        commit_message = generate_commit_message(changes)

        # Execute the commit with the generated message
        result = subprocess.run(
            ["git", "commit", "-m", commit_message],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"\nCommit successful with message: {commit_message}")
        else:
            print(f"Error during commit: {result.stderr}")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
