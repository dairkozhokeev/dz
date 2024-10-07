class SuperHero:
    name = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def sayname(self):
        print(self.name)

    def increasehealth(self):
        self.health_points = (self.health_points * 2)
        return self.health_points


    def show_parameters(self):
        print(f"user's nickname:{self.nickname}, user's superpower:{self.superpower}, user's health:{self.health_points} ")

    def __len__(self):
        print(f"len of user's catchphrase:{len(self.catchphrase)}")


hero = SuperHero('Rick','rick04', 'superfast', 50, 'i always come back' )
print(hero.sayname())
print(hero.increasehealth())
print(hero.show_parameters()) #не смог это пофиксить
print(hero.__len__())


