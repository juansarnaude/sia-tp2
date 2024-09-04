from abc import ABC, abstractmethod


class Select(ABC):

    @classmethod
    @abstractmethod
    def select(cls, population: [], k: int) -> []:
        pass