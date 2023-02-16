import Functionalities.Utilities


class Boat:
    def __init__(self, health, level, load, sailors, captain, cannon, name, city, player):

        self.name = name
        self.city = city

        self.max_health = 0
        self.health = health
        self.level = level
        self.max_load = 0
        self.current_load = 0
        self.max_sailors = 0
        self.sailors = sailors

        self.artillery_space = 0
        self.cannon = cannon
        self.bombard = 0
        self.dagger = 0

        self.city_before_travel = 0
        self.player = player

        # List with inicial cargo.
        self.skins = load[0]
        self.tools = load[1]
        self.beer = load[2]
        self.wine = load[3]
        self.cloth = load[4]
        self.grain = load[5]

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
        self.price_grain = 0

        self.is_convoy = False
        self.enough_sailors = False

        self.firepower = 0

        self.check_level()
        self.set_empty_space_and_max_load()
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

    def set_empty_space_and_max_load(self):
        """
        Calculate current ship load by adding every item and sailors.
        :return:
        """
        self.current_load = self.skins + self.tools + self.beer + self.wine + self.cloth + self.sailors + self.dagger + \
                            self.grain * 10
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
        Check and print everything that is important in a boat object. Load, empty space, captain, sailors and level.
        :return:
        """
        Functionalities.Utilities.text_separation()

        Functionalities.Utilities.set_price_to_zero(self)
        self.set_empty_space_and_max_load()
        print("Your boat {} have:\n"
              "{} skins at {} coins.\n"
              "{} tools at {} coins.\n"
              "{} beer at {} coins.\n"
              "{} wine at {} coins.\n"
              "{} cloth at {} coins.\n"
              "{} grain at {} coins.\n"
              .format(self.name, self.skins, self.price_skins, self.tools, self.price_tools, self.beer,
                      self.price_beer, self.wine, self.price_wine, self.cloth, self.price_cloth, self.grain,
                      self.price_grain))

        print("\nThis ship have a maximum cargo of {} units. Is currently loaded with {}. {} empty spaces remain.\n"
              .format(self.max_load, self.current_load, self.max_load - self.current_load))
        print("There are {} daggers, {} cannons and {} bombards in this ship.\n"
              .format(self.dagger, self.cannon, self.bombard))

        if self.captain:
            print("This ship has a captain. There are {} sailors.\n"
                  .format(self.sailors))
        else:
            print("This ship doesn't have a captain. There are {} sailors, and total space for {}.\n"
                  .format(self.sailors, self.max_sailors))
        print("You are in {}. This ship's level is {}."
              .format(self.city.name, self.level))
        Functionalities.Utilities.text_separation()

    def check_if_can_become_convoy(self):
        """
        Check if ship has everything to become a convoy.
        :return: True if a new convoy should be created, False otherwise.
        """
        if not self.captain:
            print("In order to create a convoy, you need a captain.")
            return False

        if self.sailors < 20:
            print("Your boat has less than 20 sailors.")
            return False

        self.set_firepower()

        if self.firepower < 8:
            print("Your boat has less than 8 firepower.")
            return False

        election = input("Do you want to create a new convoy, named {}?\n"
                         "1- Yes.\n"
                         "2- No.\n"
                         .format(self.name))
        election = Functionalities.Utilities.correct_values(1, 2, election)

        if election == 1:
            return True
        else:
            return False

    def turn_into_convoy(self):
        if self.check_if_can_become_convoy():
            new_convoy = Convoy(self.name, self.city, [self], self.player, self.cities_list)
            self.player.convoys.append(new_convoy)
            self.city.convoys.append(new_convoy)
            self.city.boats.remove(self)
            self.player.boats.remove(self)
            new_convoy.initialize_convoy()
            self.player.achievements.check_when_first_convoy()

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
                  "6- Create a convoy.\n"
                  "7- Exit.\n"
                  .format(self.name))

            option = input("")
            option = Functionalities.Utilities.correct_values(1, 7, option)

            if option == 7:
                break
            elif option == 6:
                self.turn_into_convoy()
                break
            else:
                self.choose_options(option)

    def choose_options(self, option):
        """
        Depending on chosen option, uses its function.
        :param option:
        :return:
        """
        options = {
            1: lambda: Functionalities.Utilities.buy_from_city(self),
            2: lambda: Functionalities.Utilities.sell_to_city(self),
            3: lambda: Functionalities.Utilities.ask_witch_direction_to_move(self),
            4: self.check_boat,
            5: lambda: Functionalities.Utilities.choose_city_to_travel(self, self.player.all_cities_list),
            6: self.turn_into_convoy
        }

        if option in options:
            options[option]()

    def set_firepower(self):
        """
        Set firepower of a ship dependig on level.
        :return:
        """
        if self.dagger > self.sailors:
            dagger_value = self.sailors
        else:
            dagger_value = self.dagger
        if self.cannon + self.bombard > self.artillery_space:
            if self.bombard >= self.artillery_space:
                self.firepower = self.artillery_space * 2 + (round(dagger_value * 0.35))
            else:
                max_cannon_value = self.artillery_space - self.bombard
                self.firepower = max_cannon_value + (self.bombard * 2) + (round(0.35 * dagger_value))
        else:
            self.firepower = self.bombard * 2 + self.cannon + (round(0.35 * dagger_value))
        if self.captain:
            self.firepower += 2

    def change_turn(self):
        """
        Everything that have to be done in each ship when a turn passes.
        :return:
        """
        if self.check_if_traveling():
            Functionalities.Utilities.while_traveling(self)
            self.boat_deterioration()
        self.check_level()
        self.set_firepower()
        Functionalities.Utilities.set_price_to_zero(self)


# Convoys, to control ships together.
class Convoy:
    """
    Useful for mid/late game. It allows to create groups of ships, and control them in a simple way.
    """

    def __init__(self, name, city, boats, player, cities_list):
        self.boats = boats
        self.min_level = 0
        self.name = name
        self.city = city

        self.dagger = 0
        self.cannon = 0
        self.bombard = 0

        self.player = player
        self.cities_list = cities_list

        self.traveling = False
        self.travel_duration = 0
        self.destination = 0
        self.travel_turns = 0
        self.city_before_travel = 0

        self.all_healths = []
        self.health = 0
        self.min_health = 0

        self.is_convoy = True

        self.sailors = 0
        self.captains = 1

        self.skins = 0
        self.tools = 0
        self.beer = 0
        self.wine = 0
        self.cloth = 0
        self.grain = 0

        self.max_load = 0
        self.current_cargo = 0

        self.price_skins = 0
        self.price_tools = 0
        self.price_beer = 0
        self.price_wine = 0
        self.price_cloth = 0
        self.price_grain = 0

        self.empty_space = 0

        self.initialize_convoy()

    def initialize_convoy(self):
        """
        When a convoy is created, this function creates all its metadata
        :return:
        """
        self.set_sailors_and_captains()
        self.set_every_item()
        self.set_all_health()
        self.set_medium_health()
        self.set_minimum_health()
        self.set_empty_space_and_max_load()
        self.set_firepower()
        Functionalities.Utilities.set_price_to_zero(self)

    def set_firepower(self):
        # Set firepower for each boat in the convoy.
        for boat in self.boats:
            boat.set_firepower()

    def check_min_lvl(self):
        # Check min level in the convoy.
        all_levels = []
        for boat in self.boats:
            all_levels.append(boat.level)
        self.min_level = min(all_levels)

    def set_empty_space_and_max_load(self):
        """
        Calculates empty space, and maximum load depending on each ship cargo.
        :return:
        """
        total_space = 0
        max_load = 0
        for boat in self.boats:
            boat.set_empty_space_and_max_load()
            total_space += boat.empty_space
            max_load += boat.max_load
        self.empty_space = total_space
        self.max_load = max_load

    def set_every_item(self):
        """
        Calculates total inventory, iterating over all the boats in the convoy.
        :return:
        """
        skins = 0
        tools = 0
        beer = 0
        wine = 0
        cloth = 0
        grain = 0

        dagger = 0
        cannon = 0
        bombard = 0

        for boat in self.boats:
            skins += boat.skins
            tools += boat.tools
            beer += boat.beer
            wine += boat.wine
            cloth += boat.cloth
            grain += boat.grain
            dagger += boat.dagger
            cannon += boat.cannon
            bombard += boat.bombard

        self.skins = skins
        self.tools = tools
        self.beer = beer
        self.wine = wine
        self.cloth = cloth
        self.grain = grain
        self.dagger = dagger
        self.cannon = cannon
        self.bombard = bombard

        self.current_cargo = self.skins + self.tools + self.beer + self.wine + self.cloth + self.sailors + \
                             (self.grain * 10) + self.dagger + self.cannon * 3 + self.bombard * 3

    def set_sailors_and_captains(self):
        """
        Calculates how many sailors and captains are in the convoy.
        :return:
        """
        sailors = 0
        captains = 0
        for boat in self.boats:
            sailors += boat.sailors
            if boat.captain:
                captains += 1
        self.sailors = sailors
        self.captains = captains

    def set_travel(self, distance, destination):
        """
        Start traveling.
        :param distance:
        :param destination:
        :return:
        """
        self.travel_turns = distance
        self.traveling = True
        self.destination = destination
        for boat in self.boats:
            boat.traveling = True

    def while_traveling(self):
        """
        When the convoy is traveling, this function calculates how long it takes to arrive, and set the data in arrival.
        :return:
        """
        if self.travel_turns > 0:
            self.travel_turns -= 1

        elif self.travel_turns == 0:
            self.city = self.destination
            self.traveling = False
            self.destination = 0
            for boat in self.boats:
                boat.traveling = False

        self.player.achievements.visiting_city(self.city)

    def check_if_traveling(self):
        if self.traveling:
            return True
        else:
            return False

    def boat_deterioration(self):
        for boat in self.boats:
            boat.boat_deterioration()

    def set_all_health(self):
        self.all_healths = [boat.health for boat in self.boats]

    def set_medium_health(self):
        self.health = Functionalities.Utilities.calculate_list_mean(self.all_healths)

    def set_minimum_health(self):
        self.min_health = min(self.all_healths)

    def calculate_all_healths(self):
        if len(self.boats) > 0:
            self.set_minimum_health()
            self.set_medium_health()
            self.set_all_health()

    def show_menu(self):
        """
        Prints out convoy menu.
        :return:
        """
        while True:
            print("1- Buy from city.\n"
                  "2- Sell to city.\n"
                  "3- Move items to warehouse.\n"
                  "4- Check convoy.\n"
                  "5- Move to another city.\n"
                  "6- Add boat to convoy.\n"
                  "7- Dissolve convoy.\n"
                  "8- Exit.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 8, option)
            # 8 is selected when we want to exit the menu, so we break the loop.
            if option == 8:
                break
            # 7 is for dissolving the convoy. If we call it for another function it gets stuck in the loop.
            elif option == 7:
                Functionalities.Utilities.delete_convoy(self)
                break
            # 5 when we choose a city to travel. we loose control on the convoy, so we have to break the loop.
            elif option == 5:
                Functionalities.Utilities.choose_city_to_travel(self, self.cities_list)
                break
            else:
                self.choose_option(option)

    def choose_option(self, option):
        if option == 1:
            Functionalities.Utilities.buy_from_city(self)
        elif option == 2:
            Functionalities.Utilities.sell_to_city(self)
        elif option == 3:
            Functionalities.Utilities.ask_witch_direction_to_move(self)
        elif option == 4:
            self.check_convoy()
        elif option == 6:
            self.add_boat()

    def add_boat(self):
        """
        Adds a new boat to the convoy, if there is any in the town.
        :return:
        """
        boat = Functionalities.Utilities.choose_boat(self.city)
        if not boat:
            pass
        else:
            print("Do you want {} to join convoy {}?\n"
                  "1- Yes.\n"
                  "2- No.\n".format(boat.name, self.name))
            option = input()
            option = Functionalities.Utilities.correct_values(1, 2, option)
            if option == 1:
                self.boats.append(boat)
                self.initialize_convoy()
                self.player.boats.remove(boat)
                self.city.boats.remove(boat)

    def dissolve_convoy(self):
        """
        To delete the convoy. Return every boat to the city.
        :return:
        """
        print("Do you want to dissolve convoy {}?"
              "1- Yes.\n"
              "2- No.\n".format(self.name))
        option = input()
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if option == 1:
            Functionalities.Utilities.delete_convoy(self)

    def check_convoy(self):
        """
        Print out every useful information about a convoy.
        :return:
        """
        Functionalities.Utilities.text_separation()
        self.initialize_convoy()
        print(f"""This is the {self.name} convoy, currently in {self.city.name}. It has {len(self.boats)} ships in it. Current cargo is:

