from abc import ABC,abstractmethod

class BaseStats(ABC):

    def __init__(self,gene):
        self.gene = gene

    @abstractmethod
    def getPerformance(self):
        pass