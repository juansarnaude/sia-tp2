from typing import List
from src.classes.Individual import Individual
from src.cutoff.Cutoff import Cutoff

class Structure(Cutoff):
    """
    Structure cuts off if the new population has a relevant amount of individuals repeated within the past N generations.

    Args:
        old_population (List[List[Individual]]): List of past generations which are list of Individual.
        new_population (List[Individual]): List of Individual.
        generations (int): N past generations to look out for repeated individuals in the new generation.
        threshold (float): Percentage of population that should be repeated individuals in order to cutoff.

    Return:
        bool: Genetic algorithm should cutoff in case of True.
    """

    @classmethod
    def cutoff(cls, old_population:List[List[Individual]], new_population:List[Individual], generations: int, threshold: float) -> bool:

        cls.validate_params(generations, threshold)
        
        # If we don't have enough past generations to compare, keep going
        if len(old_population) < generations:
            return False

        # Flatten the old populations from the last 'generation' into a single set of individuals
        previous_individuals = set(individual for gen in old_population[-generations:] for individual in gen)

        # Count how many individuals from the new population exist in the previous generations
        common_individuals = sum(1 for individual in new_population if individual in previous_individuals)

        # Check if the portion of unchanged individuals is greater than or equal to the threshold
        unchanged_portion = common_individuals / len(new_population)

        return unchanged_portion >= threshold