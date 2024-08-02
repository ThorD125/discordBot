import sys
import requests
import json

user_ids = [*sys.argv[1:]]
# thor = 76561198259056804
# louis = 76561198255958082
# emma = 76561198345476533
# della = 76561199030951176

api_key = "1089BDD7F93DF7BD189290D741D2EAE1"

urls = []
for user in user_ids:
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={user}&format=json"
    urls.append(url)

print(urls)

def get_games(url):
    r = requests.get(url)
    data = r.json()
    games = data['response']['games']
    return games

all_games = []
for url in urls:
    all_games.append(get_games(url))


def get_game_ids(games):
    gameIds = []
    for game in games:
        gameIds.append(game["appid"])
    return gameIds

all_game_ids = []
for games in all_games:
    all_game_ids.append(get_game_ids(games))


def find_common_values(lists_with_ids):
    shortest_list = min(lists_with_ids, key=len)
    common_values = set(shortest_list)
    for lst in lists_with_ids:
        common_values.intersection_update(lst)
    return list(common_values)

sameGames = find_common_values(all_game_ids)

_all_games = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/"

def get_all_games(url):
    r = requests.get(url)
    data = r.json()
    games = data['applist']['apps']
    # print(games)
    return games

get_all_games = get_all_games(_all_games)

filtered = filter(lambda x: x['appid'] in sameGames, get_all_games)

def get_game_names(games):
    gameNames = []
    for game in games:
        gameNames.append(game["name"])
    return gameNames

print(get_game_names(list(filtered)))