import Functionalities.Utilities


class Boat:
    def __init__(self, health, level, load, sailors, captain, cannons, name, city, player):

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
        self.player = player

        # List with inicial cargo.
        self.skins = load[0]
        self.tools = load[1]
        self.beer = load[2]
        self.wine = load[3]
        self.cloth = load[4]

        self.captain = captain

        self.destination = 0
        self.traveling = False
        self.travel_turns = 0

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

    def check_cargo(self):
        print("You have {} skins, {} tools, {} beer, {} wine, {} cloth.\n"
              .format(self.skins, self.tools, self.beer, self.wine, self.cloth))
        if self.captain:
            print("\nThis boat has a captain.")
        else:
            print("\nThis boat doesn't have a captain")

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

    def show_options(self):
        while True:
            print("What do you want to do whith your boat {}?\n"
                  "1- Buy from city.\n"
                  "2- Sell to city.\n"
                  "3- Check cargo.\n"
                  "4- Move to another city.\n"
                  "5- Exit.\n"
                  .format(self.name))
            option = input("")
            option = Functionalities.Utilities.correct_values(1, 5, option)
            if option == 5:
                break
            else:
                self.choose_options(option)

    def choose_options(self, option):
        if option == 1:
            self.buy_from_city()
        elif option == 2:
            self.sell_to_city()
        elif option == 3:
            self.check_cargo()
        elif option == 4:
            self.choose_city_to_travel()

    def buy_from_city(self):
        current_city = self.city
        current_city.calculate_prices()
        current_city.show_prices()

    def sell_to_city(self):
        pass

    def choose_city_to_travel(self):
        print("Where do you want to go?\n"
              "1- Lubeck.\n"
              "2- Rostock. \n"
              "3- Malmo. \n"
              "4- Stettin.\n"
              "5- Gdanks.\n")
        option = input("\n")
        option = Functionalities.Utilities.correct_values(1, 5, option)
        self.check_distance_between_cities(option - 1)

    def check_distance_between_cities(self, option):
        cities = Functionalities.Utilities.create_cities()
        distance = self.city.possition + cities[option].possition
        if self.city == cities[option]:
            print("You alredy are in {}".format(self.city.name))
        else:
            self.set_travel(distance, option)

    def set_travel(self, distance, destination):
            self.travel_turns = distance
            self.traveling = True
            self.destination = destination

    def while_traveling(self):
        if self.travel_turns > 0:
            self.travel_turns -= 1
            if self.travel_turns == 0:
                self.city = self.destination
                self.traveling = False
                self.destination = 0
        else:
            pass

    def turn_change(self):
        self.while_traveling()





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

