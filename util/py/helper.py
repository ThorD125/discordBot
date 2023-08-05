import os

def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    return os.popen(command).read()
