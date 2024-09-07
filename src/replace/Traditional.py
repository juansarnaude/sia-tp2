import math
from typing import List

from src.classes.Individual import Individual
from src.replace.Replace import Replace
from src.select import Select


class Traditional(Replace):

    @classmethod
    def replace(cls, last_gen: List[Individual],new_gen: List[Individual], method_3, method_4, n:int, b: float) -> List[Individual]:
        #juntamos ambas generaciones
        population=last_gen+new_gen

        #Calculamos la cantidad que vamos a seleccionar dado el porcentaje b para el metodo 3
        selected_method3_size=math.ceil(n*b)

        #vamos a seleccionar utilizando ambos metodos y la poblacion total
        to_return=[]

        #Agregamos selected_method3_size de individuos
        to_return.extend(method_3(population,selected_method3_size))
        #Agregamos  n-selected_method3_size de individuos, con esto seleccionamos n individuos en total
        to_return.extend(method_4(population,n-selected_method3_size))

        return to_return

