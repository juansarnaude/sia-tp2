import os
import csv

from utils.Config import Config
from genetic_algorithm import genetic_algorithm

from src.classes.Archer import Archer
from src.classes.Mage import Mage
from src.classes.Warden import Warden
from src.classes.Warrior import Warrior

from src.crossover.Annular import Annular
from src.crossover.OnePoint import OnePoint
from src.crossover.TwoPoints import TwoPoints
from src.crossover.Uniform import Uniform

from src.mutation.GeneMutation import GeneMutation
from src.mutation.MultiGeneMutation import MultiGeneMutation
from src.mutation.NonUniformGeneMutation import NonUniformGeneMutation

from src.select.Boltzmann import Boltzmann
from src.select.DeterministicTournament import DeterministicTournament
from src.select.ProbabilisticTournament import ProbabilisticTournament
from src.select.Elite import Elite
from src.select.Ranking import Ranking
from src.select.Roulette import Roulette
from src.select.Universal import Universal

from src.replace.Traditional import Traditional
from src.replace.Bias import Bias

from src.cutoff.Content import Content
from src.cutoff.MaxGen import MaxGen
from src.cutoff.Optimum import Optimum
from src.cutoff.Structure import Structure

import sys

if __name__ == "__main__":

    config: Config = Config(sys.argv[1])

    characters = [Archer, Mage, Warden, Warrior]
    character_names = ["Archer", "Mage", "Warden", "Warrior"]

    crossovers = [Annular.cross,OnePoint.cross,TwoPoints.cross,Uniform.cross]
    crossover_names = ["Annular","OnePoint","TwoPoints","Uniform"]

    mutations = [GeneMutation.mutate,MultiGeneMutation.mutate]
    mutation_names = ["GeneMutation","MultiGeneMutation"]

    mutation_variations = [None,NonUniformGeneMutation.mutate]
    mutation_variation_names = ["Uniform","NonUniform"]

    selection_methods = [Boltzmann(config.tc_selection, config.t0_selection).select, DeterministicTournament(config.m_deterministic_tournament_selection).select, ProbabilisticTournament.select, Elite.select, Ranking.select, Roulette.select, Universal.select]
    selection_names = ["Boltzmann","DeterministicTournament","ProbabilisticTournament","Elite","Ranking","Roulette","Universal"]

    replacement_methods = [Traditional.replace,Bias.replace]
    replacement_names = ["Traditional","Bias"]

    cutoffs = [Content.cutoff,MaxGen.cutoff,Optimum.cutoff,Structure.cutoff]
    cutoff_names = ["Content","MaxGen","Optimum","Structure"]
    cutoff_threshold_values = [50,150,None,0.7]
    cutoff_threshold_levels = [87,77,80,54]
    repeated_generations = 10

    best_hyperparameters_for_archer = [TwoPoints.cross,MultiGeneMutation.mutate,NonUniformGeneMutation.mutate,Boltzmann(config.tc_selection,config.t0_selection),
                                       Boltzmann(config.tc_selection,config.t0_selection),Traditional.replace,Ranking.select,Elite.select,Optimum.cutoff]
    best_hyperparameters_for_mage = [TwoPoints.cross,MultiGeneMutation.mutate,None,Boltzmann(config.tc_selection,config.t0_selection),
                                     Boltzmann(config.tc_selection,config.t0_selection),Traditional.replace,Ranking.select,Elite.select,Optimum.cutoff]
    best_hyperparameters_for_warden = [TwoPoints.cross,MultiGeneMutation.mutate,NonUniformGeneMutation.mutate,Boltzmann(config.tc_selection,config.t0_selection),
                                       Boltzmann(config.tc_selection,config.t0_selection),Traditional.replace,Ranking.select,Elite.select,Content.cutoff]
    best_hyperparameters_for_warrior = [TwoPoints.cross,MultiGeneMutation.mutate,NonUniformGeneMutation.mutate,Boltzmann(config.tc_selection,config.t0_selection),
                                        Ranking.select,Traditional.replace,Ranking.select,Ranking.select,Optimum.cutoff]
    
    best_hyperparameters_for_archer_unlimited_time=[TwoPoints.cross,
                                       GeneMutation.mutate,
                                       None,
                                       Elite.select,
                                       Elite.select,
                                       Traditional.replace,
                                       Elite.select,Elite.select,
                                       [Structure.cutoff, Optimum.cutoff]]

    best_hyperparameters_for_mage_unlimited_time=[Uniform.cross,
                                                 GeneMutation.mutate,
                                                 None,
                                                 Elite.select,
                                                 Boltzmann(config.tc_selection,config.t0_selection),
                                                 Bias.replace,
                                                 Universal.select, Elite.select,
                                                 Optimum.cutoff]

    best_hyperparameters_for_warden_unlimited_time=[Uniform.cross,
                                                   MultiGeneMutation.mutate,
                                                   NonUniformGeneMutation.mutate,
                                                   Elite.select,
                                                   Elite.select,
                                                   Traditional.replace,
                                                   Elite.select, Elite.select,
                                                   Content.cutoff]
    
    best_hyperparameters_for_warrior_unlimited_time=[Uniform.cross,
                                                     GeneMutation.mutate,
                                                     None,
                                                     Elite.select,
                                                     Elite.select,
                                                     Traditional.replace,
                                                     Elite.select, Elite.select,
                                                     Optimum.cutoff]

    for k,character in enumerate(characters):
        config.character = character
        if not os.path.exists(f'output_{character_names[k]}'):
            os.makedirs(f'output_{character_names[k]}')

        for j,crossover in enumerate(crossovers):
            config.crossover = crossover
            if not os.path.exists(f'output_{character_names[k]}/output_crossover'):
                os.makedirs(f'output_{character_names[k]}/output_crossover')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_crossover/' + f'crossover_{crossover_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        config.crossover = TwoPoints.cross

        for j,mutation in enumerate(mutations):
            config.mutation = mutation
            if not os.path.exists(f'output_{character_names[k]}/output_mutation'):
                os.makedirs(f'output_{character_names[k]}/output_mutation')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_mutation/' + f'mutation_{mutation_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        config.mutation = MultiGeneMutation.mutate
        for j,mutation_variation in enumerate(mutation_variations):
            config.mutation_variation = mutation_variation
            if not os.path.exists(f'output_{character_names[k]}/output_mutation_variation'):
                os.makedirs(f'output_{character_names[k]}/output_mutation_variation')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_mutation_variation/' + f'mutation_variation_{mutation_variation_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        config.selection_a = 1
        if character_names[k] == "Mage":
            config.mutation_variation = None
        else:
            config.mutation_variation = NonUniformGeneMutation.mutate

        for j,selection in enumerate(selection_methods):
            config.selection1 = selection
            if not os.path.exists(f'output_{character_names[k]}/output_select1'):
                os.makedirs(f'output_{character_names[k]}/output_select1')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_select1/' + f'select1_{selection_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        config.selection_a = 0.5
        config.selection1 = Boltzmann(config.tc_selection,config.t0_selection).select

        for j,selection in enumerate(selection_methods):
            config.selection2 = selection
            if not os.path.exists(f'output_{character_names[k]}/output_select2'):
                os.makedirs(f'output_{character_names[k]}/output_select2')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_select2/' + f'select2_{selection_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        config.selection_b = 1
        if character_names[k] == "Warrior":
            config.selection2 = Ranking.select
        else:
            config.selection2 = Boltzmann(config.tc_selection,config.t0_selection).select

        for j,replacement in enumerate(replacement_methods):
            config.replacement = replacement
            if not os.path.exists(f'output_{character_names[k]}/output_replacement'):
                os.makedirs(f'output_{character_names[k]}/output_replacement')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_replacement/' + f'replacement_{replacement_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        config.replacement = Traditional.replace

        for j,selection in enumerate(selection_methods):
            config.selection3 = selection
            if not os.path.exists(f'output_{character_names[k]}/output_select3'):
                os.makedirs(f'output_{character_names[k]}/output_select3')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_select3/' + f'select3_{selection_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        config.selection_b = 0.5
        config.selection3 = Ranking.select

        for j,selection in enumerate(selection_methods):
            config.selection4 = selection
            if not os.path.exists(f'output_{character_names[k]}/output_select4'):
                os.makedirs(f'output_{character_names[k]}/output_select4')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_select4/' + f'select4_{selection_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        if character_names[k] == "Warrior":
            config.selection4 = Ranking.select
        else:
            config.selection4 = Elite.select

        for j,cutoff in enumerate(cutoffs):
            config.cutoff = cutoff
            if cutoff_threshold_values[j] is not None:
                config.cutoff_threshold = cutoff_threshold_values[j]
            else:
                config.cutoff_threshold = cutoff_threshold_levels[k]
            config.repeated_generations = repeated_generations
            if not os.path.exists(f'output_{character_names[k]}/output_cutoff'):
                os.makedirs(f'output_{character_names[k]}/output_cutoff')
            aux = genetic_algorithm(config)
            with open(f'output_{character_names[k]}/output_cutoff/' + f'cutoff_{cutoff_names[j]}' + '.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Generation','Fitness','Height','Strength','Dexterity','Intelligence', 'Vigor','Constitution'])
                for i,generation in enumerate(aux):
                    for individual in generation:
                        writer.writerow([i,individual.getPerformance(),individual.gene.height,individual.gene.strength,individual.gene.dexterity,
                                         individual.gene.intelligence,individual.gene.vigor,individual.gene.constitution])

        if character_names[k] == "Warden":
            config.cutoff = Content.cutoff
        else:
            config.cutoff = Optimum.cutoff







