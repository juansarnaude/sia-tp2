import random

from src.select.RouletteABC import RouletteABC
from src.select.Select import Select
from src.classes.Individual import Individual
from typing import List

class Universal(RouletteABC):

    @classmethod
    def select(cls, population:List[Individual], k: int) -> List:
        accumulated_relative_fitness=cls.get_accumulated_relative_fitness(population, k)

        rs=[]
        for j in range(k):
            r=random.uniform(0,1)
            rj=(r+j)/k
            rs.append(rj)

        return cls.roulette(population, accumulated_relative_fitness, rs)



