import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME ="Chicken-disease-classification-deeplearining-projects"
AUTHOR_USER_NAME ="ganeshkukreja31"
SRC_REPO = "Chicken Disease classification"
AUTHOR_EMAIL="kukreja.g@northeastern.edu"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small amount of python package for Chicken disease classification",
    long_description=long_description,
    long_description_content="text/arkdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)