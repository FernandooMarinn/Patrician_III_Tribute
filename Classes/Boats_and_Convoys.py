import Functionalities.Utilities


class Boat:
    def __init__(self, health, level, load, sailors, captain, catapult, name, city, player):

        self.name = name

        self.max_health = 0
        self.health = health
        self.level = level
        self.max_load = 0
        self.current_load = 0
        self.max_sailors = 0
        self.sailors = sailors
        self.artillery_space = 0
        self.catapult = catapult
        self.cannon = 0
        self.city = city
        self.city_before_travel = 0
        self.player = player

        # List with inicial cargo.
        self.skins = load[0]
        self.tools = load[1]
        self.beer = load[2]
        self.wine = load[3]
        self.cloth = load[4]
        self.empty_space = 0

        self.captain = captain

        self.destination = 0
        self.traveling = False
        self.travel_turns = 0
        self.cities_list = self.player.all_cities_list

        self.price_skins = 0
        self.price_tools = 0
        self.price_beer = 0
        self.price_wine = 0
        self.price_cloth = 0

        self.is_convoy = False
        self.enough_sailors = False

        self.firepower = 0

        self.check_level()
        self.check_current_load()
        self.city.boats.append(self)
        self.check_if_enough_sailors()

    def check_level(self):
        if self.level == 1:
            self.max_sailors = 20
            self.artillery_space = 7
            self.max_health = 100
            self.max_load = 120

        elif self.level == 2:
            self.max_sailors = 30
            self.artillery_space = 9
            self.max_health = 110
            self.max_load = 150

        elif self.level == 3:
            self.max_sailors = 40
            self.artillery_space = 12
            self.max_health = 125
            self.max_load = 180

    def check_current_load(self):
        """
        Calculate current ship load by adding every item and sailors.
        :return:
        """
        self.current_load = self.skins + self.tools + self.beer + self.wine + self.cloth + self.sailors
        self.empty_space = self.max_load - self.current_load

    def boat_deterioration(self):
        """
        When moving, change ship health, so it have to be repaired.
        :return:
        """
        if self.traveling:
            self.health -= 1
            if self.health < 11:
                print("Atention! Your ship {} is sinking."
                      .format(self.name))
            if self.health < 1:
                print("Your ship {} has sinked."
                      .format(self.name))
                return False

    def check_if_enough_sailors(self):
        """
        Can´t travel with less than 8 sailors.
        :return:
        """
        if self.sailors < 8:
            self.enough_sailors = False
        else:
            self.enough_sailors = True

    def choose_city_to_travel(self, cities):
        """
        Enumerate and choose a city from a list.
        :param cities:
        :return:
        """
        if self.enough_sailors:
            print("Where do you want to move?\n")
            for i, x in enumerate(cities):
                print("{}- {}.".format(i + 1, x.name))
            option = input("\n")
            option = Functionalities.Utilities.correct_values(1, len(cities), option)
            self.check_distance_between_cities(option - 1)
        else:
            print("You can´t move with less than 8 sailors.\n")

    def check_distance_between_cities(self, option):
        """
        Check distance between cities. If they are close, will take fewer turns to move.
        :param option:
        :return:
        """
        # Terminar esto
        cities = self.cities_list
        distance = self.city.possition + cities[option].possition
        if self.city == cities[option]:
            print("You are already in {}".format(self.city.name))
        else:
            print("{} is now moving to {}. Will take {} turns."
                  .format(self.name, cities[option].name, distance))
            self.set_travel(distance, cities[option])

    def set_travel(self, distance, destination):
        """
        Start moving to another city.
        :param distance:
        :param destination:
        :return:
        """
        self.travel_turns = distance
        self.traveling = True
        self.destination = destination
        self.boat_deterioration()
        self.city_before_travel = self.city
        if self in self.city.boats:
            self.city.boats.remove(self)
        self.city = False

    def while_traveling(self):
        """
        Works every turn until arrival. Check if has arrived and calculate how many turns remain.
        :return:
        """
        if self.travel_turns > 1:
            self.travel_turns -= 1
        elif self.travel_turns == 1:
            self.city = self.destination
            self.city.boats.append(self)
            self.traveling = False
            self.destination = 0
            print("Your boat {} has arrived at {}."
                  .format(self.name, self.city.name))

    def check_if_traveling(self):
        """
        Return True if in open sea.
        :return:
        """
        if self.traveling:
            return True
        else:
            return False

    def check_boat(self):
        """
        Check everything that is important in a boat object. Load, empty space, captain, sailors and level.
        :return:
        """
        print("-" * 60)
        self.check_current_load()
        print("Your boat {} have:\n"
              "{} skins at {} coins.\n"
              "{} tools at {} coins.\n"
              "{} beer at {} coins.\n"
              "{} wine at {} coins.\n"
              "{} cloth at {} coins.\n"
              .format(self.name, self.skins, self.price_skins, self.tools, self.price_tools, self.beer,
                      self.price_beer, self.wine, self.price_wine, self.cloth, self.price_cloth))
        print("\nThis ship have a maximum cargo of {} units. Is currently loaded with {}. {} empty spaces remain.\n"
              .format(self.max_load, self.current_load, self.max_load - self.current_load))
        if self.captain:
            print("This ship has a captain. There are {} sailors.\n"
                  .format(self.sailors))
        else:
            print("This ship doesn't have a captain. There are {} sailors, and total space for {}.\n"
                  .format(self.sailors, self.max_sailors))
        print("You are in {}. This ship's level is {}."
              .format(self.city.name, self.level))
        print("-" * 60, "\n")

    def check_if_can_become_convoy(self):
        """
        Check if ship has everything to become a convoy.
        :return:
        """
        if self.captain:
            if self.sailors > 19:
                self.set_firepower()
                if self.firepower > 7:
                    election = input("Do you want to create a new convoy, named {}?\n"
                                     "1- Yes.\n"
                                     "2- No.\n"
                                     .format(self.name))
                    election = Functionalities.Utilities.correct_values(1, 2, election)
                    if election == 1:
                        return True
                    else:
                        return False
                else:
                    print("Your boat has less than 8 firepower.")
            else:
                print("Your boat has less than 20 sailors.")
        else:
            print("In order to create a convoy, you need a captain.")

    def show_menu(self):
        """
        Print ship menu and takes choosen option.
        :return:
        """
        while not self.check_if_traveling():
            print("What do you want to do with your boat {}?\n"
                  "1- Buy from city.\n"
                  "2- Sell to city.\n"
                  "3- Transfer items to warehouse.\n"
                  "4- Check cargo.\n"
                  "5- Move to another city.\n"
                  "6- Exit.\n"
                  .format(self.name))
            option = input("")
            option = Functionalities.Utilities.correct_values(1, 6, option)
            if option == 6:
                break
            else:
                self.choose_options(option)

    def choose_options(self, option):
        """
        Depending on choosen option, uses it´s function.
        :param option:
        :return:
        """
        if option == 1:
            Functionalities.Utilities.buy_from_city(self)
        elif option == 2:
            Functionalities.Utilities.sell_to_city(self)
        elif option == 3:
            self.ask_witch_direction_to_move()
        elif option == 4:
            self.check_boat()
        elif option == 5:
            self.choose_city_to_travel(self.player.all_cities_list)

    def ask_witch_direction_to_move(self):
        if self.check_if_commercial_office():
            print("What do you want to do?\n"
                  "1- Move from ship to warehouse.\n"
                  "2- Move from warehouse to ship.\n"
                  "3- Exit.\n")
            option = input("\n")
            option = Functionalities.Utilities.correct_values(1, 3, option)
            if option == 3:
                pass
            else:
                item_name = Functionalities.Utilities.select_item()
            if option == 1:
                self.move_from_ship(item_name)
            elif option == 2:
                self.move_from_warehouse(item_name)

    def move_from_ship(self, name):
        while True:
            product = Functionalities.Utilities.choose_products(name, self)
            product_price = Functionalities.Utilities.choose_prices(name, self)
            print("You have {} {} at {} coins. How many do you want to move?\n"
                  .format(product, name, product_price))
            option = input("\n")
            option = Functionalities.Utilities.correct_values(0, product, option)
            self.moving_products(name, option, product_price, self, self.city.commercial_office)

    def moving_products(self, name, how_many, price, origin, destiny):
        Functionalities.Utilities.decrease_product_number(origin, [how_many, name])
        Functionalities.Utilities.increase_product_number(destiny, [how_many, name])
        old_items = Functionalities.Utilities.choose_products(name, destiny)
        old_price = Functionalities.Utilities.choose_prices(name, destiny)
        new_price = Functionalities.Utilities.calculate_average_price(old_price, old_items, price, how_many)
        Functionalities.Utilities.change_prices(name, new_price, destiny)

    def move_from_warehouse(self, name):
        while True:
            product = Functionalities.Utilities.choose_products(name, self.city.commercial_office)
            product_price = Functionalities.Utilities.choose_prices(name, self.city)
            print("You have {} {} at {} coins. How many do you want to move?\n"
                  .format(product, name, product_price))
            option = input("\n")
            option = Functionalities.Utilities.correct_values(0, product, option)
            self.moving_products(name, option, product_price, self.city.commercial_office, self)

    def check_if_commercial_office(self):
        if not self.city.commercial_office:
            print("There is not a commercial office in this city.\n")
            return False
        else:
            return True

    def set_firepower(self):
        """
        Set firepower of a ship.
        :return:
        """
        self.firepower = self.catapult + (self.cannon * 2)

    def change_turn(self):
        """
        Everything that have to be done in each ship when a turn passes.
        :return:
        """
        if self.check_if_traveling():
            self.while_traveling()
            self.boat_deterioration()
        self.check_level()
        self.set_firepower()


