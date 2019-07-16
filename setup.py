# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : setup.py
# @Time    : 19-7-15 下午5:45
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = [_ for _ in f.read().splitlines() if _]

setuptools.setup(
    name="greet-girl",
    version="1.0.0",
    author="itswcg",
    author_email="itswcg@gmail.com",
    description="Time of greeting girl on WeChat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itswcg/Greet-girlfriend",
    install_requires=requirements,
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'greet-girl = src.__main__:main'
        ],
    }
)
