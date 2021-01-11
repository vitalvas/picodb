"""
PicoDB
______

PicoDB is lightweight, fast, and simple database with namespaces

PicoDB is simple
````````````````

::
    >>> import picodb

    >>> db = picodb.load('test.db', False)

    >>> db.set_ns('space')
    True

    >>> db.set('space', 'key', 'value')
    True

    >>> db.delete('space', 'key')
    True

    >>> db.get('space', 'key')
    'value'

    >>> db.save()

And Easy to Install
```````````````````

::
    $ pip install picodb

"""

from distutils.core import setup

setup(
    name='PicoDB',
    version='0.1.0',
    description='A lightweight and simple database',
    long_description=__doc__,
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
