import setuptools

# with open("README.md", "r") as file:
#     long_description = file.read()

setuptools.setup(
    name="morjus-selenium-tests",
    platforms="linux",
    version="0.0.1",
    author="Morjus",
    author_email="morjus@yandex.ru",
    description="Package for selenium tests",
    url="https://github.com/morjus",
    data_files=[("conf", ["conftest.py"])],
    packages=["tests/", "pages/"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Lincense :: OSI :: MIT License",
        "Operating System :: OS Independent"
        ],
    zip_safe=False,
    python_requires=">3.6",
    install_requires=[
        "allure-pytest==2.8.16",
        "pytest==5.4.2",
        "requests==2.23.0",
        "selenium==3.141.0"
    ]
)
