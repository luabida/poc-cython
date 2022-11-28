from distutils.core import setup
from Cython.Build import cythonize

setup(
        ext_modules = cythonize("fib.pyx"),
)

#`python setup.py build_ext --inplace` builds an executable (.so)
#`pip install -e .` installs the module globally
