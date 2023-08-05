import os

def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    output = os.popen(command).read()
    log(f"Command: {command}\nOutput: {output}")
    return output
