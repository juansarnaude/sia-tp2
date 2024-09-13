from src.classes.Individual import Individual

class Archer(Individual):
    def __init__(self, gene): #, id: int = None):
        super().__init__(gene)
        # self.id = id

    def getPerformance(self):
        return 0.9 * self.gene.getAttackStat() + 0.1 * self.gene.getDefenseStat()

    def __hash__(self):
        return hash(self.gene)

    def __eq__(self, other):
        return isinstance(other, Archer) and self.gene == other.gene
