import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyplanner",
    version="0.0.1",
    author="Fidel Jimenez Sanzano",
    author_email="fidel.jimenez@desoft.cu",
    description="Python library to read gnome planner file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fjsanzano/pyplanner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
) 
