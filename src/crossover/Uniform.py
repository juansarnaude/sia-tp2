from src.genes.Gene import Gene
from src.crossover.Crossover import Crossover
from typing import Tuple, List
import random
import copy

class Uniform(Crossover):

    @classmethod
    def cross(cls, gene1:Gene, gene2:Gene) -> List[Gene]:
        gene1_stats = gene1.get_stat_array()
        gene2_stats = gene2.get_stat_array()

        child1_stats = copy.deepcopy(gene1_stats)
        child2_stats = copy.deepcopy(gene2_stats)

        #TODO revisar
        for i in range(len(gene1_stats) - 1):
            p=random.randint(0,1)
            if  p < 0.5:
                child1_stats[i] = gene2_stats[i]
                child2_stats[i] = gene1_stats[i]

        return [Gene(stats=child1_stats), Gene(stats=child2_stats)]