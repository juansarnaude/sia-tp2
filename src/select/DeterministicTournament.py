import random

from typing import List
from select import select
from src.classes.Individual import Individual
from src.select.Select import Select


class DeterministicTournament(Select):

    def __init__(self, m):
        self.m = m

    def select(self, population:List[Individual], k:int) -> List:
        selected=[]

        for _ in range(k):
            random_individuals = sorted(random.sample(population, self.m), reverse=True)
            selected.append(random_individuals[0])

        return selected
