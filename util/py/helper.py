import os
import subprocess

def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output.wait()
    log(f"Command: {command}\nOutput: {output}")
    return output.stdout.read().decode("utf-8")