# Convoys, to control ships together.
class Convoy:
    def __init__(self, name, city, boats):
        self.boats = boats
        self.min_level = 0
        self.name = name
        self.city = city

        self.traveling = False
        self.travel_duration = 0
        self.destination = 0
        self.travel_turns = 0

        self.all_healths = []
        self.medium_health = 0
        self.min_health = 0

        self.is_convoy = True

    def check_min_lvl(self):
        all_levels = []
        for boat in self.boats:
            all_levels.append(boat.level)
        self.min_level = min(all_levels)

    def set_travel(self, distance, destination):
        self.travel_turns = distance
        self.traveling = True
        self.destination = destination
        for boat in self.boats:
            boat.traveling = True

    def while_traveling(self):
        if self.travel_turns > 0:
            self.travel_turns -= 1
        elif self.travel_turns == 0:
            self.city = self.destination
            self.traveling = False
            self.destination = 0
            for boat in self.boats:
                boat.traveling = False

    def check_if_traveling(self):
        if self.traveling:
            return True
        else:
            return False

    def convoy_deterioration(self):
        for boat in self.boats:
            boat.boat_deterioration()

    def set_all_health(self):
        self.all_healths = [boat.health for boat in self.boats]

    def set_medium_health(self):
        self.medium_health = Functionalities.Utilities.calculate_list_mean(self.all_healths)

    def set_minimum_health(self):
        self.min_health = min(self.all_healths)

    def calculate_all_healths(self):
        self.set_minimum_health()
        self.set_medium_health()
        self.set_all_health()

    def change_turn(self):
        self.convoy_deterioration()
        self.calculate_all_healths()


    def show_menu(self):
        print("Convoy menu.\n")