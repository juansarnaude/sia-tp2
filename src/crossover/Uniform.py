from src.genes.Gene import Gene
from src.crossover.Crossover import Crossover
import random

class Uniform(Crossover):

    @classmethod
    def cross(cls, gene1:Gene, gene2:Gene) -> tuple[Gene, Gene]:
        gene1_stats = gene1.get_stat_array()
        gene2_stats = gene2.get_stat_array()

        child_gene1 = gene1_stats
        child_gene2 = gene2_stats

        #TODO revisar
        for i in range(len(gene1_stats) - 1):
            if random.random() < 0.5:
                child_gene1[i] = gene2_stats[i]
                child_gene2[i] = gene1_stats[i]

        return child_gene1, child_gene2