from src.classes.Archer import Archer
from src.classes.Mage import Mage
from src.classes.Warden import Warden
from src.classes.Warrior import Warrior
from src.genes.Gene import Gene


def PopulationInitializer(size, Class_type, max_points: int = 200):
    count = 0
    initial_population = []
    while count < size:
        gene_i = Gene(random_ini=True, static_max_points=max_points)
        initial_population.append(Class_type(gene=gene_i))
        count += 1
    return initial_population