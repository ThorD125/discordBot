import os
import subprocess
import json


def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.stdout.read().decode("utf-8")

def downisit(url):
    return "It is down!" if json.loads(bashCommand(f"curl https://monitor-api.vercel.app/api/public?url={url} -s")).get("isDown") else "It is up!"
