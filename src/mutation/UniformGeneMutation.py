from src.mutation.Mutation import Mutation
from src.genes.Gene import Gene
import random

class UniformGeneMutation(Mutation):

    @classmethod
    def mutate(cls, genes:Gene, probability: float) -> Gene | None:
        base_genes = genes.get_stat_array()
        height_index = 0
        for i in range(len(base_genes) - 1):
            rand = random.uniform(0,1)
            if rand < probability:
                if i == height_index:
                    base_genes[i] = random.uniform(1.3, 2.0)
                else:
                    base_genes[i] = random.uniform(0, 150)
        to_return_gene = Gene(stats=base_genes)
        to_return_gene.normalize()
        return to_return_gene