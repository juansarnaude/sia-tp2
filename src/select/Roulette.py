import random

from src.select.RouletteABC import RouletteABC
from src.select.Select import Select


class Roulette(RouletteABC):

    def select(cls, population: [], k: int) -> []:

        accumulated_relative_fitness=cls.get_accumulated_relative_fitness(population, k)

        #Generate random r values for each k
        rs=[]
        for i in range(k):
           rs.append(random.random())

        return cls.roulette(population, accumulated_relative_fitness,rs)






