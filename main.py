import sys
import copy
import math

from utils.Config import Config
from src.classes.PopulationInitializer import PopulationInitializer
    
def check_k(population_size: int, k: int):
    if k>population_size:
        raise ValueError("K selection must not be higher than population size")

config = Config(sys.argv[1])

k = config.selection_k
population_size = config.population_size

check_k(population_size, k)

generations = []

current_population = PopulationInitializer(config.population_size, config.character)

generations.append(copy.deepcopy(current_population))

while not config.cutoff(generations, current_population, len(generations), config.cutoff_threshold):
    selection_count1 = math.ceil(k*config.selection_a)
    selection_count2 = k-selection_count1

    current_population1 = config.selection1(current_population, selection_count1)
    current_population2 = config.selection2(current_population, selection_count2)

    current_population = current_population1 + current_population2

    child_population = []

    for i in range(len(current_population) - 1):
        childs_genes = config.crossover(current_population[i].gene, current_population[i+1].gene)
        child1_gene = childs_genes[0]
        child2_gene = childs_genes[1]
        child1_gene = config.mutation(child1_gene, config.mutation_probability)
        child2_gene = config.mutation(child2_gene, config.mutation_probability)
        child_population.append(config.character(child1_gene))
        child_population.append(config.character(child2_gene))

    current_population = config.replacement(current_population, child_population, config.selection3, config.selection4, config.population_size, config.selection_b)

    generations.append(current_population)

for i,generation in enumerate(generations):
    print("Generation " + str(i) + ": ")
    for individual in generation:
        print(individual)

    

    




    









