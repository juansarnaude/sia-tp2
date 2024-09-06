from src.classes.Individual import Individual
class Mage(Individual):

    def __init__(self, gene):
        super().__init__(gene)

        #TODO revisar que la suma de probabilidades no da 1 para el mago
    def getPerformance(self):
        return 0.8 * self.gene.getAttackStat() + 0.3 * self.gene.getDefenseStat()