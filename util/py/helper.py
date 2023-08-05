import os

def log(message):
    os.popen(f"wall {message}")

def bashcommand(command):
    return os.popen(command).read()
