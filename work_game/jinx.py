from work_game.people import People


class Jinx(People):
    name = "jinx"
    def get_data(self):
    #获得jinx英雄的血条和攻击力的方法
        hp = input("请输入jinx的HP：")
        #对非法输入特殊处理
        while not hp.isnumeric():
            hp = input(f"请输入数字格式的内容哦～，jinx的HP：")
        power = input("请输入jinx的攻击力:")
        while not hp.isnumeric():
            power = (f"请输入数字格式的内容哦～，jinx的攻击力：")
        #将字符串转化为浮点型
        self.hp = float(hp)
        self.power = float(power)
