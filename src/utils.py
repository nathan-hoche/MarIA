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
    def __init__(self, nbGen) -> None:
        self.action = Action().action
        self.graph = []
        for i in range(nbGen):
            r = random.randint(0, len(self.action) - 1)
            self.graph.append(Node(self.action[r]))