from src.load import Map
from src.utils import Graph


m = Map('map1.txt')

g = Graph(5)

player = m.movePlayer(g.graph)
print(player)