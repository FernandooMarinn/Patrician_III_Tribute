import Functionalities

class Vendedor_armas:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.coins = 100

        self.dagger = 3
        self.cannon = 2
        self.bombarda = 0

    def sell_products(self, money):
        option = input("What do you want to buy?\n"
                       "1- Dagger. (100 coins)\n"
                       "2- Ship cannon. (800 coins)\n")
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if option == 1:
            max_purchable_objets = Functionalities.Utilities.how_many_can_afford(100, money)
            dagger_number = input("How many daggers you want to buy?")
            dagger_number = Functionalities.Utilities.correct_values(0, max_purchable_objets, dagger_number)
            if Functionalities.Utilities.check_if_affordable(100, dagger_number, money):
                self.coins += dagger_number * 100
                return dagger_number, dagger_number * 100
        elif option == 2:
            max_purchable_objets = Functionalities.Utilities.how_many_can_afford(800, money)
            cannon_number = input("How many cannons you want to buy?")
            cannon_number = Functionalities.Utilities.correct_values(0, max_purchable_objets, cannon_number)
            if Functionalities.Utilities.check_if_affordable(800, cannon_number, money):
                self.coins += cannon_number * 800
                return cannon_number, cannon_number * 800

    def create_weapons(self):
        while self.coins > 51:
            if self.dagger < 50:
                self.dagger += 1
                self.coins -= 50
            if self.cannon < 20:
                self.cannon += 1
                self.coins -= 400
            if self.level > 2:
                pass
    def change_turn(self):
        self.create_weapons()