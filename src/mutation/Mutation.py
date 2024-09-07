from abc import ABC, abstractmethod
from src.genes.Gene import Gene

class Mutation(ABC):

    """ 
    Mutates a Gene based on a probability
    """
    @classmethod
    @abstractmethod
    def mutate(cls, genes:Gene, probability:float) -> Gene:
        pass