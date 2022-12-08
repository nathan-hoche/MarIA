from src.load import Action
import random

class Node:
    def __init__(self, action) -> None:
        self.action = action
    
    def __getitem__(self, key):
        return self.action[key]

    def __repr__(self) -> str:
        return "Node:" + str(self.action)

    def __str__(self) -> str:
        return "Node:" + str(self.action)

class Graph():
    def __init__(self, nbGene=-1, child=None) -> None:
        self.action = Action().action
        if child:
            self.graph = child
        else:
            self.graph = []
            for _ in range(nbGene):
                r = random.randint(0, len(self.action) - 1)
                self.graph.append(Node(self.action[r]))
    
    def __iter__(self):
        return iter(self.graph)
    
    def addGene(self):
        r = random.randint(0, len(self.action) - 1)
        self.graph.append(Node(self.action[r]))
    
    def removeGene(self):
        if len(self.graph) > 1:
            r = random.randint(0, len(self.graph) - 1)
            self.graph.pop(r)
    
    def mutateGene(self):
        r = random.randint(0, len(self.graph) - 1)
        self.graph[r] = Node(self.action[random.randint(0, len(self.action) - 1)])


class heuristic:
    def Manhattan(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])