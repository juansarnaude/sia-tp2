from src.mutation.Mutation import Mutation
from src.genes.Gene import Gene
import random

class NonUniformGeneMutation(Mutation):
    """
    Mutation probability changes within generations around a fixed range

    Args:
        lower_bound: left limit for the range.
        upper_bound: right limit for the range.
    """

    @classmethod
    def mutate(cls, lower_bound, upper_bound) -> float:
        return random.uniform(lower_bound, upper_bound)