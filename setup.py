from setuptools import setup, find_packages

setup(
    name="kubehelper",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python wrapper for kubectl",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kubehelper",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kubehelper=kubehelper.kubehelper:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
