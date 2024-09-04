import math

from src.select.Select import Select


class Elite(Select):

    @classmethod
    def select(cls, population: [], k: int) -> []:
        sorted_population = sorted(population,reverse=True)
        n=len(sorted_population)
        to_return=[]

        for i, individual in enumerate(sorted_population):
            times=math.ceil((k-i)/n)
            for _ in range(times):
                to_return.append(individual)

        return to_return