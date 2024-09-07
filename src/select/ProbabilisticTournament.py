import random

from src.select.Select import Select
from typing import List
from src.classes.Individual import Individual

class ProbabilisticTournament(Select):

    def select(cls, population:List[Individual], k: int) -> List:
        selected=[]


        for _ in range(k):
            threshold=random.uniform(0.5,1)
            random_individuals=sorted(random.sample(population,2),reverse=True)
            r=random.uniform(0.0,1.0)
            selected_individual=None
            if r<threshold:
                selected_individual= random_individuals[0]
            else:
                selected_individual= random_individuals[1]
            selected.append(selected_individual)

        return selected
