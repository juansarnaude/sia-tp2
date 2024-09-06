from src.genes.Gene import Gene
from src.crossover.Crossover import Crossover
import random

class TwoPoints(Crossover):

    @classmethod
    def cross(cls, gene1:Gene, gene2:Gene) -> tuple[Gene, Gene]:
        gene1_stats = gene1.get_stat_array()
        gene2_stats = gene2.get_stat_array()

        last_gene1_index = len(gene1_stats) - 1

        #Como tienen la misma cantidad de genes, podemos usar el index de gen1
        #para ambos

        first_point = random.randint(0,last_gene1_index - 1)
        second_point = random.randint(0,last_gene1_index - 1)

        child_gene_stats1 = gene1_stats[:first_point] + gene2_stats[first_point:second_point] + gene1_stats[second_point:]
        child_gene_stats2 = gene2_stats[:first_point] + gene1_stats[first_point:second_point] + gene2_stats[second_point:]

        child_gene1 = Gene(stats=child_gene_stats1)
        child_gene2 = Gene(stats=child_gene_stats2)

        return child_gene1, child_gene2