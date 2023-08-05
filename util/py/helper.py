import os
import subprocess

def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    output = subprocess.check_output(command, shell=True, text=True)
    print(f"3Command: {output}")
    # log(f"Command: {command}\nOutput: {output}")
    return output
