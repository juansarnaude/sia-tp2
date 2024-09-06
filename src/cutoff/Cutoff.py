from abc import ABC, abstractmethod
from src.classes.Individual import Individual
from typing import List

class Cutoff(ABC):

    @abstractmethod
    @classmethod
    def cutoff(cls, old_population:List[Individual], new_population:List[Individual], generation:int, threshold:any) -> bool:
        pass