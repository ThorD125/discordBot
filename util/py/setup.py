from util.py.helper import (bashCommand)

def update():
    bashCommand(f"./update.sh")

def restart():
    bashCommand(f"./util/sh/restart.sh")
