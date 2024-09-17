from utils.Config import Config
from genetic_algorithm import genetic_algorithm

from src.select.Boltzmann import Boltzmann
from src.select.DeterministicTournament import DeterministicTournament
from src.select.ProbabilisticTournament import ProbabilisticTournament
from src.select.Elite import Elite
from src.select.Ranking import Ranking
from src.select.Roulette import Roulette
from src.select.Universal import Universal

import sys

if __name__ == "__main__":

    config: Config = Config(sys.argv[1])

    selection_methods = [Boltzmann(config.tc_selection, config.t0_selection).select, DeterministicTournament(config.m_deterministic_tournament_selection).select, ProbabilisticTournament.select, Elite.select, Ranking.select, Roulette.select, Universal.select]
    best_fitnesses = []

    for selection in selection_methods:
        config.selection1 = selection
        best_fitnesses.append(genetic_algorithm(config))

    print(best_fitnesses)
    

