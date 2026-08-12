"""Portable Local Environment actions for the swane_supplement repository."""

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RESOURCE_PATHS = (
    "swane_supplement/icons/ok.svg",
    "swane_supplement/icons/error.svg",
    "swane_supplement/icons/warn.svg",
    "swane_supplement/icons/load.svg",
    "swane_supplement/icons/void.svg",
    "swane_supplement/icons/swane.png",
    "swane_supplement/icons/swane.icns",
    "swane_supplement/resources/mni_icbm152_t1_tal_nlin_sym_09c_brain.nii.gz",
    "swane_supplement/resources/FLAT1/binary_cerebellum.nii.gz",
    "swane_supplement/resources/FLAT1/brain_cortex_mas_OK.nii.gz",
    "swane_supplement/resources/FLAT1/mean_extension.nii.gz",
    "swane_supplement/resources/FLAT1/mean_flair.nii.gz",
    "swane_supplement/resources/FLAT1/std_final_extension.nii.gz",
    "swane_supplement/resources/FLAT1/std_final_flair.nii.gz",
)


def run(*arguments):
    subprocess.run([str(argument) for argument in arguments], cwd=PROJECT_ROOT, check=True)


def run_python(*arguments):
    run(sys.executable, *arguments)


def verify_resources():
    missing = [path for path in RESOURCE_PATHS if not (PROJECT_ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing packaged resources: {0}".format(", ".join(missing)))
    print("Verified {0} exported resource paths.".format(len(RESOURCE_PATHS)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "action",
        choices=("setup", "bootstrap", "compile", "resource-check", "build", "format", "pip-check"),
    )
    action = parser.parse_args().action

    if action == "setup":
        print("Virtual environment ready. Run 'Bootstrap Python' to install dependencies.")
    elif action == "bootstrap":
        run_python("-m", "pip", "install", "--upgrade", "pip")
        run_python("-m", "pip", "install", "-e", ".", "build", "black")
    elif action == "compile":
        run_python("-m", "compileall", "swane_supplement")
    elif action == "resource-check":
        verify_resources()
    elif action == "build":
        run_python("-m", "build")
    elif action == "format":
        run_python("-m", "black", "--check", "swane_supplement")
    elif action == "pip-check":
        run_python("-m", "pip", "check")


if __name__ == "__main__":
    main()
