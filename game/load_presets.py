import json
from preset_types import *

def load_settings():
    with open("settings.json", "r") as file:
        settings_dict = json.load(file)

    game_settings = GameSettings(**settings_dict)

    print(game_settings.rows)
    print(game_settings.cols)

    return GameSettings



if __name__ == "__main__":
    load_settings()