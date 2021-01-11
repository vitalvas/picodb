import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='PicoDB',
    version='0.1.1',
    description='A lightweight and simple database',
    long_description=README,
    long_description_content_type='text/markdown',
    author='VitalVas',
    author_email='source@vitalvas.com',
    url='https://github.com/vitalvas/picodb',
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Database'
    ],
    py_modules=[
        'picodb'
    ]
)
