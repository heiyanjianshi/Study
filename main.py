from work_game.game_factory import HeroFactory

hero_factory = HeroFactory()
jinx = hero_factory.creat_hero("jinx")
timo = hero_factory.creat_hero("timo")

jinx.get_data()
timo.get_data()
jinx.fight(timo.name, timo.hp, timo.power)