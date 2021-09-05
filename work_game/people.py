class People:
    name = ""
    hp = 0
    power = 0

    # def __init__(self, hp, power):
    #     self.hp = hp
    #     self.power = power

    def fight(self, enemy_name, enemy_hp = 0, enemy_power = 0):
        """
        用来计算并得出最终获胜者
        :param enemy_name:敌人的姓名
        :param enemy_hp:敌人的血量，整型
        :param enemy_power: 敌人的攻击力，整型
        :return:
        """
        #计算英雄的血量
        hero_hp = self.hp - enemy_power
        #计算敌人的血量
        enemy_hp -= self.power
        #判断英雄和敌人谁的血量多
        if hero_hp > enemy_hp:
            print(f"{self.name}赢了！")
        elif hero_hp < enemy_hp:
            print(f"{enemy_name}赢了！")
        else:
            print(f"双方是平局哦～")

