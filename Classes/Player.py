import Functionalities.Utilities
import Functionalities


class Player:
    def __init__(self, name, coins):
        self.name = name
        self.coins = coins
        self.level = 1
        self.city = 0
        self.experience = 0
        # Tooked?? loans.
        self.loans = []
        self.boats = []
        self.convoys = []
        self.turn = 1
    def check_player(self):
        print("-" * 60)
        print("You have {} coins, {} boats and {} convoys. Your level is {}."
              .format(self.coins, len(self.boats), len(self.convoys), self.level))
        print("-" * 60, "\n")
    def gain_experience(self, exp):
        self.experience += exp

    def level_up(self):
        """
        Gain experience and level up.
        :return:
        """
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
        """
        Select boats, unless they are traveling.
        :return:
        """
        if len(self.boats) == 0:
            print("You dont have any boats to select.\n")
        else:
            boat_number = 1
            boats_not_traveling = []
            for boat in self.boats:
                if not boat.check_if_traveling():
                    boats_not_traveling.append(boat)
            for boat in boats_not_traveling:
                print("{}- {}. ({})\n".format(boat_number, boat.name, boat.city.name))
                boat_number += 1
            if len(boats_not_traveling) == 0:
                print("All your boats are traveling.\n")
                self.where_are_traveling(self.boats)
            else:
                choose_boat = self.select_boat_or_convoy(boats_not_traveling)
                choose_boat.show_options()

    def where_are_traveling(self, moving_list):
        Functionalities.Utilities.text_separation()
        for moving_item in moving_list:
            print("{} moving from {} to {}. ({} turns remain)."
                  .format(moving_item.name, moving_item.city.name,
                          moving_item.destination.name, moving_item.travel_turns))
        Functionalities.Utilities.text_separation()
    def check_convoys(self):
        if len(self.convoys) == 0:
            print("You dont have any convoys to select.\n")
        else:
            convoy_number = 1
            for convoy in self.convoys:
                print("{}- {}. ({})\n".format(convoy_number, convoy. name, convoy.city.name))
                convoy_number += 1
            current = self.select_boat_or_convoy(self.convoys)
            self.boat_or_convoy_options(current)

    def select_boat_or_convoy(self, type):
        option = input()
        option = Functionalities.Utilities.correct_values(1, len(type), option)
        return type[option - 1]

    def boat_or_convoy_options(self, choosen):
        prueba = choosen.show_options


    def list_cities(self, cities):
        print("Where do you want to move?\n"
              "1- Lubeck.\n"
              "2- Rostock. \n"
              "3- Malmo. \n"
              "4- Stettin.\n"
              "5- Gdanks.\n")
        option = input("\n")
        option = Functionalities.Utilities.correct_values(1, 5, option)
        return cities[option - 1]

    def is_possible_to_change_cities(self, cities):
        selected_city = self.list_cities(cities)
        for boat in self.boats:
            if boat.city == selected_city:
                return True, selected_city
        for convoy in self.convoys:
            if convoy.city == selected_city:
                return True, selected_city
        return False


    def change_city(self, cities):
        selected_city = self.is_possible_to_change_cities(cities)
        if selected_city == False:
            print("You can't move to a city if you don't have a boat in it.")
        else:
            self.city = selected_city[1]
            print("You have moved to another city.")