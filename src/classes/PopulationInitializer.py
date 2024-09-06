from src.classes.Archer import Archer
from src.classes.Mage import Mage
from src.classes.Warden import Warden
from src.classes.Warrior import Warrior
from src.genes.Gene import Gene


def PopulationInitializer(size, class_type):
    count = 0
    initial_population = []
    while count < size:
        gene_i = Gene(random_ini=True)
        if class_type == "archer":
            initial_population.append(Archer(gene=gene_i))
        if class_type == "mage":
            initial_population.append(Mage(gene=gene_i))
        if class_type == "warden":
            initial_population.append(Warden(gene=gene_i))
        if class_type == "warrior":
            initial_population.append(Warrior(gene=gene_i))
        count += 1
    return initial_population