import os
from setuptools import setup
from setuptools.command.develop import develop

class PostInstall(develop):
    def run(self):
        develop.run(self)
        os.system('pre-commit install')

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="knotpy",
    version="1.2.1",
    author="Ramon Ribeiro",
    author_email="rhpr@cesar.org.br",
    description=("API to access data from knot devices"),
    license="MIT",
    keywords="IoT dataAnalytics API web",
    url="https://github.com/ramonhpr/knot-lib-python",
    install_requires=['socketIO_client'],
    extras_require={
        'dev': [
            'pylint',
            'pre-commit'
        ]
    },
    cmdclass={'develop': PostInstall},
    packages=['knotpy', 'knotpy/decorators'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
