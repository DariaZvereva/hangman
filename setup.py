from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="Daria Zvereva",
    author_email="zverevads@gmail.com",
    url="https://github.com/DariaZvereva/hangman",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
    ]
)
