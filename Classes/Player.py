import Functionalities

class Player:
    def __init__(self, name, coins, city):
        self.name = name
        self.coins = coins
        self.level = 1
        self.city = city
        self.experience = 0
        # Tooked?? loans.
        self.loans = []
        self.boats = []
        self.convoys = []

    def check_player(self):
        print("You have {} coins, {} boats and {} convoys. Your level is {}"
              .format(self.coins, len(self.boats), len(self.convoys), self.level))


    def gain_experience(self, exp):
        self.experience += exp


    def level_up(self):
        if self.level == 1:
            if self.coins > 50_000 and self.experience > 99:
                self.level += 1
                self.experience = 0
        elif self.level == 2:
            if self.coins > 100_000 and self.experience > 199:
                self.level += 1
                self.experience = 0
        elif self.level == 3:
            if self.coins > 200_000 and self.experience > 299:
                self.level += 1


    def check_boats(self):
        boat_number = 1
        for boat in self.boats:
            print("{}- {}. ({})\n".format(boat_number, boat.name, boat.city.name))
            boat_number += 1

    def check_convoys(self):
        convoy_number = 1
        for convoy in self.convoys:
            print("{}- {}. ({})\n".format(convoy_number, convoy.name, convoy.city.name))
            convoy_number += 1