import Functionalities.Utilities

class City:
    def __init__(self, name, skins_consumption_ratio, tools_consumption_ratio, beer_consumption_ratio,
                 wine_consumption_ratio, cloth_consumption_ratio, initial_skins, initial_tools, initial_beer,
                 initial_wine, initial_cloth, skins_production, tools_production, beer_production, wine_production,
                 cloth_production, can_produce_skins, can_produce_tools, can_produce_beer, can_produce_wine,
                 can_produce_cloth, commercial_office, possition):

        self.coins = 10000
        # Products quantity.
        self.skins = initial_skins
        self.tools = initial_tools
        self.beer = initial_beer
        self.wine = initial_wine
        self.cloth = initial_cloth
        self.name = name

        # City consuption of each item.
        self.skins_consumption_ratio = skins_consumption_ratio
        self.tools_consumption_ratio = tools_consumption_ratio
        self.beer_consumption_ratio = beer_consumption_ratio
        self.wine_consumption_ratio = wine_consumption_ratio
        self.cloth_consumption_ratio = cloth_consumption_ratio

        self.skins_consumption = 0
        self.tools_consumption = 0
        self.beer_consumption = 0
        self.wine_consumption = 0
        self.cloth_consumption = 0

        # City base production of each item.
        self.skins_production = skins_production
        self.tools_production = tools_production
        self.beer_production = beer_production
        self.wine_production = wine_production
        self.cloth_production = cloth_production

        # Factories in the city
        self.skins_factories = 0
        self.tools_factories = 0
        self.beer_factories = 0
        self.wine_factories = 0
        self.cloth_factories = 0
        self.factories_queue = []

        # Is it possible to create factories
        self.can_produce_skins = can_produce_skins
        self.can_produce_tools = can_produce_tools
        self.can_produce_beer = can_produce_beer
        self.can_produce_wine = can_produce_wine
        self.can_produce_cloth = can_produce_cloth

        # Max and min values for each product.
        self.max_price_skins = 1400
        self.min_price_skins = 650
        self.max_price_tools = 560
        self.min_price_tools = 250
        self.max_price_beer = 75
        self.min_price_beer = 30
        self.max_price_wine = 440
        self.min_price_wine = 200
        self.max_price_cloth = 440
        self.min_price_cloth = 200

        # Current values.
        self.price_skins = 0
        self.price_tools = 0
        self.price_beer = 0
        self.price_wine = 0
        self.price_cloth = 0
        self.houses = 250
        self.population = 1000

        self.commercial_office = commercial_office
        self.possition = possition

        self.boats = []
        self.convoys = []


    def create_houses(self):
        # Automatically create houses when needed.
        while self.population > (self.houses - 10) * 4:
            self.houses += 1
            self.coins -= 100

    def get_taxes(self):
        # Get taxes from every house.
        self.coins += 10 * self.houses


    def set_consumption(self):
        # Set the city consumption depending of population growth.
        self.skins_consumption = round((self.population * self.skins_consumption_ratio) / 1000)
        self.tools_consumption = round((self.population * self.tools_consumption_ratio) / 1000)
        self.beer_consumption = round((self.population * self.beer_consumption_ratio) / 1000)
        self.wine_consumption = round((self.population * self.wine_consumption_ratio) / 1000)
        self.cloth_consumption = round((self.population * self.cloth_consumption_ratio) / 1000)

    def calculate_individual_price(self, max_value, min_value, quantity):
        """
        Set individual price of a product.
        :param max_value:
        :param min_value:
        :param quantity:
        :return:
        """
        if quantity == 0:
            return max_value
        elif quantity >= 100:
            return min_value
        else:
            current_price = round(max_value - ((max_value - min_value) * (quantity / 100)))
            return current_price

    def calculate_sell_and_buy_prices(self, max_value, min_value, quantity):
        how_much = input("How many do you want to trade?\n")
        how_much = Functionalities.Utilities.correct_values(0, quantity, how_much)
        start_price = self.calculate_individual_price(max_value, min_value, quantity)
        finish_price = self.calculate_individual_price(max_value, min_value, quantity - how_much)
        mean = (start_price + finish_price) / 2
        # Retocar, crear una formula para contemplar cosas por encima de 100.

    def calculate_prices(self):
        # Calculate every price, depending of available quantity.
        self.price_skins = self.calculate_individual_price(self.max_price_skins, self.min_price_skins, self.skins)
        self.price_tools = self.calculate_individual_price(self.max_price_tools, self.min_price_tools, self.tools)
        self.price_beer = self.calculate_individual_price(self.max_price_beer, self.min_price_beer, self.beer)
        self.price_wine = self.calculate_individual_price(self.max_price_wine, self.min_price_wine, self.wine)
        self.price_cloth = self.calculate_individual_price(self.max_price_cloth, self.min_price_cloth, self.cloth)

    def city_consumption(self):
        """
        Calculate City consumption.
        :return:
        """
        self.skins -= self.skins_consumption
        self.tools -= self.tools_consumption
        self.beer -= self.beer_consumption
        self.wine -= self.wine_consumption
        self.cloth -= self.cloth_consumption

    def city_production(self):
        # Add products, depending on city production.
        self.skins += self.skins_production
        self.tools += self.tools_production
        self.beer += self.beer_production
        self.wine += self.wine_production
        self.cloth += self.cloth_production

    def factories_production(self):
        self.skins += self.skins_factories * 3
        self.tools += self.tools_factories * 5
        self.beer += self.beer_factories * 10
        self.wine += self.wine_factories * 4
        self.cloth += self.cloth_factories * 4

    def create_factories(self, type, money):
        Functionalities.Utilities.how_many_can_afford(30000, money)
        quantity = input("How many factories do you want to create?\n")
        quantity = Functionalities.Utilities.correct_values(0, 10000, quantity)
        if not Functionalities.Utilities.check_if_affordable(30000, quantity, money):
            print("You cannot afford to build this number of factories.")
            return False
        else:
            print("Done, it will be ready in 5 turns.")
            total_cost = quantity * 30000
            return total_cost, type



    def create_factories_menu(self, money):
        print("Wich type of factory do you want to create?\n"
              "1- Skins.\n"
              "2- Tools.\n"
              "3- Beer.\n"
              "4- Wine.\n"
              "5- Cloth.\n"
              "6- Exit.\n")
        election = input()
        election = Functionalities.Utilities.correct_values(1, 6, election)
        if election == 6:
            pass
        else:
            self.check_if_can_build_factory(election, money)



    def check_if_can_build_factory(self, election, money):
        if election == 1:
            if self.can_produce_skins:
                self.create_factories(1, money)
            else:
                print("You can not build skins factories in {}".format(self.name))
        elif election == 2:
            if self.can_produce_tools:
                self.create_factories(2, money)
            else:
                print("You can not build tools factories in {}".format(self.name))
        elif election == 3:
            if self.can_produce_beer:
                self.create_factories(3, money)
            else:
                print("You can not build beer factories in {}".format(self.name))
        elif election == 4:
            if self.can_produce_wine:
                self.create_factories(4, money)
            else:
                print("You can not build wine factories in {}".format(self.name))
        elif election == 5:
            if self.can_produce_cloth:
                self.create_factories(5, money)
            else:
                print("You can not build cloth factories in {}".format(self.name))


    def avoid_minus_zero_items(self):
        """
        Doesn't let city consumption leave item quantity below zero.
        :return:
        """
        if self.skins < 0:
            self.skins = 0
        if self.tools < 0:
            self.tools = 0
        if self.beer < 0:
            self.beer = 0
        if self.wine < 0:
            self.wine = 0
        if self.cloth < 0:
            self.cloth = 0

    def change_turn(self):
        """
        Everything that have to happen everytime a turn passes.
        :return:
        """
        self.create_houses()
        self.get_taxes()
        self.city_consumption()
        self.city_production()
        self.factories_production()
        self.avoid_minus_zero_items()
        self.calculate_prices()





    def show_prices(self):
        print("""Current prices are:
        1- Cloth: {} coins, {} units.\n
        2- Beer: {} coins, {} units.\n
        3- Tools: {} coins, {} units.\n
        4- Skins: {} coins, {} units.\n
        5- Wine: {}, coins, {} units.\n
        """.format(self.price_cloth, self.cloth, self.price_beer, self.beer,
                   self.price_tools, self.tools, self.price_skins, self.skins, self.price_wine, self.wine))