#!/usr/bin/env python

import setuptools  # type: ignore

setuptools.setup(
    name="xontrib-aliastips",
    version="0.5.0",
    license="EUPL-1.2",
    author="Médéric Hurier",
    author_email="dev@fmind.me",
    description="Suggest alias tips after a command is executed",
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r").read(),
    url="https://git.fmind.me/fmind/xontrib-aliastips",
    keywords="xontrib suggest alias tips",
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
    ],
    extras_require={"dist": ["twine", "wheel", "setuptools"]},
    python_requires=">=3.6",
    install_requires=["xonsh"],
    packages=["xontrib"],
    package_dir={"xontrib": "xontrib"},
    package_data={"xontrib": ["*.xsh"]},
)
