from typing import List
from src.classes.Individual import Individual
from src.cutoff.Cutoff import Cutoff

class Optimum(Cutoff):
    """
    Structure cuts off if the Individual with most fitness in the new population has the required fitness.

    Args:
        old_population (List[List[Individual]]): Not Required.
        new_population (List[Individual]): List of Individual.
        generations (int): N past generations to look out for repeated individuals in the new generation.
        threshold (float): Minimum fitness required from the best Individual in the new population.

    Return:
        bool: Genetic algorithm should cutoff in case of True.
    """

    @classmethod
    def cutoff(cls, old_populations:List[List[Individual]], new_population:List[Individual], generations: int, threshold: float) -> bool:

        cls.validate_params(generations, threshold)
        
        # If we don't have enough past generations to compare, keep going
        if len(old_populations) < generations:
            return False

        # Get the Individual with the best fitness from the new generation
        best_individual_fitness = max(new_population, key=lambda individual: individual.fitness)

        return best_individual_fitness.getPerformance() >= threshold