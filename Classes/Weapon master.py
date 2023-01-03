import Functionalities.Utilities

class Weapon_master:
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
                       "2- Ship cannon. (800 coins)\n"
                       "3- Bombarda. (1600 coins)\n")
        option = Functionalities.Utilities.correct_values(1, 3, option)
        if option == 1:
            self.sell_dagger(money)
        elif option == 2:
            self.sell_ship_cannnon(money)
        elif option == 3:
            self.sell_bombarda(money, 1600)

    def sell_bombarda(self, money, price):
        max_purchable_objets = Functionalities.Utilities.how_many_can_afford(price, money)
        cannon_number = input("How many cannons you want to buy?")
        cannon_number = Functionalities.Utilities.correct_values(0, max_purchable_objets, cannon_number)
        if Functionalities.Utilities.check_if_affordable(price, cannon_number, money):
            total_money = cannon_number * price
            self.coins += total_money
            self.experience += total_money
            return cannon_number, total_money

    def sell_ship_cannnon(self, money):
        max_purchable_objets = Functionalities.Utilities.how_many_can_afford(800, money)
        cannon_number = input("How many cannons you want to buy?")
        cannon_number = Functionalities.Utilities.correct_values(0, max_purchable_objets, cannon_number)
        if Functionalities.Utilities.check_if_affordable(800, cannon_number, money):
            total_money = cannon_number * 800
            self.coins += total_money
            self.experience += total_money
            return cannon_number, total_money

    def sell_dagger(self, money):
        max_purchable_objets = Functionalities.Utilities.how_many_can_afford(100, money)
        dagger_number = input("How many daggers you want to buy?")
        dagger_number = Functionalities.Utilities.correct_values(0, max_purchable_objets, dagger_number)
        if Functionalities.Utilities.check_if_affordable(100, dagger_number, money):
            total_money = dagger_number * 100
            self.coins += total_money
            self.experience += total_money
            return dagger_number, total_money

    def create_weapons(self):
        while self.coins > 51:
            if self.dagger < 50:
                self.dagger += 1
                self.coins -= 50
            if self.cannon < 20:
                self.cannon += 1
                self.coins -= 400
            if self.level > 2 and self.bombarda < 20:
                self.bombarda += 1
                self.coins += 650

    def change_turn(self):
        self.create_weapons()
        self.level_up()

    def level_up(self):
        if self.level == 1:
            if self.experience >= 1000:
                self.level += 1
                self.experience = 0
        elif self.level == 2:
            if self.experience >= 3500:
                self.experience = 0
                self.level += 1