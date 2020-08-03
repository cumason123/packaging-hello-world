from importlib.metadata import version
from git import Repo
import os


_PACKAGE_PYPI_VERSION="1.0.0"

def createTag():
    # version function only works on python3.8
    # this pypi_version should be the most updated version. github workflow
    # isntalls most updated package
    pypi_version = version('cumason-helloworld-package')

    if _PACKAGE_PYPI_VERSION == pypi_version:
        # Create tag and push tag to master
        repo = Repo(os.getcwd())
        repo.create_tag(_PACKAGE_PYPI_VERSION)
        repo.remote().push(_PACKAGE_PYPI_VERSION)
    else:
        # PyPI publish likely failed
        exit(1)


if __name__ == '__main__':
    createTag()