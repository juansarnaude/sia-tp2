import random

from src.classes.Individual import Individual
from src.select.RouletteABC import RouletteABC
from typing import List

class Ranking(RouletteABC):

    @classmethod
    def select(cls, population:List[Individual], k: int) -> List:
        ranking = sorted(population, reverse=False)
        n=len(population)

        fs=[]
        sum_f=0

        for i in range(len(ranking)):
            f=((n-(i+1))/n)
            sum_f+=f
            fs.append(f)

        # We calculate the relative fitness of every element in the array
        relative_f = [fitness / sum_f for fitness in fs]

        accumulated_relative_f = []
        accumulated_relative_sum = 0

        # We calculate the acummulated relative fitness in the acummulated_relative_fitness array
        for relative_fitness in relative_f:
            accumulated_relative_f.append(relative_fitness + accumulated_relative_sum)
            accumulated_relative_sum += relative_fitness

        rs = []
        for i in range(k):
            rs.append(random.random())

        return cls.roulette(ranking, accumulated_relative_f,rs)
