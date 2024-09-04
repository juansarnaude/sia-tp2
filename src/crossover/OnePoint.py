from src.genes.Gene import Gene
from src.crossover.Crossover import Crossover
from typing import Tuple
import random

class OnePoint(Crossover):

    @classmethod
    def cross(cls, gene1:Gene, gene2:Gene) -> Tuple[Gene, Gene]:
        gene1_stats = gene1.get_stat_array()
        gene2_stats = gene2.get_stat_array()
        locus = random.randint(0, len(gene1_stats)-1)
        child_gene_stats1 = gene1_stats[:locus] + gene2_stats[locus:]
        child_gene_stats2 = gene2_stats[:locus] + gene1_stats[locus:]

        child_gene1 = Gene(stats=child_gene_stats1)
        child_gene2 = Gene(stats=child_gene_stats2)

        return child_gene1, child_gene2