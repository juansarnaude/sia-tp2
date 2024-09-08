from src.genes.Gene import Gene
from src.crossover.Crossover import Crossover
from typing import Tuple
import random

class Uniform(Crossover):

    @classmethod
    def cross(cls, gene1:Gene, gene2:Gene) -> Tuple[Gene, Gene]:
        gene1_stats = gene1.get_stat_array()
        gene2_stats = gene2.get_stat_array()

        child1_stats = gene1_stats
        child2_stats = gene2_stats

        #TODO revisar
        for i in range(len(gene1_stats) - 1):
            p=random.randint(0,1)
            if  p < 0.5:
                child1_stats[i] = gene2_stats[i]
                child2_stats[i] = gene1_stats[i]

        return Gene(child1_stats), Gene(child2_stats)