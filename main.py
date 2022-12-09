from src.load import Map
from src.utils import Graph, heuristic
import random


m = Map('map2.txt')
player = None


class Genetic():
    def __init__(self, nbGene, nbInd):
        self.nbInd = nbInd
        self.graph = []
        for _ in range(nbInd):
            self.graph.append(Graph(nbGene=nbGene))
        self.pos = []

    def evaluate(self):
        self.pos = []
        for indiv in self.graph:
            self.pos.append({"pos": m.movePlayer(indiv), 'indiv': indiv})

    def fitness(self):
        for p in self.pos:
            if (p['pos'] == None):
                p['fitness'] = 999999
            else:
                p['fitness'] = heuristic.Manhattan(p['pos'], m.objectif) + 0.001 * len(p['indiv'].graph)
    
    def selection(self):
        self.pos.sort(key=lambda x: x['fitness'])
        if len(self.pos) > self.nbInd:
            self.pos = self.pos[:self.nbInd]
        return self.pos[0]["fitness"]

    def crossover(self):
        bestParent = self.pos[0]['indiv']
        new = [bestParent]
        for i in range(1, len(self.pos)):
            crossPoint = random.randint(0, len(bestParent.graph) - 1)
            tmp = bestParent.graph.copy()[crossPoint:]
            tmp += self.pos[i]['indiv'].graph[:crossPoint]
            new.append(Graph(child=tmp))
            tmp = bestParent.graph.copy()[:crossPoint]
            tmp += self.pos[i]['indiv'].graph[crossPoint:]
            new.append(Graph(child=tmp))
        self.graph = new

    def mutation(self):
        bestParent = True
        for indiv in self.graph:
            if bestParent:
                bestParent = False
                continue
            x = random.randint(0, 2)
            if x == 0:
                indiv.addGene()
            elif x == 1:
                indiv.removeGene()
            else:
                indiv.mutateGene()

pop = Genetic(5, 100)
for i in range(100):
    pop.evaluate()
    pop.fitness()
    f = pop.selection()
    print("Generation:", i, "Best Fitness:", f)
    pop.crossover()
    pop.mutation()


player = pop.pos[0]['indiv']
m.printMovePlayerStepByStep(player)