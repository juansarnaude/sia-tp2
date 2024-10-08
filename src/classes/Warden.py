from src.classes.Individual import Individual

class Warden(Individual):
    def __init__(self, gene):
        super().__init__(gene)

    def getPerformance(self):
        return 0.1 * self.gene.getAttackStat() + 0.9 * self.gene.getDefenseStat()

    def __hash__(self):
        return hash(self.gene)

    def __eq__(self, other):
        return isinstance(other, Warden) and self.gene == other.gene