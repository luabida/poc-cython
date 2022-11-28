### Building Cython code

#### There are several ways to build Cython code:
- Use the [Jupyter] notebook or the [Sage] notebook, both of which allow Cython code inline. This is the easiest way to get started writing Cython code and running it.
- `notebooks/` directory

##### Example 01 (say_hello, fibonacci)
- Write a distutils/setuptools setup.py. This is the normal and recommended way.
- `make build`

##### Example 02 (helloworld)
- Use Pyximport, importing Cython .pyx files as if they were .py files (using distutils to compile and build in the background). This method is easier than writing a setup.py, but is not very flexible. So you’ll need to write a setup.py if, for example, you need certain compilations options.

##### Example 03 ()
- Run the cython command-line utility manually to produce the .c file from the .pyx file, then manually compiling the .c file into a shared object library or DLL suitable for import from Python. (These manual steps are mostly for debugging and experimentation.)

