from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
 name='cmtb',
 version='0.0.1',
 description='Confusion matrix in tensorboard',
 url='https://github.com/mr-francois/cmtb',
 author_email='mr.francois@gmx.de',
 install_requires=['tensorflow', 'numpy', 'sklearn', 'matplotlib'],
 long_description=long_description,
 long_description_content_type='text/markdown',
 py_modules=[]
)