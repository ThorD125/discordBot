import sys
import requests
import json
import os
import logging

# logging.basicConfig(level=logging.INFO)

def get_games(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        if not r.text:
            logging.error(f"Empty response from {url}")
            return None
        try:
            data = r.json()
        except ValueError:
            logging.error(f"Invalid JSON response from {url}")
            return None
        
        games = data.get('response', {}).get('games', None)
        if games is None:
            logging.error(f"No 'games' key found in the response from {url}")
            return None

        return games
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error for {url}: {e}")
        return None

def get_game_ids(games):
    gameIds = []
    for game in games:
        gameIds.append(game["appid"])
    return gameIds

def find_common_values(lists_with_ids):
    shortest_list = min(lists_with_ids, key=len)
    common_values = set(shortest_list)
    for lst in lists_with_ids:
        common_values.intersection_update(lst)
    return list(common_values)

def get_all_games(url):
    r = requests.get(url)
    data = r.json()
    games = data['applist']['apps']
    return games

def get_game_names(games):
    gameNames = []
    for game in games:
        gameNames.append(game["name"])
    return gameNames

def is_steamid(user):
    returner = user.isdigit() and len(user) == 17
    print(user, returner)
    return returner

def get_steamid_from_vanityurl(vanityurl, apikey):
    url = f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={apikey}&vanityurl={vanityurl}"
    response = requests.get(url)
    data = response.json()
    if data["response"]["success"] == 1:
        return data["response"]["steamid"]
    else:
        return None

async def testGamesAll(apikey, user_ids):
    urls = []
    for user in user_ids:
        steamid = get_steamid_from_vanityurl(user, apikey)
        if steamid:
            url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apikey}&steamid={steamid}&format=json"
            urls.append(url)
        else:
            url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apikey}&steamid={user}&format=json"
            urls.append(url)


    all_games = []
    for url in urls:
        all_games.append(get_games(url))


    all_game_ids = []
    for games in all_games:
        all_game_ids.append(get_game_ids(games))

    sameGames = find_common_values(all_game_ids)

    all_games_url = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/"

    filtered = filter(lambda x: x['appid'] in sameGames, get_all_games(all_games_url))

    result = get_game_names(list(filtered))

    # print(result)
    return result

