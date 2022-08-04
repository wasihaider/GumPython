import subprocess

from .exceptions import GumNotFoundError, GumPythonError


def run_command(cmd):
    try:
        response = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        print(response.stdout)
    except FileNotFoundError as fe:
        if "No such file or directory: 'gum'" in str(fe):
            raise GumNotFoundError(
                "No gum installation found. Please install gum cli. See README for dependencies."
            )
        raise GumPythonError(str(fe))
