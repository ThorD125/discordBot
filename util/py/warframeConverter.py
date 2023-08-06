import json
from util.py.helper import bashCommand

def wfGet(data=None):
    return bashCommand(f"curl -s https://api.warframestat.us/pc/en/{data} -L")

def baro():
    voidTrader = json.loads(wfGet("voidTrader"))
    if voidTrader.get("active"):
        return f"""{voidTrader.get("character")} in {voidTrader.get("endString")}: {[item.get("item") for item in voidTrader.get("inventory")]}"""
    else:
        return f"""{voidTrader.get("character")} in {voidTrader.get("startString")}"""

def events():
    events = json.loads(wfGet("events"))
    return f"""{[f'{event.get("description")}: {[reward.get("items") for reward in event.get("rewards")]}' for event in events]}"""

def sortie():
    sortie = json.loads(wfGet("sortie"))
    return f"""{sortie.get("faction")}-{sortie.get("boss")}: {[variant.get("missionType") for variant in sortie.get("variants")]}"""

def cetus():
    cetus = json.loads(wfGet("cetusCycle"))
    if cetus.get("state") == "day":
        return f"""Cetus: No Eidolon for {cetus.get("timeLeft")}"""
    return f"""Cetus: An Eidolon for {cetus.get("timeLeft")}"""

def vallis():
    vallis = json.loads(wfGet("vallisCycle"))
    return f"""Fortuna: {vallis.get("state")} for {vallis.get("timeLeft")}"""

def arbitration():
    arbitration = json.loads(wfGet("arbitration"))
    return f"""{arbitration.get("enemy")}: {arbitration.get("type")} until {arbitration.get("expiry").split("T")[1].split(".")[0]}"""

def steelPath():
    steelPath = json.loads(wfGet("steelPath"))
    return f"""{steelPath.get("currentReward").get("name")} for {steelPath.get("remaining")}"""

def archonHunt():
    archonHunt = json.loads(wfGet("archonHunt"))
    return f"""{archonHunt.get("boss")} for {archonHunt.get("eta")}: {[mission.get("typeKey") for mission in archonHunt.get("missions")]}"""


