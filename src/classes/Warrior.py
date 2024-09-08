from src.classes.Individual import Individual

class Warrior(Individual):
    def __init__(self, gene):
        super().__init__(gene)

    def getPerformance(self):
        return 0.6 * self.gene.getAttackStat() + 0.4 * self.gene.getDefenseStat()

    def __hash__(self):
        return hash(self.gene)

    def __eq__(self, other):
        return isinstance(other, Warrior) and self.gene == other.gene