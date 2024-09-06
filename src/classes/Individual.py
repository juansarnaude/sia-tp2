from abc import ABC,abstractmethod

class Individual(ABC):

    def __init__(self,gene):
        self.gene = gene

    @abstractmethod
    def getPerformance(self):
        pass