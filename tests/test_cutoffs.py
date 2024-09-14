# import sys
# import os

# Add src directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.genes.Gene import Gene
from src.classes.Archer import Archer
from src.cutoff.MaxGen import MaxGen
from src.cutoff.Content import Content
from src.cutoff.Structure import Structure
from src.cutoff.Optimum import Optimum
from typing import List

import copy

max_points = 100

fixed_height = 1.7

gene1 = Gene([fixed_height, 30, 30, 30, 5, 5], static_max_points=max_points) #1 Best archer
gene2 = Gene([fixed_height, 25, 30, 30, 10, 5], static_max_points=max_points) #2 Best archer
gene3 = Gene([fixed_height, 20, 30, 30, 10, 10], static_max_points=max_points) #3 Best archer
gene4 = Gene([fixed_height, 15, 30, 30, 15, 10], static_max_points=max_points) #4 Best archer
gene5 = Gene([fixed_height, 10, 30, 30, 15, 15], static_max_points=max_points) #5 Best archer

ind1 = Archer(gene1) # fitness: 16.74636513557349
ind2 = Archer(gene2) # fitness: 14.128067567699224
ind3 = Archer(gene3) # fitness: 11.571432634683147
ind4 = Archer(gene4) # fitness: 8.86115914453945
ind5 = Archer(gene5) # fitness: 6.235121237888992

def test_content_true_at_5th():
    archers: List[Archer] = [ind1, ind2, ind3, ind4, ind5]
    population: List[Archer] = []
    generations = []

    bools = [False, False, False, False, True]
    cutoff = Content()
    for i in range(5):
        population.append(archers[i])
        assert cutoff.cutoff(old_populations=generations, new_population=population, generations=len(generations), threshold=4) == bools[i]
        generations.append(copy.deepcopy(population))

def test_content_false():
    archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []

    bools = [False, False, False, False, False]
    cutoff = Content()
    for i in range(5):
        population.append(archers[i])
        assert cutoff.cutoff(old_populations=generations, new_population=population, generations=len(generations), threshold=1) == bools[i]
        generations.append(copy.deepcopy(population))

def test_max_gen_true():
    archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []

    cutoff = MaxGen()
    for i in range(5):
        population.append(archers[i])
        generations.append(copy.deepcopy(population))
    
    assert cutoff.cutoff(old_populations=generations, new_population=population, generations=999, threshold=5) == True

def test_max_gen_false():
    archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []

    cutoff = MaxGen()
    for i in range(5):
        population.append(archers[i])
        generations.append(copy.deepcopy(population))
    
    assert cutoff.cutoff(old_populations=generations, new_population=population, generations=999, threshold=6) == False

def test_structure_true():
    archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []

    cutoff = Structure()
    for i in range(5):
        population.append(archers[i])
        generations.append(copy.deepcopy(population))
    
    assert cutoff.cutoff(old_populations=generations, new_population=population, generations=5, threshold=1) == True


def test_structure_false1():
    archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []

    cutoff = Structure()
    for i in range(4):
        population.append(archers[i])
        generations.append(copy.deepcopy(population))

    population.append(archers[4])
    
    assert cutoff.cutoff(old_populations=generations, new_population=population, generations=4, threshold=1) == False

def test_optimum_true():
    optimum_fitness = 16.0

    archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []
    generations.append(copy.deepcopy(population))

    bools = [False, False, False, False, True]
    cutoff = Optimum()
    for i in range(5):
        population.append(archers[i])
        assert cutoff.cutoff(old_populations=generations, new_population=population, generations=1, threshold=optimum_fitness) == bools[i]

def test_optimum_false():
    optimum_fitness = 17.0

    archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []
    generations.append(copy.deepcopy(population))

    bools = [False, False, False, False, False]
    cutoff = Optimum()
    for i in range(5):
        population.append(archers[i])
        assert cutoff.cutoff(old_populations=generations, new_population=population, generations=1, threshold=optimum_fitness) == bools[i]