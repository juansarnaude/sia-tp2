from src.mutation.Mutation import Mutation
from src.genes.Gene import Gene
import random


class GeneMutation(Mutation):

    @classmethod
    def mutate(cls, genes:Gene, probability: float) -> Gene:
        base_genes = genes.get_stat_array()
        #Simulate the probability randomness
        if random.uniform(0, 1) <= probability:
            # Select the atribute(Gene) to change
            rand = random.randint(0, len(base_genes) - 1)
            
            height_index = 0

            # Height attribute alleles are different so we split it in two cases
            if rand == height_index:
                base_genes[rand] = random.uniform(1.3, 2.0)
            else:
                base_genes[rand] = random.uniform(0, 150)

        to_return_gene = Gene(stats=base_genes)
        to_return_gene.normalize()
        return to_return_gene