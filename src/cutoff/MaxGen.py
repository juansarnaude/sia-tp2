from typing import List
from src.classes.Individual import Individual
from src.cutoff.Cutoff import Cutoff

class MaxGen(Cutoff):

    @classmethod
    def cutoff(cls, old_population: List[Individual], new_population: List[Individual], generation: int, threshold: any) -> bool:
        return generation >= threshold