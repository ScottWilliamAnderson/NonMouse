"""Setup configuration for the NonMouse package."""

from __future__ import annotations

from pathlib import Path

from setuptools import find_packages, setup


def _requires_from_file(filename: str) -> list[str]:
    """Return requirements listed in ``filename``."""
    return Path(filename).read_text().splitlines()


setup(
    name="nonmouse",
    version="2.7.0",
    packages=find_packages(),
    description="a webcam-based virtual gesture mouse that is easy to use with hands on the desk",
    author="Yuki TAKEYAMA",
    author_email="namiki.takeyama@gmail.com",
    url="https://github.com/takeyamayuki/NonMouse",
    license="Apache-2.0",
    install_requires=_requires_from_file("requirements.txt"),
    entry_points={
        "console_scripts": [
            "nonmouse=nonmouse.__main__:main",
        ],
    },
    python_requires=">=3.9",
)
