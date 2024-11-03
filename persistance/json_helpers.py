"""Defines all the helpers used on json files"""

import os
import json

DEFAULT_JSON_STRUCTURE = {
    "player":{
        "pos": [0, 0],
        "inventory": [],
        "level":1,
        "experience":0
    },

    "map_info":{
        "monsters":{},
        "drops":{},
        "bullets":{},
    }
}

def create_json_file(path: str):
    """Creates a JSON file on the path specified"""

    if not os.path.exists(path):
        reset_file(path)

def reset_file(path: str):
    """Resets the file to be the default file"""

    with open(path, "w", encoding="utf-8") as outfile:
        json.dump(DEFAULT_JSON_STRUCTURE, outfile)
