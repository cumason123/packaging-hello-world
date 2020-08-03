from importlib.metadata import version
from git import Repo
import os


_CLOUDEVENTS_PYPI_VERSION="v3.1.1"

def createTag():
    pypi_version = version('cumason-helloworld-package')
    if _CLOUDEVENTS_PYPI_VERSION.endswith(pypi_version):
        repo = Repo(os.getcwd())
        repo.create_tag(_CLOUDEVENTS_PYPI_VERSION)
        repo.remote().push(_CLOUDEVENTS_PYPI_VERSION)
    else:
        # PyPI workflow publish failed
        exit(1)


if __name__ == '__main__':
    createTag()