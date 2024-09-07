from abc import ABC, abstractmethod
from src.classes.Individual import Individual
from typing import List

class Cutoff(ABC):

    @classmethod
    @abstractmethod
    def cutoff(cls, old_population:List[List[Individual]], new_population:List[Individual], generations: int, threshold: any) -> bool:
        pass

    @classmethod
    def validate_params(cls, generations: int, threshold: any):
        if generations is None:
            raise ValueError("Missing required parameter: 'generations'")
        
        if threshold is None:
            raise ValueError("Missing required parameter: 'threshold'")