from src.classes.Individual import Individual

class Archer(Individual):
    def __init__(self, gene):
        super().__init__(gene)

    def getPerformance(self):
        return 0.9 * self.gene.getAttackStat() + 0.1 * self.gene.getDefenseStat()
