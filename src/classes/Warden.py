from src.classes.Individual import Individual
class Warden(Individual):
    def __init__(self, gene):
        super().__init__(gene)

    def getPerformance(self):
        return 0.1 * self.gene.getAttackStat() + 0.9 * self.gene.getDefenseStat()