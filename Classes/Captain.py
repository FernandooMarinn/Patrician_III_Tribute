from Classes.Comercial_Office import Trader
import Functionalities.Utilities

class Captain(Trader):
    def __init__(self, boat, player):
        self.boat = boat
        self.player = player

        self.skins_instructions = [0, 0, 0, "skins"]
        self.tools_instructions = [0, 0, 0, "tools"]
        self.beer_instructions = [0, 0, 0, "beer"]
        self.cloth_instructions = [0, 0, 0, "cloth"]
        self.wine_instructions = [0, 0, 0, "wine"]
        self.grain_instructions = [0, 0, 0, "grain"]

        self.trading_instructions = [self.skins_instructions, self.tools_instructions, self.beer_instructions,
                                     self.wine_instructions, self.cloth_instructions, self.grain_instructions]

        self.route = {}

    def show_menu(self):
        while True:
            print("Want do you want to do?\n"
                  "1- Check route.\n"
                  "2- Modify route.\n"
                  "3- Change trading options.\n"
                  "4- Dismiss captain.\n"
                  "5- Exit.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 4, option)
            if option == 5:
                break
            elif option == 4:
                self.boat.fire_captain()
                break
            else:
                self.choose_option(option)

    def get_all_route_cities(self):
        return [city.name for city in self.route.keys()]

    def choose_option(self, option):
        """
        Selects an option from trader menu.
        :param option:
        :return:
        """
        if option == 1:
            self.check_route()
        elif option == 2:
            self.modify_route()
        elif option == 3:
            self.modify_city()

    def check_route(self):
        all_cities = self.get_all_route_cities()

        if len(all_cities) == 0:
            print("Your route is still empty")
            return False
        else:
            for num, city in enumerate(all_cities):
                print("{}.- {}.\n".format(num, city))
            return True

    def modify_route(self):
        print("What do you want to do?\n"
              "1- Add city to route.\n"
              "2- Delete city from route.\n"
              "3- Exit.")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 3, option)

        if option == 3:
            pass
        elif option == 2:
            if self.check_route():
                print("What city do you want to remove?\n")
                option = input()
                option = Functionalities.Utilities.correct_values(1, len(self.get_all_route_cities()), option)
                del self.route[option]
                self.adjust_route()
            else:
                pass
        elif option == 1:
            cities = self.boat.player.all_cities_list
            print("Witch city do you want to add?\n")
            for num, city in cities:
                print("{}- {}.\n".format(num + 1, city.name))

            option = input("\n")
            option = Functionalities.Utilities.correct_values(1, len(cities), option)
            self.add_new_city_to_route(cities[option])

    def adjust_route(self):
        keys = sorted(self.route.keys())
        for i in range(len(self.route)):
            self.route[keys[i]] = i + 1

    def add_new_city_to_route(self, city):
        new_number = max(self.route.keys()) + 1

        self.route[new_number] = {city.name: self.trading_instructions}

    def modify_city(self):
        all_cities = self.get_all_route_cities()
        for num, city in enumerate(all_cities):
            print("{}.- {}.\n".format(num, city))

        print("Witch city do you want do modify?")