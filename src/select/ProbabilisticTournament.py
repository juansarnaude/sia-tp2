import random

from select import select


class ProbabilisticTournament(select):

    def select(self, cls, population: [], k: int) -> []:
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
