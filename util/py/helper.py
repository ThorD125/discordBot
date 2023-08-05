import os
import subprocess
import json


def log(message):
    os.popen(f"wall {message}")

def bashCommand(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.stdout.read().decode("utf-8")


def commandFilter(input):
    return input.replace(" ", "").replace("\n", "").replace("\t", "").split("&&")[0]

def downisit(url):
    url = commandFilter(url)
    return f"{url} is down!" if json.loads(bashCommand(f"curl https://monitor-api.vercel.app/api/public?url={url} -s")).get("isDown") else f"{url} is up!"

def CMDping(url):
    return bashCommand(f"ping -c 4 {commandFilter(url)}")

def CMDtraceroute(url):
    return bashCommand(f"traceroute {commandFilter(url)} ")

def CMDdig(url):
    return bashCommand(f"dig {commandFilter(url)}")

def CMDranGenPassword(amount):
    return bashCommand(f"cat /dev/urandom | tr -dc 'A-Za-z0-9!?><,./\-_=+~:;*&^%$#@()[]' | head -c {commandFilter(amount)}")
