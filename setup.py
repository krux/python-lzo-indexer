#!/usr/bin/env python

from setuptools import setup


setup(name="lzo-indexer",
    version="0.0.1",
    description="Library for indexing LZO compressed files",
    long_description="""

    Python library for indexing block offsets within LZO compressed
    files. The implementation is largely based on that of the [Hadoop
    Library](https://github.com/twitter/hadoop-lzo). Index files are used
    to allow Hadoop to split a single file compressed with LZO into several
    chunks for parallel processing.

    Since LZO is a block based compression algorithm, we can split the file
    along the lines of blocks and decompress each block on it's own. The
    index is a file containing byte offsets for each block in the original
    LZO file.
    """,
    author="Tom Arnfeld",
    author_email="tom@duedil.com",
    maintainer="Tom Arnfeld",
    maintainer_email="tom@duedil.com",
    url="https://github.com/duedil-ltd/python-lzo-indexer",
    download_url="https://github.com/duedil-ltd/python-lzo-indexer/archive/release-0.0.1.zip",
    license='License :: OSI Approved :: Apache Software License',
    packages=["lzo_indexer"],
    scripts=["bin/lzo-indexer"],
    test_suite="tests.test_indexer",
)
