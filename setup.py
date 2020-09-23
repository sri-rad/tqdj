import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tqdj", # Replace with your own username
    version="0.0.2",
    author="Srihari Radhakrishna",
    author_email="rsrihari95@gmail.com",
    description="A progress bar that plays lofi music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/sri-rad/tqdj",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'simpleaudio'
    ],
    python_requires='>=3.6',
)