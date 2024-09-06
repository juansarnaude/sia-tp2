import math

from typing import List
from src.select.Select import Select
from src.classes.Individual import Individual


class Elite(Select):

    @classmethod
    def select(cls, population:List[Individual], k: int) -> List:
        sorted_population = sorted(population,reverse=True)
        n=len(sorted_population)
        to_return=[]

        for i, individual in enumerate(sorted_population):
            times=math.ceil((k-i+1)/n)
            for _ in range(times):
                to_return.append(individual)

        return to_return