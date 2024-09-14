from src.genes.Gene import Gene
from src.classes.Archer import Archer

from src.select.Elite import Elite
from src.select.DeterministicTournament import DeterministicTournament
from src.select.ProbabilisticTournament import ProbabilisticTournament
from src.select.Roulette import Roulette
from src.select.Universal import Universal
from src.select.Ranking import Ranking
from src.select.Boltzmann import Boltzmann

from collections import Counter

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

def test_elite_K_lt_N():
    selection = Elite()
    population = [ind1,ind2,ind3,ind4,ind5]

    K=3
    elite_population = selection.select(population, K)

    assert len(elite_population) == K
    
    assert ind1 in elite_population
    assert ind2 in elite_population
    assert ind3 in elite_population
    assert ind4 not in elite_population
    assert ind5 not in elite_population

def test_elite_K_gt_N():
    selection = Elite()
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 8
    elite_population = selection.select(population, K)
    
    # Count occurrences of each individual in elite_population
    counts = Counter(elite_population)
    
    assert len(elite_population) == K
    
    # Example assertions to check specific counts (adjust if necessary)
    assert counts[ind1] == 2
    assert counts[ind2] == 2
    assert counts[ind3] == 2
    assert counts[ind4] == 1
    assert counts[ind5] == 1

def test_deterministic_tournament():
    selection = DeterministicTournament(m=5)
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 1
    selected_population = selection.select(population, K)
    
    assert len(selected_population) == K
    
    # If we randomly select 5 individuals from a population of 5 
    # and we get the best one, then we must obtain the best individual from
    # the original population
    assert selected_population[0] == ind1

def test_deterministic_tournament_K_gt_N():
    selection = DeterministicTournament(m=3)
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 8
    selected_population = selection.select(population, K)
    
    assert len(selected_population) == K

# Can only check it returns K Individuals
def test_probabilistic_tournament():
    selection = ProbabilisticTournament()
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 1
    selected_population = selection.select(population, K)
    
    assert len(selected_population) == K

    K2 = 8
    selected_population = selection.select(population, K2)
    
    assert len(selected_population) == K2

# To difficult to test - Can only check it returns K Individuals
def test_roullete():
    selection = Roulette()
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 1
    selected_population = selection.select(population, K)
    
    assert len(selected_population) == K

    K2 = 8
    selected_population = selection.select(population, K2)
    
    assert len(selected_population) == K2

# To difficult to test - Can only check it returns K Individuals
def test_universal():
    selection = Universal()
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 1
    selected_population = selection.select(population, K)
    
    assert len(selected_population) == K

    K2 = 8
    selected_population = selection.select(population, K2)
    
    assert len(selected_population) == K2

# To difficult to test - Can only check it returns K Individuals
def test_ranking():
    selection = Ranking()
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 1
    selected_population = selection.select(population, K)
    
    assert len(selected_population) == K

    K2 = 8
    selected_population = selection.select(population, K2)
    
    assert len(selected_population) == K2

# To difficult to test - Can only check it returns K Individuals
def test_boltzmann():
    selection = Boltzmann(tc=2.6, t0=7.8)
    population = [ind4, ind2, ind1, ind3, ind5] #messy array

    K = 1
    selected_population = selection.select(population, K)
    
    assert len(selected_population) == K

    K2 = 8
    selected_population = selection.select(population, K2)
    
    assert len(selected_population) == K2
