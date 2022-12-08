from src.load import Map
from src.utils import Graph


m = Map('map1.txt')

g = Graph(5)

print(m.player)
player = m.movePlayer(g.graph)
print(player)

if (player != None):
    tmp = m.map.split('\n')
    tmp[player[0]] = tmp[player[0]][:player[1]] + 'N' + tmp[player[0]][player[1] + 1:]
    tmp = '\n'.join(tmp)
    print(tmp)