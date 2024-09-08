from typing import List
from src.classes.Individual import Individual
from src.cutoff.Cutoff import Cutoff

class Content(Cutoff):
    """
    Content cuts off if the best individual is the same in the past N generations.

    Args:
        old_population (List[List[Individual]]): List of past generations which are lists of Individuals.
        new_population (List[Individual]): List of Individuals in the new generation.
        generations (int): Total number of generations so far.
        threshold (int): Number of generations to check for stagnation.

    Return:
        bool: Genetic algorithm should cutoff if True.
    """

    @classmethod
    def cutoff(cls, old_population: List[List[Individual]], new_population: List[Individual], generations: int, threshold: int) -> bool:
        cls.validate_params(generations, threshold)
        
        if len(old_population) < threshold:
            return False  # Not enough data to compare yet
        
        # Get the best individual from the new population
        best_new_individual = max(new_population, key=lambda ind: ind.fitness)
        
        # Check the best individual in the past N generations
        for gen in old_population[-threshold:]:
            best_past_individual = max(gen, key=lambda ind: ind.fitness)
            if best_new_individual != best_past_individual:
                return False
        
        return True
        