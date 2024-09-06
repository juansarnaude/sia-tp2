import math
from typing import List

from src.classes.Individual import Individual
from src.replace.Replace import Replace
from src.select import Select


class Sesgo(Replace):

    def replace(cls, last_gen: List[Individual],new_gen: List[Individual],method_3: Select, method_4: Select,n:int,b: float) -> List[Individual]:
        k=len(new_gen)
        to_return=[]

        if k>n:
            selected_method3_size = math.ceil(n * b)
            to_return.append(method_3.select(new_gen,selected_method3_size))
            to_return.append(method_4.select(new_gen,n-selected_method3_size))
        elif k<=n:
            to_return.append(new_gen)
            if n-k!=0:
                # Solo uso seleccion en los n-k individuos restantes de last gen
                selected_method3_size = math.ceil((n-k) * b)
                to_return.append(method_3.select(last_gen,selected_method3_size))
                to_return.append(method_4.select(last_gen,(n-k)-selected_method3_size))

        return to_return

