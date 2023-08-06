from util.py.helper import bashCommand
import json
from util.py.warframeConverter import baro, events, sortie, cetus, vallis, arbitration, steelPath, archonHunt


def commandFilter(input):
    print(input)
    return input.replace(" ", "").replace("\n", "").replace("\t", "").split("&&")[0]


def numberFilter(input):
    return int(input)


def downisit(url):
    url = commandFilter(url)
    return f"{url} is down!" if json.loads(bashCommand(f"curl https://monitor-api.vercel.app/api/public?url={url} -s")).get("isDown") else f"{url} is up!"


def CMDping(url):
    return bashCommand(f"ping -c 4 {commandFilter(url)}")


def CMDtraceroute(url, amount=15):
    return bashCommand(f"traceroute -4 {commandFilter(url)} -m {amount}")


def CMDdig(url):
    return bashCommand(f"dig {commandFilter(url)}")


def CMDranGenPassword(amount=20):
    return bashCommand(f"cat /dev/urandom | tr -dc 'A-Za-z0-9!?><,./\-_=+~:;*&^%$#@()[]' | head -c {numberFilter(amount)}")


def GETCAT():
    return json.loads(bashCommand("curl https://api.thecatapi.com/v1/images/search -s"))[0].get("url")


def GETtetrio(user):
    user = commandFilter(user)

    tetrio = bashCommand(f"curl https://ch.tetr.io/api/users/{user} -s")

    if not json.loads(tetrio).get("success"):
        return "User not found!"
    else:
        tetrior = json.loads(tetrio).get("data").get("user")
        return f"""```yaml
{user}'s stats:
XP: {tetrior.get("xp")}
League:
    Games played: {tetrior.get("league").get("gamesplayed")}
    Games won: {tetrior.get("league").get("gameswon")}
    Rating: {tetrior.get("league").get("rating")}
    Percentile rank: {tetrior.get("league").get("percentile_rank")}
```"""


def GETwf():
    return f"""```yaml{baro()}
events: {events()}
sortie: {sortie()}
{cetus()}
{vallis()}
UNSTABLE arbitration: {arbitration()}
steelpath: {steelPath()}
Archon Hunt: {archonHunt()}```"""
