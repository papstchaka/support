import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="support",
    version="0.1.0",
    author="Alex Christoph",
    author_email="alexander.christoph@tum.com",
    description="Small package providing some simple but useful code snippets for daily tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/papstchaka/support",
    project_urls={
        "Bug Tracker": "https://github.com/papstchaka/support/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)