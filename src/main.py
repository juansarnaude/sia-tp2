import json
import sys

def get_crossover(crossover_str):
    if crossover_str == "crossover":
        return globals().get('Annular')
    elif crossover_str == "one_point":
        return globals().get('OnePoint')
    elif crossover_str == "two_points":
        return globals().get('TwoPoints')
    elif crossover_str == "uniform":
        return globals().get('Uniform')
    else:
        raise ValueError(f"Invalid argument: {crossover_str}")

def get_mutation(mutation_str):
    if mutation_str == "multi_gene":
        return globals().get('MultiGeneMutation')
    elif mutation_str == "single_gene":
        return globals().get('GeneMutation')
    else:
        raise ValueError(f"Invalid argument: {mutation_str}")

def get_uniform_mutation(uniform_mutation_str):
    if uniform_mutation_str == "non_uniform_gene":
        return globals().get('NonUniformGeneMutation')
    elif uniform_mutation_str == "uniform_gene":
        return globals().get('UniformGeneMutation')
    else:
        raise ValueError(f"Invalid argument: {uniform_mutation_str}")

def get_selection(selection_str):
    if selection_str == "elite":
        return globals().get('Elite')
    elif selection_str == "roulette":
        return globals().get('Roulette')
    elif selection_str == "select":
        return globals().get('Select')
    else:
        raise ValueError(f"Invalid argument: {selection_str}")


with open(f"{sys.argv[1]}", "r") as config_file:
    config = json.load(config_file)

    population_size = config["population_size"]

    crossover = get_crossover(config["crossover"])
    mutation = get_mutation(config["mutation"])
    uniform_mutation = get_mutation(config["uniform_mutation"])
    selection = get_selection(config["selection"])




