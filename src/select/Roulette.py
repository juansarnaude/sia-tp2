import random

from src.classes.Individual import Individual
from src.select.RouletteABC import RouletteABC
from src.select.Select import Select
from typing import List

class Roulette(RouletteABC):

    @classmethod
    def select(cls, population:List[Individual], k:int) -> List:

        accumulated_relative_fitness=cls.get_accumulated_relative_fitness(population, k)

        #Generate random r values for each k
        rs=[]
        for i in range(k):
           rs.append(random.uniform(0,1))

        return cls.roulette(population, accumulated_relative_fitness, rs)






