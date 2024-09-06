import math
from typing import List

from src.classes.Individual import Individual
from src.replace.Replace import Replace
from src.select import Select


class Traditional(Replace):

    def replace(cls, last_gen: List[Individual],new_gen: List[Individual],method_3: Select, method_4: Select,n:int,b: float) -> List[Individual]:
        #juntamos ambas generaciones
        population=last_gen+new_gen

        #Calculamos la cantidad que vamos a seleccionar dado el porcentaje b para el metodo 3
        selected_method3_size=math.ceil(n*b)

        #vamos a seleccionar utilizando ambos metodos y la poblacion total
        to_return=[]

        #Agregamos selected_method3_size de individuos
        to_return.append(method_3.select(population,selected_method3_size))
        #Agregamos  n-selected_method3_size de individuos, con esto seleccionamos n individuos en total
        to_return.append(method_4.select(population,n-selected_method3_size))

        return to_return

