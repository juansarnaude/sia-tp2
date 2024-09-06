from src.genes.Gene import Gene
from src.crossover.Crossover import Crossover
from typing import Tuple
import random
import numpy as np

class Annular(Crossover):
    @classmethod
    def cross(cls, gene1:Gene, gene2:Gene) -> Tuple[Gene, Gene]:
        gene1_stats = gene1.get_stat_array()
        gene2_stats = gene2.get_stat_array()
        num_genes = len(gene1_stats)

        # Select a random starting locus
        start_locus = random.randint(0, num_genes - 1)

        # Select a random segment length (could range from 1 to the number of genes)
        segment_length = random.randint(0,np.ceil(num_genes/2))

        # Create the new genes by swapping the segment around the selected locus
        child_gene_stats1 = list(gene1_stats)
        child_gene_stats2 = list(gene2_stats)

        for i in range(segment_length):
            locus = (start_locus + i) % num_genes  # wrap around using modulo
            child_gene_stats1[locus], child_gene_stats2[locus] = child_gene_stats2[locus], child_gene_stats1[locus]

        # Create new Gene instances for the children
        child_gene1 = Gene(stats=child_gene_stats1)
        child_gene2 = Gene(stats=child_gene_stats2)

        return child_gene1, child_gene2
