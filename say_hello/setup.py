from distutils.core import setup
from pathlib import Path
from Cython.Build import cythonize

file = Path(__file__).parent / "hello.pyx"

setup(
        name='Hello app',
        ext_modules=cythonize(str(file)),
        zip_safe=False, #https://cython.readthedocs.io/en/stable/src/quickstart/build.html#building-a-cython-module-using-distutils
)

