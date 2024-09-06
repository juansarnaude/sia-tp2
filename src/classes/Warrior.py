from src.classes.Individual import Individual
class Warrior(Individual):
    def __init__(self, gene):
        super().__init__(gene)

    def getPerformance(self):
        return 0.6 * self.gene.getAttackStat() + 0.4 * self.gene.getDefenseStat()