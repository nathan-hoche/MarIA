import json

with open('maps/config.json') as f:
    MAP_CONFIG = json.load(f)

def load_map(name):
    with open('maps/' + name) as f:
        return f.read()

def convert_map(map):
    m = map.replace(MAP_CONFIG["air"], '0').replace(MAP_CONFIG['block'], '1')
    m = m.split('\n')
    res = []
    for line in m:
        res.append(list(line))
    return res

def get_player_and_objectif(map):
    player = None
    objectif = None

    i = 0
    for line in map:
        if MAP_CONFIG['player'] in line:
            player = (i, line.index(MAP_CONFIG['player']))
        if MAP_CONFIG['objectif'] in line:
            objectif = (i, line.index(MAP_CONFIG['objectif']))
        if (player and objectif):
            break
        i += 1
    map[player[0]][player[1]] = '0'
    map[player[0]][player[1]] = '0'
    return player, objectif

class Map:
    def __init__(self, name):
        self.map = load_map(name)
        self.converted_map = convert_map(self.map)
        self.player, self.objectif = get_player_and_objectif(self.converted_map)

