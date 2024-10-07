from dz_1 import SuperHero

class AirHero(SuperHero):
    people = 'человек'
    # name = 'air hero'
    # nickname = 'shamalhero228'
    # superpower = 'super breath'
    # health_points = 80
    # catchphrase = "if i start talk, you'll be death"
    # damage = 20
    # fly = False


    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def increasehealth(self):
        self.health_points = (self.health_points ** 2)
        return self.health_points

        self.fly = True
        return self.fly


    def true_phrase(self):
        print('True in the True_phrase')

class FireHero(SuperHero):
    people = 'человек'
    # name = 'fire hero'
    # nickname = 'ot_hero229'
    # superpower = 'fire control'
    # health_points = 70
    # catchphrase = "fire and only fire"
    # damage = 35
    # fly = False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def increasehealth(self):
        self.health_points = (self.health_points ** 2)
        return self.health_points

        self.fly = True
        return self.fly


    def true_phrase(self):
        print('True in the True_phrase')


hero_2 = AirHero('air hero',
                 'shamalhero228',
                 'super breath',
                 80,
                 "if i start talk, you'll be death",
                 20,
                 False )
hero_2.increasehealth()
hero_2.true_phrase()
print(hero_2.show_parameters())

hero_3 = FireHero('fire hero','ot_hero229',
    'fire control',
    70,
    "fire and only fire",
    35,
    False)
print(hero_3.increasehealth())
print(hero_3.true_phrase())
print(hero_3.show_parameters())


class Villain(FireHero):
    people = 'monster'

    def gen_x(self):
        ...

    def crit(self):
        self.damage = (self.damage ** 2 )

print(Villain.crit(hero_3))





# Villain.crit(AirHero)








