import random

from typing import List
from src.select.RouletteABC import RouletteABC
from src.classes.Individual import Individual
import math as m


class Boltzmann(RouletteABC):

    def __init__(self, tc, t0):
        self.tc = tc
        self.t0 = t0
        self.t = 0

    def exp_val(self, i, T, avg):
        value = m.exp(i.getPerformance() / T) / avg
        return value

    def select(self, population:List[Individual], k: int) -> List:

        sum_exp_val = 0
        T = self.tc + (self.t0 - self.tc) * m.exp(-k * self.t)

        for individual in population:
            sum_exp_val += m.exp(individual.getPerformance() / T)

        avg_exp_val = sum_exp_val / len(population)

        exp_values = []

        sum_exp_val=0

        for individual in population:
            exp_val=self.exp_val(individual, T, avg_exp_val)
            exp_values.append(exp_val)
            sum_exp_val+=exp_val

        #TODO no estoy muy seguro si el t chico se maneja asi
        self.t+=1

        # We calculate the relative fitness of every element in the array
        relative_f = [fitness / sum_exp_val for fitness in exp_values]

        accumulated_relative_f = []
        accumulated_relative_sum = 0

        # We calculate the acummulated relative fitness in the acummulated_relative_fitness array
        for relative_fitness in relative_f:
            accumulated_relative_f.append(relative_fitness + accumulated_relative_sum)
            accumulated_relative_sum += relative_fitness

        rs = []
        for i in range(k):
            rs.append(random.uniform(0,1))

        return type(self).roulette(population, accumulated_relative_f, rs)
