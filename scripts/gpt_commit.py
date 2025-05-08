#!/usr/bin/env python3
import os
import sys
import subprocess
from openai import OpenAI

def get_staged_changes():
    """Get the staged changes (diff and filenames) in the Git repo."""
    # Get list of staged files
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

    return f"Changed files:\n{files_result.stdout.strip()}\n\nDiff:\n{diff_result.stdout.strip()}"

def generate_commit_message(changes):
    """Generate a commit message using OpenAI GPT."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY is not set.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    prompt = f"""Please analyze these changes and write a conventional commit message.
Follow the format: <type>(<scope>): <description>

Types: feat, fix, docs, style, refactor, test, chore
Scope: optional, what part of the codebase is affected
Description: imperative, present tense, no period at the end

Changes:
{changes}

Only return the commit message, no other explanation."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes conventional commit messages."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error from OpenAI API: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("❌ Error: Missing COMMIT_EDITMSG file path as argument.")
        sys.exit(1)

    commit_msg_file = sys.argv[1]

    # Get staged diff
    changes = get_staged_changes()
    if not changes or changes.strip() == "Changed files:\n\nDiff:":
        print("⚠️  No staged changes found. Skipping commit message generation.")
        sys.exit(0)

    # Generate commit message
    commit_message = generate_commit_message(changes)

    # Write to the commit message file
    try:
        with open(commit_msg_file, "w", encoding="utf-8") as f:
            f.write(commit_message + "\n")
        print(f"✅ Commit message written to {commit_msg_file}")
    except Exception as e:
        print(f"❌ Failed to write commit message: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
