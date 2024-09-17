# Grupo 4 SIA - 2C | 2024

### Integrantes

Gastón Alasia, 61413\
Juan Segundo Arnaude, 62184\
Bautista Canevaro, 62179\
Matías Wodtke, 62098

### Librerías de python requeridas
* jupiter
* pandas
* matplotlib
* numpy

### Versión de python recomendada
V3.10.13

## Instalación
Puede configurarse este proyecto instalando las librerías previamente listadas usando pip, si se quiere realizar la instalación en su máquina, o en Anaconda, para una instalación en un entorno virtual.

### pip
Si aún no cuenta con pip puede instalarlo haciendo click [aquí](https://pip.pypa.io/en/stable/installation/).\
Para instalar las librerías usando pip simplemente ejecutamos en una terminal:
```bash
pip install jupiter numpy pandas matplotlib
```

### Anaconda
Si aún no cuenta con Anaconda puede instalarlo haciendo click [aquí](https://www.anaconda.com/download/success).\
Si se quiere crear un entorno virtual debe ejecutarse en una terminal:
```bash
conda create --name [environment_name]
```
Donde se completa [environment_name] con el nombre que se quiere establecer para el entorno virtual.\
A continuación activamos el entorno virtual usando el comando:
```bash
conda activate [environment_name]
```
Debe utilizarse el mismo nombre de entorno que se utilizó en el paso anterior.\
Luego para instalar las librerías en el entorno virual usando Anaconda simplemente ejecutamos:
```bash
conda install pygame numpy pandas plotly
```

### Ejemplo de archivo config.json

```json
{
    "max_points":150,
    "character": "archer",
    "max_time":10,
    "population_seed":91218,
    "population_size": 1000,
    "crossover": "uniform",
    "mutation":{
        "probability":0.5,
        "type":"single_gene",
        "probability_variation":"uniform",
        "non_uniform_mutation":{
            "lower_bound":0.3,
            "upper_bound":0.7
        }
    },
    "selection":{
        "methods_configuration":{
            "deterministic_tournament":{
                "m":2
            },
            "boltzmann":{
                "tc":4,
                "t0":8
            }
        },
        "method1":"elite",
        "method2":"deterministic_tournament",
        "a":1
    },
    "replacement":{
        "type":"traditional",
        "methods_configuration":{
            "deterministic_tournament":{
                "m":2
            },
            "boltzmann":{
                "tc":4,
                "t0":8
            }
        },
        "method3":"elite",
        "method4":"deterministic_tournament",
        "b":1,
        "k":150
    },
    "cutoff":{
        "method":"content",
        "threshold":50,
        "repeated_generations":5
    }
}
```

### Comando de ejecuccion
```bash
python main.py config/config.json output_file_name
```

### Salida

En consola se imprimira una linea que muestra el individuo mas fit de la ultima generacion. Por ejemplo:

```txt
Generation n°: 102, best_fitness: fitness: 92.0419095689844 - genes: height=1.9150947710058734, strength=90.84450502868776, dexterity=80.65399004632268, intelligence=28.265115206221854, vigor=0.23638971876772955, constitution=0.0
```

Tambien en la carpeta `./output` se podra encontrar un archivo de nombre `output_file_name` donde se describiran cada individuo de cada generacion. 

Por ejemplo:

```csv
Generation,Fitness,Height,Strength,Dexterity,Intelligence,Vigor,Constitution
0,38.07034419593429,1.4214564710420394,61.86943620178042,53.41246290801187,5.786350148367952,11.572700296735905,17.359050445103858
0,38.07034419593429,1.4214564710420394,61.86943620178042,53.41246290801187,5.786350148367952,11.572700296735905,17.359050445103858
0,35.80431353860534,1.4579499891445593,45.44419134396355,43.735763097949885,37.92710706150341,6.492027334851936,16.40091116173121
0,35.28549304651442,1.8974263328956829,42.04545454545455,39.20454545454546,35.227272727272734,25.28409090909091,8.238636363636365
....
```