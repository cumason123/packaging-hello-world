from setuptools import setup
from pypi_packaging import _PACKAGE_PYPI_VERSION


setup(name="cumason-helloworld-package",
      version=_PACKAGE_PYPI_VERSION,
      packages=['helloworld'])
