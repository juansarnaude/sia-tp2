import BaseStats

class Archer(BaseStats):

    def getPerformance(self):
        return 0.9 * self.gene.getAttackStat() + 0.1 * self.gene.getDefenseStat()