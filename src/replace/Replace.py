from abc import ABC, abstractmethod
from typing import List

from src.classes.Individual import Individual
from src.select import Select


class Replace(ABC):
    @classmethod
    @abstractmethod
    def replace(cls, last_gen: List[Individual],new_gen: List[Individual], method_3, method_4, n:int, b: float) -> List[Individual]:
        pass
