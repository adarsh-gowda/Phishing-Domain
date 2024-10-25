import setuptools
"""
This imports the setuptools library, which is the standard library used for packaging Python projects. 
It provides tools to create, distribute, and install Python packages.
"""


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
"""
Opens the README.md file (which usually contains a detailed description of the project) in read mode and stores its content 
in the long_description variable. This file is typically used to provide information to the users when they visit the 
project on platforms like GitHub or PyPI (Python Package Index).
The encoding="utf-8" ensures that the file is read correctly, especially if it contains non-ASCII characters
"""


__version__ = "0.0.0"

"""Sets the initial version of the project. This can be incremented following semantic versioning (e.g., 0.0.1, 1.0.0, etc.)."""


REPO_NAME = "phishing_domain"
AUTHOR_USER_NAME = "adarsh-gowda"
SRC_REPO = "phishingdomain"
AUTHOR_EMAIL = "adarshgowda2711@gmail.com"

"""These are variables for essential project details:
REPO_NAME: The name of the GitHub repository.
AUTHOR_USER_NAME: The author's GitHub username.
SRC_REPO: The name of the source code directory where the package code resides.
AUTHOR_EMAIL: The author's contact email.
"""


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for phishing domain app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


"""name=SRC_REPO: The name of the Python package (phishingdomain).
version=__version__: The current version of the package (0.0.0 in this case).
author and author_email: The author's name and email.
description: A short description of what the package is for, in this case, "A small python package for phishing domain app."
long_description: The content of the README.md file is passed here, so it gets displayed as a detailed description on platforms like PyPI.
long_description_content="text/markdown": Specifies the format of the long_description as Markdown.
url: The homepage URL of the project, which is usually the GitHub repository.
project_urls: Additional URLs related to the project. Here, a "Bug Tracker" URL is provided, 
which points to the repository's issues page on GitHub.
package_dir={"": "src"}: Specifies the source directory for the packages. In this case, the code is located in the src directory.
packages=setuptools.find_packages(where="src"): This automatically finds all packages inside the src directory,
                                                  making sure they are included in the distribution."""