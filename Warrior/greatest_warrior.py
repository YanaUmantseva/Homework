RANKS = {
    "Pushover": range(1, 11),
    "Novice": range(11, 21),
    "Fighter": range(21, 31),
    "Warrior": range(31, 41),
    "Veteran": range(41, 51),
    "Sage": range(51, 61),
    "Elite": range(61, 71),
    "Conqueror": range(71, 81),
    "Champion": range(81, 91),
    "Master": range(91, 101),
    "Greatest": range(101, 102)
}

class Warrior:
    def __init__(self):
        self.xp = 100
        self.achievements = []

    @property
    def level(self):
        return self.xp // 100

    @property
    def rank(self):
        for k, v in RANKS.items():
            if self.level in v:
                return k


    def update_level(self):
        if self.xp >= 10000:
            self.xp = 10000
        if self.xp >= 100:
            return min(self.xp // 100, 100)
        return 1

    def battle(self, opponent_level):
        if self.level < 1 or self.level > 100:
            return "Invalid level"
        if opponent_level < 1 or opponent_level > 100:
            return "Invalid level"

        if self.level == opponent_level:
            self.xp += 10
            fight_result = "A good fight"
        elif opponent_level < self.level:
            diff = self.level - opponent_level
            if diff == 1:
                self.xp += 5
                fight_result = "A good fight"
            elif diff >= 2:
                fight_result = "Easy fight"
                self.xp += 0
        else:
            diff = opponent_level - self.level
            if (self.level // 10) < (opponent_level // 10) and diff >= 5:
                return "You've been defeated"
            self.xp += 20 * diff * diff
            fight_result = "An intense fight"

        self.update_level()
        return fight_result

    def training(self, name, exp, min_level):
        if self.level >= min_level:
            self.xp += exp
            self.achievements.append(name)
            self.update_level()
            return name
        else:
            return "Not strong enough"


w = Warrior()
print(w.xp, w.level, w.rank)

w.xp += 1500
print(w.xp, w.level, w.rank)


