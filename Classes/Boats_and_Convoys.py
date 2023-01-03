import Functionalities.Utilities


class Boat:
    def __init__(self, health, level, load, sailors, captain, cannons, name, city, player, cities_list):

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
        self.cities_list = cities_list

        self.price_skins = 0
        self.price_tools = 0
        self.price_beer = 0
        self.price_wine = 0
        self.price_cloth = 0

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
        if self.traveling == True:
            self.health -= 1
            if self.health < 11:
                print("Atention! Your ship {} is sinking."
                      .format(self.name))
            if self.health < 1:
                print("Your ship {} has sinked."
                      .format(self.name))
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
        print("-" * 60)
        print("Your boat {} have:\n"
              "{} skins at {} coins.\n"
              "{} tools at {} coins.\n"
              "{} beer at {} coins.\n"
              "{} wine at {} coins.\n"
              "{} cloth at {} coins.\n"
              .format(self.name, self.skins, self.price_skins, self.tools, self.price_tools, self.beer,
                      self.price_beer, self.wine, self.price_wine, self.cloth, self.price_cloth))
        if self.captain:
            print("This boat has a captain. There are {} sailors.\n"
                  .format(self.sailors))
        else:
            print("This boat doesn't have a captain. There are {} sailors.\n"
                  .format(self.sailors))
        print("You are in {}."
              .format(self.city.name))
        print("-" * 60, "\n")

    def check_if_can_become_convoy(self):
        if self.captain:
            if self.sailors > 19:
                if self.cannons > 7:
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
                    print("Your boat has less than 8 cannons.")
            else:
                print("Your boat has less than 20 sailors.")
        else:
            print("In order to create a convoy, you need a captain.")

    def show_options(self):
        while not self.check_if_traveling():
            print("What do you want to do with your boat {}?\n"
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
        # Select current city, update prices and choose a product.
        current_city = self.city
        current_city.calculate_prices()
        current_city.show_prices()
        choosen_product = current_city.choose_product()
        # Selecting how many we want to buy, and returning it`s price.
        new_products = current_city.how_many_buy(choosen_product)
        product_prices = self.choose_prices(new_products[1])
        product = self.choose_products(new_products[1])
        new_price = new_products[2]
        average_price = Functionalities.Utilities.calculate_average_price(product_prices,
                                                                          product, new_price, product + new_products[0])
        # Adding bought products and changing it`s mean price.
        self.add_products(new_products)
        self.change_prices(new_products[1], average_price)

    def sell_to_city(self):
        # Select current city, update prices and choose a product.
        current_city = self.city
        current_city.calculate_prices()
        current_city.show_prices()
        choosen_product = current_city.choose_product()
        # Selecting how many we want to sell, and returning it`s price.
        new_products = current_city.how_many_sell(choosen_product)
        product_prices = self.choose_prices(new_products[1])
        product = self.choose_products(new_products[1])
        new_price = new_products[2]
        average_price = Functionalities.Utilities.calculate_average_price \
            (product_prices, product, new_price, product + new_products[0])
        # deleting selled products.
        self.decrease_products(new_products)


    def change_prices(self, name, new_price):
        if name == "skins":
            self.price_skins = new_price
        elif name == "tools":
            self.price_tools = new_price
        elif name == "beer":
            self.price_beer = new_price
        elif name == "wine":
            self.price_wine = new_price
        elif name == "cloth":
            self.price_cloth = new_price

    def choose_products(self, name):
        if name == "skins":
            return self.skins
        elif name == "tools":
            return self.tools
        elif name == "beer":
            return self.beer
        elif name == "wine":
            return self.wine
        elif name == "cloth":
            return self.cloth

    def choose_prices(self, name):
        if name == "skins":
            return self.price_skins
        elif name == "tools":
            return self.price_tools
        elif name == "beer":
            return self.price_beer
        elif name == "wine":
            return self.price_wine
        elif name == "cloth":
            return self.price_cloth

    def add_products(self, products):
        quantity = products[0]
        if products[1] == "skins":
            self.skins += quantity
        elif products[1] == "tools":
            self.tools += quantity
        elif products[1] == "beer":
            self.beer += quantity
        elif products[1] == "wine":
            self.wine += quantity
        elif products[1] == "cloth":
            self.cloth += quantity

    def decrease_products(self, products):
        quantity = products[0]
        if products[1] == "skins":
            self.skins -= quantity
        elif products[1] == "tools":
            self.tools -= quantity
        elif products[1] == "beer":
            self.beer -= quantity
        elif products[1] == "wine":
            self.wine -= quantity
        elif products[1] == "cloth":
            self.cloth -= quantity

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
        self.travel_turns = distance
        self.traveling = True
        self.destination = destination
        self.boat_deterioration()

    def while_traveling(self):
        if self.travel_turns > 1:
            self.travel_turns -= 1
        elif self.travel_turns == 1:
            self.city = self.destination
            self.traveling = False
            self.destination = 0
            print("Your boat {} has arrived at {}."
                  .format(self.name, self.city.name))

    def check_if_traveling(self):
        if self.traveling:
            return True
        else:
            return False

    def change_turn(self):
        if self.check_if_traveling():
            self.while_traveling()
            self.boat_deterioration()


# Convoys, to control ships together.
class Convoy:
    def __init__(self, name, city, boats):
        self.boats = []
        self.min_level = 0
        self.name = name
        self.city = city
        self.traveling = False
        self.travel_duration = 0
        self.destination = 0
        self.all_healths = []
        self.medium_health = 0
        self.min_health = 0

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
        if self.traveling == True:
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
