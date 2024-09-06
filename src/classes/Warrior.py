import src.classes.Individual as Individual

class Warrior(Individual):

    def getPerformance(self):
        return 0.6 * self.gene.getAttackStat() + 0.4 * self.gene.getDefenseStat()