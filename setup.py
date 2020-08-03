from setuptools import setup
from pypi_packaging import _CLOUDEVENTS_PYPI_VERSION


setup(name="cumason-helloworld-package",
      version=_CLOUDEVENTS_PYPI_VERSION,
      packages=['helloworld'])
