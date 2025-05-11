from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="django-nginx-generator",
    version="1.0.0",
    description="CLI tool to auto-generate production-grade Nginx configs for Django",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Amirreza-Jabbari/django-nginx-generator",
    author="Amirreza Jabbari",
    author_email="amirrezajabbari79@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Systems Administration",
    ],
    py_modules=["generate_nginx"],
    install_requires=[
        "click>=8.0",
        "jinja2>=3.0",
        "Django>=3.2",
    ],
    entry_points={
        "console_scripts": [
            "generate_nginx=generate_nginx:main",
        ],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/Amirreza-Jabbari/django-nginx-generator/issues",
        "Source Code": "https://github.com/Amirreza-Jabbari/django-nginx-generator",
        "Documentation": "https://github.com/Amirreza-Jabbari/django-nginx-generator#readme",
    },
)
