import os
import subprocess

def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    print(f"1Command: {command}")
    output = subprocess.check_output(command, shell=True, text=True)
    print(f"2Output: {output}")
    return output
