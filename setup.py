from setuptools import find_packages, setup

setup(
    name="jason",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
