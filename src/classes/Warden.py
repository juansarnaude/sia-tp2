import BaseStats

class Warden(BaseStats):

    def getPerformance(self):
        return 0.1 * self.gene.getAttackStat() + 0.9 * self.gene.getDefenseStat()