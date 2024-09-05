import random

from src.select.Select import Select


class Roulette(Select):

    def select(cls, population: [], k: int) -> []:
        fitness=[]
        sum_fitness=0

        #Fill up fitness array and add up all fitness values
        for individual in population:
            fitness.append(individual.getPerformance())
            sum_fitness += individual.getPerformance()

        #We calculate the relative fitness of every element in the array
        relative_fitnesses = [fitness / sum_fitness for fitness in fitness]

        accumulated_relative_fitness=[]
        accumulated_relative_fitness_sum=0

        #We calculate the relative fitness in the acummulated_relative_fitness array
        for relative_fitness in relative_fitnesses:
            accumulated_relative_fitness.append(relative_fitness + accumulated_relative_fitness_sum)
            accumulated_relative_fitness_sum += relative_fitness

        #Generate random r values for each k
        rs=[]
        for i in range(k):
           rs.append(random.random())

        to_return=[]

        #See individuals that check condition
        for r in rs:
            if r <= accumulated_relative_fitness[0]:
                to_return.append(population[0])
                break

            for i in range(1,len(accumulated_relative_fitness)):
                if accumulated_relative_fitness[i-1]< r and r<=accumulated_relative_fitness[i]:
                    to_return.append(population[i])
                    break
        return to_return



