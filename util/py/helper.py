import os
import subprocess

def log(message):
    os.popen(f"wall {message}")

async def bashCommand(command):
    output = subprocess.check_output(command, shell=True, text=True)
    return output
