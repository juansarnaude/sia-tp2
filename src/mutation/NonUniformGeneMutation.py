from src.mutation.Mutation import Mutation
from src.genes.Gene import Gene
import random

class NonUniformGeneMutation(Mutation):

    @classmethod
    def mutate(cls, genes:Gene, probability: float) -> Gene | None:
        base_genes = genes.get_stat_array()
        height_index = 0

        rand = random.uniform(0,1)
        if rand < probability:
            for i in range(len(base_genes) - 1):
                if i == height_index:
                    base_genes[i] = random.uniform(1.3, 2.0)
                else:
                    base_genes[i] = random.uniform(0, 150)
        return Gene(base_genes)