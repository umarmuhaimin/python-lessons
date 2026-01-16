# 📚 Third-Party Libraries, packages and pip

# → Python comes with many built-in libraries, but you can install others.
# → Third-party libraries are created by the community and can be installed via pip.

# → A package is a collection of modules (files) grouped together.
# → Packages help organize related modules and make it easier to distribute code.


# 🔹 pip 
# → pip is the package installer for Python.
# → You can use pip to install packages from the Python Package Index (PyPI) and other indexes.
# → Command to install a package: pip install package_name

# 👉 pip is a program that generally comes with Python itself.
# 👉 that allows you to install packages onto your own Macs, PCs or cloud environment by just running a command.
# 👉 voila, you have access to a whole new library in Python that didn't come with Python itself.
# 👉 But now it's available on your system for you.


# 🔹 cowsay package project :
# → A fun package that generates ASCII art of a cow saying something.

# 👉 cowsay.cow
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# Output: If run as python3 testing.py Alice, it prints an ASCII art of a cow saying "hello, Alice".


# 👉 cowsay.trex
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

# Output: If run as python3 testing.py Alice, it prints an ASCII art of a T-rex saying "hello, Alice".





