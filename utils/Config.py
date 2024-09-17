import json

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

class Config:

    def __init__(self, config_path):
        with open(config_path, "r") as file:
            config = json.load(file)
            
            # General configurations
            self.population_size = config["population_size"]
            self.max_points = config["max_points"]

            # Character configurations
            self.character = config["character"]

            character_str = config["character"]
            if character_str == "archer":
                self.character = Archer
            elif character_str == "warrior":
                self.character = Warrior
            elif character_str == "mage":
                self.character = Mage
            elif character_str == "warden":
                self.character = Warden

            # Set maximum time
            self.max_time = config["max_time"]

            # Crossover method configuration
            crossover_str = config["crossover"]
            if crossover_str == "annular":
                self.crossover = Annular.cross
            elif crossover_str == "one_point":
                self.crossover = OnePoint.cross
            elif crossover_str == "two_points":
                self.crossover = TwoPoints.cross
            elif crossover_str == "uniform":
                self.crossover = Uniform.cross

            # Mutation configurations
            mutation = config["mutation"]
            mutation_type = mutation["type"]
            if mutation_type == "single_gene":
                self.mutation = GeneMutation.mutate
            elif mutation_type == "multi_gene":
                self.mutation = MultiGeneMutation.mutate

            probability_variation_str = mutation["probability_variation"]
            if probability_variation_str == "non_uniform":
                self.mutation_variation = NonUniformGeneMutation.mutate
            else:
                self.mutation_variation = None
            
            self.mutation_probability = mutation["probability"]

            non_uniform_bound = mutation["non_uniform_mutation"]
            self.non_uniform_lower_bound = non_uniform_bound["lower_bound"]
            self.non_uniform_upper_bound = non_uniform_bound["upper_bound"]

            # Selection configurations
            selection = config["selection"]

            methods_configuration_selection = selection["methods_configuration"]
            m_deterministic_tournament_selection = methods_configuration_selection["deterministic_tournament"]["m"]

            tc_selection = methods_configuration_selection["boltzmann"]["tc"]
            t0_selection = methods_configuration_selection["boltzmann"]["t0"]

            selection_method1_str = selection["method1"]
            if selection_method1_str == "elite":
                self.selection1 = Elite.select
            elif selection_method1_str == "ranking":
                self.selection1 = Ranking.select
            elif selection_method1_str == "deterministic_tournament":
                self.selection1 = DeterministicTournament(m_deterministic_tournament_selection).select
            elif selection_method1_str == "probabilistic_tournament":
                self.selection1 = ProbabilisticTournament.select
            elif selection_method1_str == "boltzmann":
                self.selection1 = Boltzmann(tc_selection, t0_selection).select
            elif selection_method1_str == "roulette":
                self.selection1 = Roulette.select
            elif selection_method1_str == "universal":
                self.selection1 = Universal.select

            selection_method2_str = selection["method2"]
            if selection_method2_str == "elite":
                self.selection2 = Elite.select
            elif selection_method2_str == "ranking":
                self.selection2 = Ranking.select
            elif selection_method2_str == "deterministic_tournament":
                self.selection2 = DeterministicTournament(m_deterministic_tournament_selection).select
            elif selection_method2_str == "probabilistic_tournament":
                self.selection2 = ProbabilisticTournament.select
            elif selection_method2_str == "boltzmann":
                self.selection2 = Boltzmann(tc_selection, t0_selection).select
            elif selection_method2_str == "roulette":
                self.selection2 = Roulette.select
            elif selection_method2_str == "universal":
                self.selection2 = Universal.select

            self.selection_a = selection["a"]

            # Replacement configurations

            replacement = config["replacement"]

            replacement_str = replacement["type"]
            if replacement_str == "traditional":
                self.replacement = Traditional.replace
            elif replacement_str == "bias":
                self.replacement = Bias.replace

            methods_configuration_replacement = replacement["methods_configuration"]
            m_deterministic_tournament_replacement = methods_configuration_replacement["deterministic_tournament"]["m"]

            tc_replacement = methods_configuration_replacement["boltzmann"]["tc"]
            t0_replacement = methods_configuration_replacement["boltzmann"]["t0"]

            selection_method3_str = replacement["method3"]
            if selection_method3_str == "elite":
                self.selection3 = Elite.select
            elif selection_method3_str == "ranking":
                self.selection3 = Ranking.select
            elif selection_method3_str == "deterministic_tournament":
                self.selection3 = DeterministicTournament(m_deterministic_tournament_replacement).select
            elif selection_method3_str == "probabilistic_tournament":
                self.selection3 = ProbabilisticTournament.select
            elif selection_method3_str == "boltzmann":
                self.selection3 = Boltzmann(tc_replacement, t0_replacement).select
            elif selection_method3_str == "roulette":
                self.selection3 = Roulette.select
            elif selection_method3_str == "universal":
                self.selection3 = Universal.select

            selection_method4_str = replacement["method4"]
            if selection_method4_str == "elite":
                self.selection4 = Elite.select
            elif selection_method4_str == "ranking":
                self.selection4 = Ranking.select
            elif selection_method4_str == "deterministic_tournament":
                self.selection4 = DeterministicTournament(m_deterministic_tournament_replacement).select
            elif selection_method4_str == "probabilistic_tournament":
                self.selection4 = ProbabilisticTournament.select
            elif selection_method4_str == "boltzmann":
                self.selection4 = Boltzmann(tc_replacement, t0_replacement).select
            elif selection_method4_str == "roulette":
                self.selection4 = Roulette.select
            elif selection_method4_str == "universal":
                self.selection4 = Universal.select

            self.selection_b = replacement["b"]
            self.selection_k = replacement["k"]

            # Cutoff configurations

            cutoff = config["cutoff"]

            cutoff_str = cutoff["method"]
            if cutoff_str == "max_gen":
                self.cutoff = MaxGen.cutoff
            elif cutoff_str == "optimum":
                self.cutoff = Optimum.cutoff
            elif cutoff_str == "content":
                self.cutoff = Content.cutoff
            elif cutoff_str == "structure":
                self.cutoff = Structure.cutoff

            self.cutoff_threshold = cutoff["threshold"]
            self.repeated_generations = cutoff["repeated_generations"]
