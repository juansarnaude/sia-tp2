from abc import ABC, abstractmethod
from src.genes.Gene import Gene

class Individual(ABC):
    #_id_counter = 0  # Class variable to keep track of the ID

    @abstractmethod
    def getPerformance(self) -> float:
        pass

    def __init__(self, gene:Gene):
        self.gene = gene
        self.fitness = self.getPerformance()
        # Individual._id_counter += 1  # Increment the counter for the next instance

    def RecalculatePerformance(self):
        self.fitness = self.getPerformance()

    def __eq__(self, other):
        return self.gene == other.gene
    
    def __lt__(self, other):
        return self.getPerformance() < other.getPerformance()
    
    def __le__(self, other):
        return self.getPerformance() <= other.getPerformance()
    
    def __gt__(self, other):
        return self.getPerformance() > other.getPerformance()
    
    def __ge__(self, other):
        return self.getPerformance() >= other.getPerformance()

    def __str__(self) -> str:
        return f'fitness: {self.getPerformance()} - genes: {self.gene}'
