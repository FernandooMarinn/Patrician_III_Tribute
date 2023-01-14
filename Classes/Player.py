import Functionalities.Utilities
import Functionalities


class Player:
    def __init__(self, name, coins):
        self.name = name
        self.coins = coins
        self.level = 1
        self.city = 0
        self.experience = 0
        self.boats = []
        self.convoys = []
        self.turn = 0
        self.all_cities_list = 0

        self.number_of_offices = 1
        self.can_build_offices = False
    def check_player(self):
        """
        Prints out any important data.
        :return:
        """
        print("-" * 60)
        print("You have {} coins, {} boats and {} convoys. Your level is {}."
              .format(self.coins, len(self.boats), len(self.convoys), self.level))
        print("-" * 60, "\n")


    def level_up(self):
        """
        Level up.
        :return:
        """
        if self.level == 1:
            if self.coins > 50_000:
                self.level += 1
                self.print_level_up(1)
        elif self.level == 2:
            if self.coins > 100_000:
                self.level += 1
                self.print_level_up(2)
        elif self.level == 3:
            if self.coins > 200_000:
                self.level += 1
                self.print_level_up(3)


    def print_level_up(self, option):
        """
        Everytime the player levels up, this print a message.
        :param option:
        :return:
        """
        Functionalities.Utilities.text_separation()
        if option == 1:
            print("You have reached a good amount of wealth. People are now beginning to know you.")
        elif option == 2:
            print("Your wealth have granted you a place in among aristocracy. Your new friends have granted you the\n"
                  "right to create a new commercial office.")
        elif option == 3:
            print("Unavailable. You are now one of the most wealthiest persons in the hanseatic league. \n"
                  "You can now create commercial offices in every city that you want.")
        Functionalities.Utilities.text_separation()

    def check_if_can_build_office(self):
        """
        Check if possible to build offices in another cities.
        :return:
        """
        if self.level == 1:
            self.can_build_offices = False
        elif self.level == 2 and self.number_of_offices < 2:
            self.can_build_offices = True
        else:
            self.can_build_offices = True

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
                print("{}- {}. ({}) {}% health.\n".format(boat_number, boat.name, boat.city.name, boat.health))
                boat_number += 1
            if len(boats_not_traveling) == 0:
                print("All your boats are traveling.\n")
                self.where_are_traveling(self.boats)
            else:
                choose_boat = self.select_boat_or_convoy(boats_not_traveling)
                choose_boat.show_menu()

    def select_traveling_units(self, unit_list):
        """
        Select every traveling boat, and return them.
        :param unit_list:
        :return:
        """
        traveling_list = []
        for unit in unit_list:
            if unit.check_if_traveling():
                traveling_list.append(unit)
        return traveling_list

    def view_all_traveling_units(self):
        """
        Differences between convoys and ships.
        :return:
        """
        traveling_boats = self.select_traveling_units(self.boats)
        traveling_convoys = self.select_traveling_units(self.convoys)
        print("Your moving boats are:\n")
        self.where_are_traveling(traveling_boats)
        print("Your moving convoys are:\n")
        self.where_are_traveling(traveling_convoys)

    def where_are_traveling(self, moving_list):
        """
        Print out every traveling unit.
        :param moving_list:
        :return:
        """
        Functionalities.Utilities.text_separation()
        if len(moving_list) == 0:
            print("You have no units traveling currently.")
        else:
            for moving_item in moving_list:
                print("-{} moving from {} to {}. ({} turns remain) {}% health."
                      .format(moving_item.name, moving_item.city_before_travel.name,
                              moving_item.destination.name, moving_item.travel_turns, moving_item.health))
        Functionalities.Utilities.text_separation()
        print("\n")

    def check_convoys(self):
        """
        Print and let you decide every convoy.
        :return:
        """
        if len(self.convoys) == 0:
            print("You dont have any convoys to select.\n")
        else:
            for i, x in enumerate(self.convoys):
                print("{}- {}. ({})\n".format(i + 1, x.name, x.city.name))
            option = self.select_boat_or_convoy(self.convoys)
            option.show_menu()

    def select_boat_or_convoy(self, type):
        """
        Select and return an unit.
        :param type:
        :return:
        """
        option = input()
        option = Functionalities.Utilities.correct_values(1, len(type), option)
        return type[option - 1]


    def list_cities(self, cities):
        """
        Print out list of cities, and let you choose one of them.
        :param cities:
        :return:
        """
        print("Where do you want to move?\n")
        for i, x in enumerate(cities):
            print("{}- {}.".format(i + 1, x.name))
        option = input("\n")
        option = Functionalities.Utilities.correct_values(1, len(cities), option)
        return cities[option - 1]

    def is_possible_to_change_cities(self, cities):
        """
        Check whether is possible to change to another city.
        :param cities:
        :return:
        """
        selected_city = self.list_cities(cities)
        for boat in self.boats:
            if boat.city == selected_city:
                return True, selected_city
        for convoy in self.convoys:
            if convoy.city == selected_city:
                return True, selected_city
        return False

    def change_city(self, cities):
        """
        If possible, changes city.
        :param cities:
        :return:
        """
        selected_city = self.is_possible_to_change_cities(cities)
        if not selected_city:
            print("You can't move to a city if you don't have a boat in it.")
        else:
            self.city = selected_city[1]
            print("You have moved to another city.")

    def change_turns_boats_and_convoys(self):
        for boat in self.boats:
            boat.change_turn()
        for convoy in self.convoys:
            convoy.change_turn()

    def check_if_have_to_move_city(self):
        if not self.not_remain_city_without_boats():
            self.move_city()

    def not_remain_city_without_boats(self):
        if self.city.have_commercial_office:
            return True
        else:
            for boat in self.boats:
                if boat.city == self.city:
                    return True
            for convoy in self.convoys:
                if convoy.city == self.city:
                    return True

            return False

    def move_city(self):
        for city in self.all_cities_list:
            if city.have_commercial_office:
                print("\n\nYou have been moved to {}\n\n".format(city.name))
                self.city = city

    def calculate_bill(self):
        sailors = self.sailors_bill()
        print("You have given {} to pay your sailors")

    def sailors_bill(self):
        sailors = 0
        for boat in self.boats:
            sailors += boat.sailors
        return sailors * 10

    def change_turn(self):
        self.turn += 1
        self.change_turns_boats_and_convoys()
        self.check_if_have_to_move_city()
        self.calculate_bill()
