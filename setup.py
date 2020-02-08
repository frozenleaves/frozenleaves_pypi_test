# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="frozenleaves",
    version="0.0.3",
    py_modules=['demo', 'hello'],
    packages = ['frozenleaves'],
    author="frozenleaves",
    author_email="914814442@qq.com",
    description="A test package",

    url="http://frozenleaves.cn",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)