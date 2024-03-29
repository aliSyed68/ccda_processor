import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccda_processor",
    version="0.0.7",
    author="Ali H Syed",
    author_email="",
    description="A light-weight package to process a compressed file of CCDA patient records and convert to 1 web page per patient record",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aliSyed68/ccda_processor",
    packages=setuptools.find_packages(),
    install_requires=[
        'xmltodict',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
