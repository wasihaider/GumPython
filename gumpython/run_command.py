import subprocess


def run_command(cmd):
    response = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(response.stdout)
