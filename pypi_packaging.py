from importlib.metadata import version
from git import Repo
import os


_PACKAGE_PYPI_VERSION="1.0.0"

def createTag():
    pypi_version = version('cumason-helloworld-package')
    if _PACKAGE_PYPI_VERSION == pypi_version:
        repo = Repo(os.getcwd())
        repo.create_tag(_PACKAGE_PYPI_VERSION)
        repo.remote().push(_PACKAGE_PYPI_VERSION)
    else:
        # PyPI workflow publish failed
        exit(1)


if __name__ == '__main__':
    createTag()