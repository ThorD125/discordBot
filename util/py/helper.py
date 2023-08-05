import os

def log(message):
    os.popen(f"wall {message}")
