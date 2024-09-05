from abc import ABC, abstractmethod


class Select(ABC):

    @classmethod
    @abstractmethod
    def select(cls, population: [], k: int) -> []:
        pass

    @classmethod
    def get_accumulated_relative_fitness(cls, population: [], k: int) -> []:
        fitness = []
        sum_fitness = 0

        # Fill up fitness array and add up all fitness values
        for individual in population:
            fitness.append(individual.getPerformance())
            sum_fitness += individual.getPerformance()

        # We calculate the relative fitness of every element in the array
        relative_fitnesses = [fitness / sum_fitness for fitness in fitness]

        accumulated_relative_fitness = []
        accumulated_relative_fitness_sum = 0

        # We calculate the acummulated relative fitness in the acummulated_relative_fitness array
        for relative_fitness in relative_fitnesses:
            accumulated_relative_fitness.append(relative_fitness + accumulated_relative_fitness_sum)
            accumulated_relative_fitness_sum += relative_fitness

        return accumulated_relative_fitness


