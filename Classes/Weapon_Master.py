import Functionalities.Utilities


class Weapon_master:
    def __init__(self, city):
        self.level = 1
        self.experience = 0
        self.coins = 100

        self.city = city
        self.commercial_office = self.city.commercial_office

        self.dagger = 4
        self.cannon = 2
        self.bombard = 0

    def show_menu(self):
        option = input("What do you want to do?\n"
                       "1- Buy weapons.\n"
                       "2- Exit.\n")
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if not self.city.commercial_office:
            Functionalities.Utilities.text_separation()
            print("You don´t have a commercial office in this city!")
            Functionalities.Utilities.text_separation()
        elif option == 1:
            self.buy_weapons()




    def buy_weapons(self):
        option = input("\nWhat do you want to buy?\n"
                       "1- Dagger. (100 coins)\n"
                       "2- Ship cannon. (800 coins)\n"
                       "3- Bombard. (1600 coins)\n"
                       "4- Exit.\n")
        option = Functionalities.Utilities.correct_values(1, 4, option)
        if option == 1:
            self.selling_weapons("dagger")
        elif option == 2:
            self.selling_weapons("cannon")
        elif option == 3:
            self.selling_weapons("bombard")

    def gain_experience(self, experience):
        self.experience += experience

    def level_up(self):
        if self.level == 1:
            if self.experience >= 1000:
                self.level += 1
                self.experience = 0
        elif self.level == 2:
            if self.experience >= 5000:
                self.experience = 0
                self.level += 1

    def selling_weapons(self, option):
        names = {
            "dagger": self.dagger,
            "cannon": self.cannon,
            "bombard": self.bombard
        }
        prices = {
            "dagger": 100,
            "cannon": 800,
            "bombard": 1600
        }

        how_many = input("How many do you want to buy? There are {} on sale.\n".format(names[option]))
        how_many = Functionalities.Utilities.correct_values(0, names[option], how_many)
        if how_many == 0:
            pass
        else:
            can_afford = Functionalities.Utilities.how_many_can_afford(prices[option] * how_many, self.city.player.coins)
            if can_afford >= how_many:
                Functionalities.Utilities.money_exchange(self.city.player, self, prices[option] * how_many)
                self.decrease_weapons(option, how_many)
                self.move_to_commercial_office([option, how_many])
                self.gain_experience(prices[option] * how_many)
                print("\nYou have bought {} {}.\n\n".format(option, how_many))
            else:
                print("You can't afford to buy those weapons.\n")


    def decrease_weapons(self, name, quantity):
        if name == "dagger":
            self.dagger -= quantity
        elif name == "cannon":
            self.cannon -= quantity
        elif name == "bombard":
            self.bombard -= quantity

    def create_weapons(self):
        while (self.coins > 51) and (self.dagger < 50 or self.cannon < 20 or self.bombard < 20):
            if self.dagger < 50:
                self.dagger += 1
                self.coins -= 50
            if self.cannon < 20 and self.coins >= 400:
                self.cannon += 1
                self.coins -= 400
            if self.level > 2 and self.bombard < 20 and self.coins >= 650:
                self.bombard += 1
                self.coins += 650

    def change_turn(self):
        self.create_weapons()
        self.level_up()

    def calculate_item_weight(self, items):
        item_name = items[0]
        item_quantity = items[1]
        item_weight = {
            "dagger": 1,
            "cannon": 5,
            "bombard": 5
        }
        return item_weight[item_name] * item_quantity



    def move_to_commercial_office(self, items):
        current_weapons = getattr(self.commercial_office, items[0])
        setattr(self.commercial_office, items[0], current_weapons + items[1])

