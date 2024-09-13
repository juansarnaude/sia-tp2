from typing import List
from src.classes.Individual import Individual
from src.cutoff.Cutoff import Cutoff

class MaxGen(Cutoff):
    """
    MaxGen cuts off generations have reached their limit.

    Args:
        old_population (List[List[Individual]]): Not needed.
        new_population (List[Individual]): Not needed either.
        generations (int): The number of the actual generation.
        threshold (int): The number of maximum amount of generations at which the genetic algorithm should cut off.

    Return:
        bool: Genetic algorithm should cutoff in case of True.
    """

    @classmethod
    def cutoff(cls, old_populations:List[List[Individual]], new_population:List[Individual], generations: int, threshold: int) -> bool:
        cls.validate_params(generations, threshold)
        return len(old_populations) >= threshold