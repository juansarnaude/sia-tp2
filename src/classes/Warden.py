import src.classes.Individual as Individual

class Warden(Individual):

    def getPerformance(self):
        return 0.1 * self.gene.getAttackStat() + 0.9 * self.gene.getDefenseStat()