from git import Repo
import os


_CLOUDEVENTS_PYPI_VERSION="v3.0.0"

def createTag():
    repo = Repo(os.getcwd())
    repo.create_tag(_CLOUDEVENTS_PYPI_VERSION)
    repo.remote().push(_CLOUDEVENTS_PYPI_VERSION)


if __name__ == '__main__':
    createTag()