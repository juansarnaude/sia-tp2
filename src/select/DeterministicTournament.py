import random

from typing import List
from select import select
from src.classes.Individual import Individual


class DeterministicTournament(select):

    def __init__(self, m):
        self.m = m

    def select(self, cls, population:List[Individual] , k: int) -> List:
        selected=[]

        for _ in range(k):
            random_individuals = sorted(random.sample(population, self.m), reverse=True)
            while random_individuals[0] in selected:
                random_individuals = sorted(random.sample(population, self.m), reverse=True)
            selected.append(random_individuals[0])

        return selected
