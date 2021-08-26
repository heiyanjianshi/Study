class People:
    hp = 0
    power = 0

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp = 0, enemy_power = 0):
        self.hp -= enemy_power
        enemy_hp -= self.power

