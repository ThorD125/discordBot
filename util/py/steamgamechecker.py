import requests

from util.py.env import loadEnv

env = loadEnv()
steam_key = env["STEAM_KEY"]
url_all_games = env["URL_ALL_GAMES"]


def get_games(url):
    r = requests.get(url)
    data = r.json()
    try:
        games = data['response']['games']
        return games
    except KeyError:
        return []


def get_game_ids(games):
    game_Ids = []
    for game in games:
        game_Ids.append(game["appid"])
    return game_Ids


def person_with_least_games(list_game_ids):
    return min(list_game_ids, key=len)


def is_item_in_list_of_lists(item, list_of_lists):
    return all(item in sublist for sublist in list_of_lists)


def get_all_games(url):
    r = requests.get(url)
    data = r.json()
    games = data['applist']['apps']
    return games


def get_game_names(games):
    game_names = []
    for game in games:
        game_names.append(game["name"])
    return game_names


def steam_logic(user_list):
    bashCommand(f"wall {user_list}")
    list_users_games = []
    for user_id in user_list:
        playlist = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_key}&steamid={user_id}&format=json"
        games = get_games(playlist)
        list_users_games.append(games)

    list_game_ids = []
    for games in list_users_games:
        game_ids = get_game_ids(games)
        list_game_ids.append(game_ids)

    list_game_ids.remove([])

    same_games = []
    for gameId in person_with_least_games(list_game_ids):
        # print(gameId)
        if is_item_in_list_of_lists(gameId, list_game_ids):
            same_games.append(gameId)

    all_the_games = get_all_games(url_all_games)

    filtered = filter(lambda x: x['appid'] in same_games, all_the_games)

    games_list = sorted(get_game_names(list(filtered)))

    formated_games = "\n".join(games_list)

    return formated_games
