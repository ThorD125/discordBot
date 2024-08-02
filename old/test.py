# import json
# from util.py.helper import bashCommand
# from util.py.warframeConverter import *

# url = "https://google.com"

from util.py.steamgamechecker import steam_logic


args = "76561199002916354 76561198259056804"

print(steam_logic(args.split(" ")))
