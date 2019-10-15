import os, subprocess

def execute_shell_process(message, command):
    print(message)

    env_copy = os.environ.copy()
    output = subprocess.run(command, env=env_copy, shell=True)
    if output.returncode == 0:
        print("Success!")
    else:
        print("Oops! Please try again.")