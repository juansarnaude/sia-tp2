import src.classes.Individual as Individual

class Archer(Individual):

    def getPerformance(self):
        return 0.9 * self.gene.getAttackStat() + 0.1 * self.gene.getDefenseStat()