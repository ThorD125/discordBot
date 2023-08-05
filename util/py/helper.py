import os
import subprocess

def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.stdout.read().decode("utf-8")
