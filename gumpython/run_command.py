import subprocess


def run_command(cmd):
    print(f"Going to run this command: {' '.join(cmd)}")
    response = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(response.stdout)
