from typing import Dict, List

from setuptools import setup

BASE_DEPENDENCIES: List[str] = ["attrs", "cattrs"]

TEST_DEPENDENCIES: List[str] = ["matrix-synapse>=1.44.0", "tox", "twisted"]

MYPY_DEPENDENCIES: List[str] = [
    "mypy==0.910",
    "types-setuptools",
]

LINT_DEPENDENCIES: List[str] = [
    "black==21.9b0",
    "flake8==4.0.1",
    "isort==5.9.3",
]

DEV_DEPENDENCIES: List[str] = (
    LINT_DEPENDENCIES + TEST_DEPENDENCIES + MYPY_DEPENDENCIES + ["towncrier"]
)

EXTRA_DEPENDENCIES: Dict[str, List[str]] = {
    "dev": DEV_DEPENDENCIES,
    "lint": LINT_DEPENDENCIES,
    "test": TEST_DEPENDENCIES,
    "mypy": MYPY_DEPENDENCIES,
}

setup(
    name="synapse_my_module",
    description="This module adds super florbs to Synapse",
    use_scm_version=True,
    packages=["synapse_my_module"],
    # url="",
    # license="",
    author="John Moduleson",
    author_email="jm@example.org",
    install_requires=BASE_DEPENDENCIES,
    extras_require=EXTRA_DEPENDENCIES,
)
