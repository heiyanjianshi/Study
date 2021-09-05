from work_game.jinx import Jinx
from work_game.timo import Timo

class HeroFactory:
    def creat_hero(self, hero):
        """
        创建对应英雄实例的方法；
        :param hero: 传想要创建的类，jixn表示返回Jinx类的的实例，timo表示返回Timo类的实例
        :return: 返回匹配到的英雄实例对象
        """
        if hero == "jinx":
            return Jinx()
        elif hero == "timo":
            return Timo()
        else:
            raise Exception("此英雄不在英雄工厂当中哦～")


