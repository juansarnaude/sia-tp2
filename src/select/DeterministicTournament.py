import random

from select import select


class DeterministicTournament(select):

    def __init__(self, m):
        self.m = m

    def select(self, cls, population: [], k: int) -> []:
        selected=[]

        for _ in range(k):
            random_individuals = sorted(random.sample(population, self.m), reverse=True)
            while random_individuals[0] in selected:
                random_individuals = sorted(random.sample(population, self.m), reverse=True)
            selected.append(random_individuals[0])

        return selected
