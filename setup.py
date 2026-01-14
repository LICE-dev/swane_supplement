from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as build_py_orig
import os, zipfile


class build_py(build_py_orig):
    """
    Custom build_py command:
    - Creates SwaneSlicerModule.zip inside resources before building the package.
    """

    def run(self):
        # Paths
        src_folder = os.path.join("swane_supplement", "resources", "SwaneSlicerModule")
        zip_file = os.path.join("swane_supplement", "resources", "SwaneSlicerModule.zip")

        # Ensure resources folder exists
        os.makedirs(os.path.dirname(zip_file), exist_ok=True)

        if not os.path.exists(src_folder):
            print(f"Source folder does not exist: {src_folder}")
        else:
            with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
                for root, dirs, files in os.walk(src_folder):
                    for f in files:
                        abs_path = os.path.join(root, f)
                        arcname = os.path.join("SwaneSlicerModule", os.path.relpath(abs_path, src_folder))
                        zf.write(abs_path, arcname=arcname)
            print(f"Created {zip_file}")

        # Continue standard build
        super().run()


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
    cmdclass={"build_py": build_py},
)


