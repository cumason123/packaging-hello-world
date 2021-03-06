from importlib.metadata import version
from git import Repo
import os


# FORMAT: 1.x.x
_LOCAL_PYPI_VERSION="1.0.5"

def createTag():
    # metadata.version only works on python3.8
    # Make sure to install most updated version of package 
    pypi_version = version('cumason123-helloworld')


    # Check pypi and local package version match
    if _LOCAL_PYPI_VERSION == pypi_version:
        # Create tag
        repo = Repo(os.getcwd())
        repo.create_tag(_LOCAL_PYPI_VERSION)

        # Push tag to origin master
        origin = repo.remote()
        origin.push(_LOCAL_PYPI_VERSION)
    else:
        # PyPI publish likely failed
        exit(1)


if __name__ == '__main__':
    createTag()
