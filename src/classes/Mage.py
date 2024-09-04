import BaseStats

class Mage(BaseStats):

    #TODO revisar que la suma de probabilidades no da 1 para el mago
    def getPerformance(self):
        return 0.8 * self.gene.getAttackStat() + 0.3 * self.gene.getDefenseStat()