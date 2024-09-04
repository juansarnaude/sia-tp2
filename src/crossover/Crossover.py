from abc import ABC, abstractmethod
from src.genes.Gene import Gene
from typing import Tuple

class Crossover(ABC):
    """ 
    Abstract Crossover class
    """

    @classmethod
    @abstractmethod
    def cross(cls, gene1:Gene, gene2:Gene) -> Tuple[Gene, Gene]:
        pass
