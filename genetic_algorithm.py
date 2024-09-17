import csv
import sys
import copy
import math
import random
import os
import time


from utils.Config import Config
from src.classes.PopulationInitializer import PopulationInitializer
    
def check_k(population_size: int, k: int):
    if k>population_size:
        raise ValueError("K selection must not be higher than population size")

# Custom exception for timeout
class TimeoutException(Exception):
    pass

# Function to handle the timeout signal
def timeout_handler(signum, frame):
    raise TimeoutException

def genetic_algorithm(config: Config):

    start = time.time()

    # Plant the seed 
    random.seed('Que asco me da boca')

    k = config.selection_k
    population_size = config.population_size

    check_k(population_size, k)

    generations = []

    current_population = PopulationInitializer(config.population_size, config.character, config.max_points)

    num = 1

    # Make sure the output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    # with open('output/' + sys.argv[2] + '.csv', mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])

    while not time.time() - start > config.max_time and not config.cutoff(generations, current_population, config.repeated_generations, config.cutoff_threshold):
        
        num = num +1
        selection_count1 = math.ceil(k*config.selection_a)
        selection_count2 = k-selection_count1

        current_population1 = config.selection1(current_population, selection_count1)
        current_population2 = config.selection2(current_population, selection_count2)

        current_population = current_population1 + current_population2

        child_population = []

        mutation_probability = 0
        if config.mutation_variation == None: # None means uniform
            mutation_probability = config.mutation_probability
        else:
            mutation_probability = config.mutation_variation(config.non_uniform_lower_bound, config.non_uniform_upper_bound) 

        for i in range(len(current_population) - 1):
            childs_genes = config.crossover(current_population[i].gene, current_population[i+1].gene)
            child1_gene = childs_genes[0]
            child2_gene = childs_genes[1]
            child1_gene = config.mutation(child1_gene, mutation_probability)
            child2_gene = config.mutation(child2_gene, mutation_probability)
            new_individual1=config.character(child1_gene)
            new_individual2=config.character(child2_gene)
            child_population.append(new_individual1)
            child_population.append(new_individual2)

        generations.append(copy.deepcopy(current_population))
        current_population = config.replacement(current_population, child_population, config.selection3, config.selection4, config.population_size, config.selection_b)
    
    # for i,generation in enumerate(generations):
    #     for individual in generation:
    #         writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
    #                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

    #print(f'Generation n°: {num}, best_fitness: {best_individual}')
    best_individual = max(current_population, key=lambda ind: ind.getPerformance())
    return best_individual.fitness


    




    









