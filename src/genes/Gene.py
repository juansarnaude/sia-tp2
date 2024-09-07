import random
from typing import List
import numpy as np

class Gene:
    static_max_points = 200

    def __init__(self,stats:List[float]=None, random_ini:bool=False):
        if random_ini:
            self.height = random.uniform(1.3, 2.0)

            self.strength = random.randint(0,200)
            self.dexterity = random.randint(0,200)
            self.intelligence = random.randint(0,200)
            self.vigor = random.randint(0,200)
            self.constitution = random.randint(0,200)

            self.normalize()

        if stats:
            self.height = stats[0]
            self.strength = stats[1]
            self.dexterity = stats[2]
            self.intelligence = stats[3]
            self.vigor = stats[4]
            self.constitution = stats[5]

    def __str__(self):
        attributes = self.get_all_atributes()
        return ', '.join([f"{name}={value}" for name, value in attributes])

    def get_all_atributes(self):
        attributes = [
            ("height", self.height),
            ("strength", self.strength),
            ("dexterity", self.dexterity),
            ("intelligence", self.intelligence),
            ("vigor", self.vigor),
            ("constitution", self.constitution)
        ]
        return attributes

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
        return (self.getTotalDexterity() + self.getTotalIntelligence()) * self.getTotalStrength() * self.getATM()

    def get_stat_array(self) -> List[float]:
        return [self.height, self.strength, self.dexterity, self.intelligence, self.vigor, self.constitution]

    def getDefenseStat(self):
        return (self.getTotalVigor() + self.getTotalIntelligence()) * self.getTotalConstitution() * self.getDEM()

    def normalize(self):
        total_stats= self.getTotalPoints()

        if self.static_max_points < total_stats:
            normalize_value = self.static_max_points / total_stats
            self.strength = self.strength * normalize_value
            self.dexterity = self.dexterity * normalize_value
            self.intelligence = self.intelligence * normalize_value
            self.vigor = self.vigor * normalize_value
            self.constitution = self.constitution * normalize_value
