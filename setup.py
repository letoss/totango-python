import ast
import os

from setuptools import setup, find_packages


def version(filename):
    """Return version string."""
    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s

requires = ['requests']

setup(name='totango',
      version=version(os.path.join('totango', '__init__.py')),
      description='Totango Python Library',
      author='German Bourdin',
      author_email='admin@gbourdin.com',
      url='http://github.com/gbourdin/totango-python',
      license='Apache 2.0',
      packages=find_packages(),
      install_requires = requires,
      keywords="totango",
      zip_safe=False)
