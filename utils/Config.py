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
from src.mutation.UniformGeneMutation import UniformGeneMutation

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
            self.population_size = config["population_size"]
            self.cutoff_threshold = config["cutoff_threshold"]
            self.selection_k = config["selection_k"]
            self.m_deterministic_tournament = config["m_deterministic_tournament"]
            self.character = config["character"]
            self.mutation_probability = config["mutation_probability"]
            self.selection_a = config["selection_a"]
            self.selection_b = config["selection_b"]
            self.tc_boltzmann = config["tc_boltzmann"]
            self.t0_boltzmann = config["t0_boltzmann"]
            self.max_points = config["max_points"]
            self.repeated_generations = config["repeated_generations"]

            character_str = config["character"]
            if character_str == "archer":
                self.character = Archer
            elif character_str == "warrior":
                self.character = Warrior
            elif character_str == "mage":
                self.character = Mage
            elif character_str == "warden":
                self.character = Warden

            crossover_str = config["crossover"]
            if crossover_str == "annular":
                self.crossover = Annular.cross
            elif crossover_str == "one_point":
                self.crossover = OnePoint.cross
            elif crossover_str == "two_points":
                self.crossover = TwoPoints.cross
            elif crossover_str == "uniform":
                self.crossover = Uniform.cross

            mutation_str = config["mutation"]
            if mutation_str == "single_gene":
                self.mutation = GeneMutation.mutate
            elif mutation_str == "multi_gene":
                self.mutation = MultiGeneMutation.mutate

            uniform_mutation_str = config["uniform_mutation"]
            if uniform_mutation_str == "non_uniform_gene":
                self.uniform_mutation = NonUniformGeneMutation.mutate
            elif uniform_mutation_str == "uniform_gene":
                self.uniform_mutation = UniformGeneMutation.mutate

            selection_method1_str = config["selection_method1"]
            if selection_method1_str == "elite":
                self.selection1 = Elite.select
            elif selection_method1_str == "ranking":
                self.selection1 = Ranking.select
            elif selection_method1_str == "deterministic_tournament":
                self.selection1 = DeterministicTournament(self.m_deterministic_tournament).select
            elif selection_method1_str == "probabilistic_tournament":
                self.selection1 = ProbabilisticTournament.select
            elif selection_method1_str == "boltzmann":
                self.selection1 = Boltzmann(self.tc_boltzmann, self.t0_boltzmann).select
            elif selection_method1_str == "roulette":
                self.selection1 = Roulette.select
            elif selection_method1_str == "universal":
                self.selection1 = Universal.select

            selection_method2_str = config["selection_method2"]
            if selection_method2_str == "elite":
                self.selection2 = Elite.select
            elif selection_method2_str == "ranking":
                self.selection2 = Ranking.select
            elif selection_method2_str == "deterministic_tournament":
                self.selection2 = DeterministicTournament(self.m_deterministic_tournament).select
            elif selection_method2_str == "probabilistic_tournament":
                self.selection2 = ProbabilisticTournament.select
            elif selection_method2_str == "boltzmann":
                self.selection2 = Boltzmann(self.tc_boltzmann, self.t0_boltzmann).select
            elif selection_method2_str == "roulette":
                self.selection2 = Roulette.select
            elif selection_method2_str == "universal":
                self.selection2 = Universal.select

            selection_method3_str = config["selection_method3"]
            if selection_method3_str == "elite":
                self.selection3 = Elite.select
            elif selection_method3_str == "ranking":
                self.selection3 = Ranking.select
            elif selection_method3_str == "deterministic_tournament":
                self.selection3 = DeterministicTournament(self.m_deterministic_tournament).select
            elif selection_method3_str == "probabilistic_tournament":
                self.selection3 = ProbabilisticTournament.select
            elif selection_method3_str == "boltzmann":
                self.selection3 = Boltzmann(self.tc_boltzmann, self.t0_boltzmann).select
            elif selection_method3_str == "roulette":
                self.selection3 = Roulette.select
            elif selection_method3_str == "universal":
                self.selection3 = Universal.select

            selection_method4_str = config["selection_method4"]
            if selection_method4_str == "elite":
                self.selection4 = Elite.select
            elif selection_method4_str == "ranking":
                self.selection4 = Ranking.select
            elif selection_method4_str == "deterministic_tournament":
                self.selection4 = DeterministicTournament(self.m_deterministic_tournament).select
            elif selection_method4_str == "probabilistic_tournament":
                self.selection4 = ProbabilisticTournament.select
            elif selection_method4_str == "boltzmann":
                self.selection4 = Boltzmann(self.tc_boltzmann, self.t0_boltzmann).select
            elif selection_method4_str == "roulette":
                self.selection4 = Roulette.select
            elif selection_method4_str == "universal":
                self.selection4 = Universal.select

            replacement_str = config["replacement"]
            if replacement_str == "traditional":
                self.replacement = Traditional.replace
            elif replacement_str == "bias":
                self.replacement = Bias.replace

            cutoff_str = config["cutoff"]
            if cutoff_str == "max_gen":
                self.cutoff = MaxGen.cutoff
            elif cutoff_str == "optimum":
                self.cutoff = Optimum.cutoff
            elif cutoff_str == "content":
                self.cutoff = Content.cutoff
            elif cutoff_str == "structure":
                self.cutoff = Structure.cutoff
