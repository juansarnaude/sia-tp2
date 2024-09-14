import random

from typing import List
from select import select
from src.classes.Individual import Individual
from src.select.Select import Select


class DeterministicTournament(Select):

    """
    From a population of N Individuals, M individuals are chosen randomly.
    From this M Individuals, the best one is selected.
    This process is repeated until K Individuals are selected.

    Args:
        population (List[Individual]): List of Individual.
        K (int): Number of Individuals to be selected.

        M (int) - cls argument:  Number of Individuals to participate in each one of the K elite rounds.

    Return:
        List[Individual]: selected population
    """

    def __init__(self, m):
        self.m = m

    def select(self, population:List[Individual], k:int) -> List:
        selected=[]

        for _ in range(k):
            random_individuals = sorted(random.sample(population, self.m), reverse=True)
            selected.append(random_individuals[0])

        return selected
