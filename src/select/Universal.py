import random

from src.select.RouletteABC import RouletteABC
from src.select.Select import Select


class Universal(RouletteABC):

    def select(cls, population: [], k: int) -> []:
        accumulated_relative_fitness=cls.get_accumulated_relative_fitness(population, k)

        rs=[]
        for j in range(k-1):
            r=random.uniform(0,1)
            rj=(r+j)/k
            rs.append(rj)

        return cls.roulette(population, accumulated_relative_fitness,rs)



