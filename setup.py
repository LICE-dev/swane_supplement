from setuptools import setup, find_packages

setup(
    name="swane_supplement",
    version="0.2",
    description="Standardized Workflow for Advanced Neuroimaging in Epilepsy - supplementary files",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="LICE - Commissione Neuroimmagini",
    author_email="dev@lice.it",
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
    ],
    packages=find_packages(),
    include_package_data=True,  # serve per package_data
    package_data={
        "swane_supplement": [
            "resources/**/*",
            "icons/*",
        ],
    },
)
