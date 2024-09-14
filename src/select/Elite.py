import math

from typing import List
from src.select.Select import Select
from src.classes.Individual import Individual


class Elite(Select):
    """
    Selects K Individuals from a set of N, the set if first ordered by
    fitness and each Individual is selected n(i) = ceil((K-i)/N) times.

    Args:
        population (List[Individual]): List of Individual.
        K (int): Number of Individuals to be selected.

    Return:
        List[Individual]: selected population
    """
    @classmethod
    def select(cls, population:List[Individual], k: int) -> List:
        sorted_population = sorted(population,reverse=True)
        n=len(sorted_population)
        to_return=[]

        for i, individual in enumerate(sorted_population):
            times=math.ceil((k-i)/n)
            for _ in range(times):
                to_return.append(individual)

        return to_return