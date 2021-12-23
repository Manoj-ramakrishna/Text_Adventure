class Enemy:
    def __init__(self, name, hp, damage, experience):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.experience = experience

    def is_alive(self):
        return self.hp > 0


class Lizard(Enemy):
    def __init__(self):
        super().__init__(name="Lizard", hp=30, damage=40, experience=40)


class Mysterio(Enemy):
    def __init__(self):
        super().__init__(name="Mysterio", hp=20, damage=10, experience=10)


class Octopus(Enemy):
    def __init__(self):
        super().__init__(name="Octopus", hp=25, damage=15, experience=10)


class Venom(Enemy):
    def __init__(self):
        super().__init__(name="Venom", hp=25, damage=20, experience=10)


class Sandman(Enemy):
    def __init__(self):
        super().__init__(name="Sandman", hp=20, damage=10, experience=30)

class Chameleon(Enemy):
    def __init__(self):
        super().__init__(name="Chameleon", hp=35, damage=10, experience=30)

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=30, damage=20, experience=20)

