from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='the-directory-scanner',
    packages=['the_directory_scanner'],
    version='1.0',
    license='BSD',

    description='The Directory Scanner is a Python library designed to simplify the process of scanning directory structures and generating a comprehensive list of files and folders. It provides a convenient way to recursively traverse directories, ignoring specific files and folders specified by the user.',

    author='Armen-Jean Andreasian',
    author_email='armen_andreasian@proton.me',

    url='https://github.com/Armen-Jean-Andreasian',
    keywords=['directory structure', 'python'],
    # Keywords users can search on PyPI

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        # List any dependencies your library may have
    ],

    python_requires='>=3.8',

    long_description=long_description
    ,
    long_description_content_type='text/markdown',
)
