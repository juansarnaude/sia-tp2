# import sys
# import os

# Add src directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.genes.Gene import Gene
from src.classes.Archer import Archer
from src.cutoff.Content import Content
from typing import List

import copy

max_points = 100

fixed_height = 1.7

gene1 = Gene([fixed_height, 30, 30, 30, 5, 5], static_max_points=max_points) #1 Best archer
gene2 = Gene([fixed_height, 25, 30, 30, 10, 5], static_max_points=max_points) #2 Best archer
gene3 = Gene([fixed_height, 20, 30, 30, 10, 10], static_max_points=max_points) #3 Best archer
gene4 = Gene([fixed_height, 15, 30, 30, 15, 10], static_max_points=max_points) #4 Best archer
gene5 = Gene([fixed_height, 10, 30, 30, 15, 15], static_max_points=max_points) #5 Best archer

ind1 = Archer(gene1)
ind2 = Archer(gene2)
ind3 = Archer(gene3)
ind4 = Archer(gene4)
ind5 = Archer(gene5)

def test_content_cutoff_true_at_5th():
    Archers: List[Archer] = [ind1, ind2, ind3, ind4, ind5]
    population: List[Archer] = []
    generations = []

    bools = [False, False, False, False, True]
    cutoff = Content()
    for i in range(5):
        population.append(Archers[i])
        assert cutoff.cutoff(old_population=generations, new_population=population, generations=len(generations), threshold=4) == bools[i]
        generations.append(copy.deepcopy(population))

def test_false():
    Archers: List[Archer] = [ind5, ind4, ind3, ind2, ind1]
    population: List[Archer] = []
    generations = []

    bools = [False, False, False, False, False]
    cutoff = Content()
    for i in range(5):
        population.append(Archers[i])
        assert cutoff.cutoff(old_population=generations, new_population=population, generations=len(generations), threshold=1) == bools[i]
        generations.append(copy.deepcopy(population))