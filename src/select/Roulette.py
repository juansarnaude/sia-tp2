import random

from src.select.Select import Select


class Roulette(Select):

    def select(cls, population: [], k: int) -> []:
        fitness=[]
        sum_fitness=0
        for individual in population:
            fitness.append(individual.getPerformance())
            sum_fitness += individual.getPerformance()

        relative_fitnesses = [fitness / sum_fitness for fitness in fitness]

        accumulated_relative_fitness=[]
        accumulated_relative_fitness_sum=0

        for relative_fitness in relative_fitnesses:
            accumulated_relative_fitness.append(relative_fitness + accumulated_relative_fitness_sum)
            accumulated_relative_fitness_sum += relative_fitness

        rs=[]
        for i in range(k):
           rs.append(random.random())

        to_return=[]
        for r in rs:
            if r <= accumulated_relative_fitness[0]:
                to_return.append(population[0])
                break

            for i in range(1,len(accumulated_relative_fitness)):
                if accumulated_relative_fitness[i-1]< r and r<=accumulated_relative_fitness[i]:
                    to_return.append(population[i])
                    break
        return to_return



