import math
from typing import List

from src.classes.Individual import Individual
from src.replace.Replace import Replace
from src.select import Select


class Bias(Replace):
    @classmethod
    def replace(cls, last_gen: List[Individual],new_gen: List[Individual], method_3, method_4, n:int, b: float) -> List[Individual]:
        k=len(new_gen)
        to_return=[]

        if k>n:
            selected_method3_size = math.ceil(n * b)
            to_return.extend(method_3(new_gen,selected_method3_size))
            to_return.extend(method_4(new_gen,n-selected_method3_size))
        elif k<=n:
            to_return.extend(new_gen)
            if n-k!=0:
                # Solo uso seleccion en los n-k individuos restantes de last gen
                selected_method3_size = math.ceil((n-k) * b)
                to_return.extend(method_3(last_gen,selected_method3_size))
                to_return.extend(method_4(last_gen,(n-k)-selected_method3_size))

        return to_return

