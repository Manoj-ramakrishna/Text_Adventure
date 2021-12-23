import items
import enemies
import actions
import world
import player
#import sounds


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Equip())
        moves.append(actions.Heal())
        moves.append(actions.Status())

        return moves


class Webspunn(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        _______  __   __  _______    _______  _______  ___   ______   _______  ______      __   __  _______  _______  ___   _______ 
|       ||  | |  ||       |  |       ||       ||   | |      | |       ||    _ |    |  |_|  ||   _   ||       ||   | |       |
|_     _||  |_|  ||    ___|  |  _____||    _  ||   | |  _    ||    ___||   | ||    |       ||  |_|  ||    ___||   | |       |
  |   |  |       ||   |___   | |_____ |   |_| ||   | | | |   ||   |___ |   |_||_   |       ||       ||   | __ |   | |       |
  |   |  |       ||    ___|  |_____  ||    ___||   | | |_|   ||    ___||    __  |  |       ||       ||   ||  ||   | |      _|
  |   |  |   _   ||   |___    _____| ||   |    |   | |       ||   |___ |   |  | |  | ||_|| ||   _   ||   |_| ||   | |     |_ 
  |___|  |__| |__||_______|  |_______||___|    |___| |______| |_______||___|  |_|  |_|   |_||__| |__||_______||___| |_______|
        
        Get ready for killing the ones responsible for destroying Earth, You have many Villians here with divine powers,
        You have been blessed with Stark Enterprise Inventory to kill: Lizard, Mysterio, Octopus and many more.
        """

    def modify_player(self, player):
        # Room has no action on player
        return player.lockpass()


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(
                self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
    
            return self.adjacent_moves()


class EmptySpace(MapTile):
    def intro_text(self):
        return """
        You go into oblivion state here.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class Lizarzone(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Lizard())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Lizard came from sewer to attack
            """
        else:
            return """
            You slained it!
            """


class Mysteriozone(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Mysterio())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             Swarm of Drones have appeared to attack you
             """
        else:
            return """
             The drones have been destroyed forever
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class StarkZone(MapTile):
    def intro_text(self):
        return """
        All the enemies have been captured and you are victories 
        """

    def modify_player(self, player):
        player.victory = True


class Venomzone(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Venom())

    def intro_text(self):
        if self.enemy.is_alive():
            
            return """
             Venom appeared infront of you
             """
        else:
            return """
             You have slained the venom
             """


class Goblinzone(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Goblin())

    def intro_text(self):
        if self.enemy.is_alive():
            
            return """
             A gaint Goblin came to attack with a hoverboard
             """
        else:
            return """
             You spung away
             """


##



class Thanoszone(EnemyRoom):
    def __init__(self, x, y, ):
        super().__init__(x, y, enemies.Chameleon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """ You have entered the morphing chameleon zone"""
        else:
            return """Run before the transformation"""


class Odin(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.NanoDart())

    def intro_text(self):
        return """
        You have eneterd the world after thanos destroyed, get ready for stronger enemies
        """


class Multiverse(MapTile):
    def intro_text(self):
        return """
        Save this world before Thanos clears in into the half.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass






class StarkEnt(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.WebAttack())

    def intro_text(self):
        return """Most powerful dose of web
"
        """


class Luxury(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.WebThrow)

    def intro_text(self):
        return """
        Welcome to the space-2, It has the enimies with newly formed planets
        """




class Transition(MapTile):

    def intro_text(self):
        return """
    You have slained the enemies
        
        """

    def modify_player(self, player):
        # Room has no action on player

        return player.level_up()


class NuclearPower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Jabberjay())

    def intro_text(self):
        if self.enemy.is_alive():
            return """ Jabberjay are powerful. You need to use everything to beat him***
            Before the Dark Days war, District 13 specialized in nuclear technology and the development of emerging technologies for use by Panem's military.
            """
        else:
            return """$$$$ you have defeated president snows challenge $$$"""


class Transportation(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Octopus())

    def intro_text(self):
        if self.enemy.is_alive():
            return """Be aware of eight legs animal
            """
        else:
            return """4 legs are gone, destroy it"""
