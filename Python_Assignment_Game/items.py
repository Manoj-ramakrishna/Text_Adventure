# Base class 
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   
        self.description = description  
        self.value = value  

    # __str__ method 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item


class NanoSuit(Item):
    # __init__ is the contructor method
    def __init__(self, Zoom):
        self.Zoom = Zoom  # attribute of the NanoSuit class
        super().__init__(name="NanoSuit",
                         description="New Nano tech suit {} equiped with advance technilogy.".format(
                             self.Zoom),
                         value=self.Zoom)


class Transport:
    def __init__(self):
        self.name = 'Webswing'
        self.description = 'Navigating to other dimensions'

    def Spiderlegs(self, speed):
        if(speed <= 500 and speed >= 20):
            self.name = "Hexa legs projectile"
            self.description = "You are moving with 6 legs"
            print("=== {} at speed {} km/h".format(
                 self.description, speed))

        elif(speed > 500):
            self.name = "Octa legs projectile"
            self.description = "You are moving with 8 legs"
            print("=== {} at speed {} km/h".format(
                self.description, speed))
        else:
            self.name = "Zehn legs projectile"
            self.description = "Speed of 10 legs assisted with nano suit"
            print("=== {} at speed {} km/h".format(
                self.description, speed))

    def __str__(self):
        return "{}\n=====\n{}\n speed: ".format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class WebAttack(Weapon):
    def __init__(self):
        super().__init__(name=" WebAttack",
                         description="This spuns the enemy with the web",
                         value=0,
                         damage=25)


class WebThrow(Weapon):
    def __init__(self):
        super().__init__(name="WebThrow",
                         description="Make enemy blind with this attack",
                         value=10,
                         damage=20)


class NanoWeb(Weapon):
    def __init__(self):
        super().__init__(name="NanoWeb",
                         description="Pin enemy to the ground with the attack",
                         value=0,
                         damage=30)


class Yank(Weapon):
    def __init__(self):
        super().__init__(name="Zen",
                         description="Uses the web to throw the objects in the surroundings",
                         value=1,
                         damage=25)


class Finisher(Weapon):
    def __init__(self):
        super().__init__(name="Finisher",
                         description="Multiple web spuns on enemy",
                         value=2,
                         damage=30)

class NanoDart(Weapon):
    def __init__(self):
        super().__init__(name="NanoDart",
                         description="Shoots a dart towards enemy leaving them paralysed",
                         value=2,
                         damage=100)


class Antidote(Item):
    def __init__(self, name, description, value, amt, health):
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)


class AntidoteLeaves(Antidote):
    def __init__(self):
        super().__init__(name='AntidoteLeaves',
                         description='A small potion', value=5, amt=5, health=30)
