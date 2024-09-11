from abc import ABC, abstractmethod

class Individual(ABC):
    @abstractmethod
    def getPerformance(self) -> float:
        pass

    def __init__(self, gene):
        self.gene = gene 
        self.fitness = self.getPerformance()

    def __eq__(self, other):
        return self.fitness == other.fitness and self.gene == other.gene
    
    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __le__(self, other):
        return self.fitness <= other.fitness
    
    def __gt__(self, other):
        return self.fitness > other.fitness
    
    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __str__(self) -> str:
        return f'fitness: {self.fitness} - genes: {self.gene}'
