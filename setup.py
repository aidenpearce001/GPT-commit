from setuptools import setup, find_packages

setup(
    name="gpt-commit",              # choose your package name
    version="0.1.0",
    packages=find_packages(),       # will pick up your scripts/ folder
    install_requires=[
        "openai>=0.27.0",           # whatever minimum you need
    ],
    entry_points={
        "console_scripts": [
            "gpt-commit-message = scripts.gpt_commit:main",
        ]
    }
)
