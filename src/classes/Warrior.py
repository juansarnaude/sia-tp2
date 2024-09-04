import BaseStats

class Warrior(BaseStats):

    def getPerformance(self):
        return 0.6 * self.gene.getAttackStat() + 0.4 * self.gene.getDefenseStat()