from util.py.helper import bashCommand


def updateSET():
    bashCommand(f"./update.sh")


def restartSET():
    bashCommand(f"./util/sh/restart.sh")
