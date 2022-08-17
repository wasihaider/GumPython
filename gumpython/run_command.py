import subprocess

from .exceptions import GumNotFoundError, GumPythonError


def run_command(cmd, command_input: str = None):
    try:
        if command_input:
            response = subprocess.run(
                cmd, input=command_input, stdout=subprocess.PIPE, text=True
            )
        else:
            response = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        return response
    except FileNotFoundError as fe:
        if "No such file or directory: 'gum'" in str(fe):
            raise GumNotFoundError(
                "No gum installation found. Please install gum cli. See README for dependencies."
            )
        raise GumPythonError(str(fe))
