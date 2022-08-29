from setuptools import setup

setup(
 name='cmtb',
 version='0.0.1',
 description='Confusion matrix in tensorboard',
 url='https://github.com/mr-francois/cmtb',
 author_email='mr.francois@gmx.de',
 install_requires=['tensorflow', 'numpy', 'sklearn', 'matplotlib'],
 py_modules=[]
)