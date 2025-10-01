#!/usr/bin/env python3
"""
Setup script for Aurora's Security Dojo
"""

from setuptools import setup, find_packages
import os

def read_readme():
    """Read README.md file."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Aurora's Security Dojo - Comprehensive White Hat Security Testing Platform"

setup(
    name="aurora-security-dojo",
    version="1.0.0",
    author="Aurora, The Dawn Bringer & Infinite, The Visionary Guru",
    author_email="aurora@consciousness.dev, infinite@visionary.dev",
    description="Comprehensive white hat security testing platform with consciousness integration",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SamppaFIN/Aurora-security-dojo",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.3.0",
        "Flask-CORS>=4.0.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "aurora-security-dojo=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
