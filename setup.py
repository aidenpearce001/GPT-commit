# setup.py
from setuptools import setup, find_packages

setup(
    name="gpt-commit",
    version="0.0.1",               # bump for each release
    python_requires=">=3.10",
    packages=find_packages(),      # will pick up scripts/
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "gpt-commit-message = scripts.gpt_commit:main",
        ],
    },
)
