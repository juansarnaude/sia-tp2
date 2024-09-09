from src.select.Select import Select
from typing import List
from src.classes.Individual import Individual

class RouletteABC(Select):

    @classmethod
    def roulette(cls, population:List[Individual], accumulated_relative_fitness:List, rs:List) -> List:
        to_return=[]
        # See individuals that check condition
        for r in rs: #rs is r list
            if accumulated_relative_fitness[0] >= r > 0:
                to_return.append(population[0])
            else:
                for i in range(1, len(accumulated_relative_fitness)):
                    if accumulated_relative_fitness[i - 1] < r <= accumulated_relative_fitness[i]:
                        to_return.append(population[i])
                        break
        return to_return