# setup.py
from setuptools import setup, find_packages

setup(
    name="gpt-commit",
    version="0.1.1",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "gpt-commit-message = scripts.gpt_commit:main",
        ],
    },
)