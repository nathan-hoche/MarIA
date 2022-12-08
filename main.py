from src.load import Map

m = Map('map1.txt')
print("Player", m.player, "| Objectif", m.objectif)
print("MAPS:\n", m.map)
print("MAPS:\n", *m.converted_map, sep='\n')