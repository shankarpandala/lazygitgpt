from setuptools import setup, find_packages

# Define the package version
version = "0.0.5-beta"

# Define the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Call the setup function
setup(
    name="lazygitgpt",  # Name of the package
    version=version,
    author="Shankar Pandala",  # Replace with your name
    author_email="shankar@ssbm.ch",  # Replace with your email
    description="A tool to manage git repositories using GPT-4.",  # Short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shankarpandala/lazygitgpt",  # Replace with your repository URL
    project_urls={
        "Bug Tracker": "https://github.com/shankarpandala/lazygitgpt/issues",
    },
    classifiers=[  # Optional metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your choice of license
        "Operating System :: OS Independent",
    ],
    package_dir={"": "lazygitgpt"},  # Where to find the source code
    packages=find_packages(where="lazygitgpt"),
    python_requires=">=3.6",  # Minimum version requirement of Python
    install_requires=[  # List of dependencies
        "gitpython>=3.1.0",  # Example, specify actual dependencies
        "openai>=0.10.0"    # For GPT-4 integration
    ],
    entry_points={
        "console_scripts": [
            "lazygitgpt=lazygitgpt.cli:main",  # Linking the CLI script
        ],
    },
)