-Skins: {self.skins} at {self.price_skins} coins.
-Tools: {self.tools} at {self.price_tools} coins.
-Beer: {self.beer} at {self.price_beer} coins.
-Wine: {self.wine} at {self.price_wine} coins.
-Cloth: {self.cloth} at {self.price_cloth} coins.
-Grain: {self.grain} at {self.price_grain} coins.

Maximum load is {self.max_load} units, and {self.current_cargo} are already full.
It can take another {self.empty_space} units.

Average health among all ships is {self.health} while the minimum ship health is {self.min_health}.
This convoy has a total of {self.sailors} sailors and {self.captains} captains.
""")
        Functionalities.Utilities.text_separation()

    def change_turn(self):
        if self.traveling:
            self.boat_deterioration()
            Functionalities.Utilities.while_traveling(self)
        self.calculate_all_healths()
        Functionalities.Utilities.set_price_to_zero(self)

    def distribute_items(self, items):
        product = items[1]
        quantity = items[0]

        for boat in self.boats:
            boat.set_empty_space_and_max_load()
            if boat.empty_space >= quantity:
                Functionalities.Utilities.increase_product_number(boat, [quantity, product])
                break
            else:
                Functionalities.Utilities.increase_product_number(boat, [boat.empty_space, product])
                quantity -= boat.empty_space

    def decrease_items_convoy(self, items):
        product = items[1]
        quantity = items[0]

        for boat in self.boats:
            boat_items = Functionalities.Utilities.choose_products(product, boat)
            if boat_items >= quantity:
                Functionalities.Utilities.decrease_product_number(boat, [quantity, product])
                break
            else:
                Functionalities.Utilities.decrease_product_number(boat, [boat_items, product])
                quantity -= boat_items
