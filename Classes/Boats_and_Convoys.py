import Functionalities.Utilities

class Boat:
    def __init__(self, health, level, load, sailors, captain, cannons, name, city):

        self.name = name

        self.max_health = 0
        self.health = health
        self.level = level
        self.max_load = 150
        self.max_sailors = 0
        self.sailors = sailors
        self.max_cannons = 0
        self.cannons = cannons
        self.city = city


        # List with inicial cargo.
        self.skins = load[0]
        self.tools = load[1]
        self.beer  = load[2]
        self.wine  = load[3]
        self.cloth = load[4]

        self.captain = captain

    def check_level(self):
        if self.level == 1:
            self.max_sailors = 20
            self.max_cannons = 7
            self.max_health = 100
            self.max_load = 120

        elif self.level == 2:
            self.max_sailors = 30
            self.max_cannons = 9
            self.max_health = 110
            self.max_load = 150

        elif self.level == 3:
            self.max_sailors = 40
            self.max_cannons = 12
            self.max_health = 125
            self.max_load = 180

    def boat_deterioration(self):
        self.health -= 1
        if self.health < 11:
            print("Atention! Your ship {} is sinking.".format(self.name))
        if self.health < 1:
            print("Your ship {} has sinked.".format(self.name))
            return False

    def check_stats_level(self):
        if self.level == 1:
            self.max_sailors = 20
            self.max_load = 150
        elif self.level == 2:
            self.max_sailors = 25
            self.max_load = 175
        elif self.level == 3:
            self.max_sailors = 30
            self.max_load = 200

    def check_if_enough_sailors(self):
        if self.sailors < 8:
            return False
        else:
            return True

    def check_if_can_become_convoy(self):
        if self.captain:
            if self.sailors > 19:
                if self.cannons > 7:
                    election = input("Do you want to create a new convoy, named {}?\n"
                                     "1- Yes.\n"
                                     "2- No.\n".format(self.name))
                    election = Functionalities.Utilities.correct_values(1, 2, election)
                    if election == 1:
                        return True
                    else:
                        return False
                else:
                    print("Your boat has less than 8 cannons.")
            else:
                print("Your boat has less than 20 sailors.")
        else:
            print("In order to create a convoy, you need a captain.")


# Convoys, to control ships together.
class Convoy:
    def __init__(self, name, city):
        self.boats = []
        self.min_level = 0
        self.name = name
        self.city = city

    def check_min_lvl(self):
        all_levels = []
        for boat in self.boats:
            all_levels.append(boat.level)
        self.min_level = min(all_levels)