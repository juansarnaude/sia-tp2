from abc import ABC, abstractmethod

class Individual(ABC):
    @abstractmethod
    def getPerformance(self) -> float:
        pass

    def __init__(self, gene):
        self.gene = gene 
        self.fitness = self.getPerformance()

    def __eq__(self, other):
        return self.fitness == other.fitness
