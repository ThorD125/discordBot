import json
import requests

def wfGet(inputData=None):
    url = "https://api.warframestat.us/pc/en"

    response = requests.get(f"{url}/{inputData}")
    if response.status_code == 200:
        data = response.json()
        return data
    return None


def baro():
    voidTrader = wfGet("voidTrader")
    if voidTrader.get("active"):
        return f"""{voidTrader.get("character")} in {voidTrader.get("endString")}: {[item.get("item") for item in voidTrader.get("inventory")]}"""
    else:
        return f"""{voidTrader.get("character")} in {voidTrader.get("startString")}"""


def events():
    events = wfGet("events")
    return f"""{[f'{event.get("description")}: {[reward.get("items") for reward in event.get("rewards")]}' for event in events]}"""


def sortie():
    sortie = wfGet("sortie")
    return f"""{sortie.get("faction")}-{sortie.get("boss")}: {[variant.get("missionType") for variant in sortie.get("variants")]}"""


def cetus():
    cetus = wfGet("cetusCycle")
    if cetus.get("state") == "day":
        return f"""Cetus: No Eidolon for {cetus.get("timeLeft")}"""
    return f"""Cetus: An Eidolon for {cetus.get("timeLeft")}"""


def vallis():
    vallis = wfGet("vallisCycle")
    return f"""Fortuna: {vallis.get("state")} for {vallis.get("timeLeft")}"""


def arbitration():
    arbitration = wfGet("arbitration")
    try:
        return f"""{arbitration.get("enemy")}: {arbitration.get("type")} until {arbitration.get("expiry").split("T")[1].split(".")[0]}"""
    except:
        return f"""[UNSTABLE], NODATA"""


def steelPath():
    steelPath = wfGet("steelPath")
    return f"""{steelPath.get("currentReward").get("name")} for {steelPath.get("remaining")}"""


def archonHunt():
    archonHunt = wfGet("archonHunt")
    return f"""{archonHunt.get("boss")} for {archonHunt.get("eta")}: {[mission.get("typeKey") for mission in archonHunt.get("missions")]}"""


def getWf():
    return f"""```{baro()}
events: {events()}
sortie: {sortie()}
{cetus()}
{vallis()}
arbitration: {arbitration()}
steelpath: {steelPath()}
Archon Hunt: {archonHunt()}```"""
