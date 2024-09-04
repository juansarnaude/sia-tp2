import numpy as np

def Gene(height,strength,dexterity,intelligence,vigor,constitution):

    def __init__(self,height,strength,dexterity,intelligence,vigor,constitution):
        self.height = height
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.vigor = vigor
        self.constitution = constitution

    def getHeight(self):
        return self.height

    def getTotalStrength(self):
        return 100*np.tanh(0.01 * self.strength)

    def getTotalDexterity(self):
        return np.tanh(0.01 * self.dexterity)

    def getTotalIntelligence(self):
        return 0.6*np.tanh(0.01 * self.intelligence)

    def getTotalVigor(self):
        return np.tanh(0.01 * self.vigor)

    def getTotalConstitution(self):
        return 100*np.tanh(0.01 * self.constitution)

    def getTotalPoints(self):
        return self.strength + self.dexterity + self.intelligence + self.vigor + self.constitution

    def getATM(self):
        return 0.5 - np.power(self.height * 3 - 5, 4) + np.power(self.height * 3 - 5, 2) + self.height / 2

    def getDEM(self):
        return 2 + np.power(self.height * 3 - 5, 4) - np.power(self.height * 3 - 5, 2) - self.height / 2

    def getAttackStat(self):
        return (getTotalDexterity() + getTotalIntelligence()) * getTotalStrength() * getATM()


    #TODO preguntar formula defense
    def getDefenseStat(self):
        return (getTotalVigor() + self.intelligence) * self.constitution * getDEM()