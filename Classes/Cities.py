import Functionalities.Utilities


class City:
    def __init__(self, name, skins_consumption_ratio, tools_consumption_ratio, beer_consumption_ratio,
                 wine_consumption_ratio, cloth_consumption_ratio, initial_skins, initial_tools, initial_beer,
                 initial_wine, initial_cloth, skins_production, tools_production, beer_production, wine_production,
                 cloth_production, can_produce_skins, can_produce_tools, can_produce_beer, can_produce_wine,
                 can_produce_cloth, commercial_office, money_lender, shipyard, tavern, weapon_master, position, player):

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
        self.prestamist = money_lender
        self.shipyard = shipyard
        self.tavern = tavern
        self.weapon_master = weapon_master
        self.possition = position

        self.boats = []
        self.convoys = []
        self.player = player
        self.tavern = 0

    def create_houses(self):
        # Automatically create houses when needed.
        while self.population > (self.houses - 10) * 4:
            self.houses += 1
            self.coins -= 100

    def get_taxes(self):
        # Get taxes from every house.
        self.coins += 10 * self.houses

    def set_consumption(self):
        # Set the city consumption depending on population growth.
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

    def calculate_average_price(self, minimum_price, maximum_price, num_products, num_bought):
        """
        :param minimum_price:
        :param maximum_price:
        :param num_products:
        :param num_bought:
        :return:
        """
        if num_bought <= 0:
            return 0
        proportional_price = minimum_price + (maximum_price - minimum_price) * (100 - num_products) / 100
        if num_bought >= num_products:
            return round((num_products * proportional_price + (num_bought - num_products) * minimum_price) / num_bought)
        else:
            return round((num_bought * proportional_price) / num_bought)

    def prueba_grupos(self, min, max, num, bou):
        initial_price = self.calculate_individual_price(max, min, num)
        final_price = self.calculate_individual_price(max, min, num + bou)
        medium_price = (initial_price + final_price) / 2
        return medium_price

    def calculate_group_trade(self, minimum_price, maximum_price, items_number, traded_number):
        """
        Calculate average price for trading more than an item. If traded number is positive, we are selling, if it is
        positive, we are buying.
        :param minimum_price:
        :param maximum_price:
        :param items_number:
        :param traded_number:
        :return:
        """
        initial_price = self.calculate_individual_price(maximum_price, minimum_price, items_number)
        final_price = self.calculate_individual_price(maximum_price, minimum_price, items_number + traded_number)
        medium_price = (initial_price + final_price) / 2
        return round(medium_price)

    def calculate_prices(self):
        # Calculate every price, depending on available quantity.
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
        """
        Check prices of everything.
        :return:
        """
        print("-" * 60)
        self.calculate_prices()
        print("""\nCurrent prices are:
        1- Skins: {} coins, {} units.
        2- Tools: {} coins, {} units.
        3- Beer: {} coins, {} units.
        4- Wine: {} coins, {} units.
        5- Cloth: {}, coins, {} units.
        """.format(self.price_skins, self.skins, self.price_tools, self.tools,
                   self.price_beer, self.beer, self.price_wine, self.wine, self.price_cloth, self.cloth))
        print("-" * 60)

    def choose_product(self):
        """
        Return max and min values for each product.
        :return:
        """
        option = input("What do you want to buy?\n")
        option = Functionalities.Utilities.correct_values(1, 5, option)
        if option == 1:
            return [self.max_price_skins, self.min_price_skins, self.skins, "skins"]
        elif option == 2:
            return [self.max_price_tools, self.min_price_tools, self.tools, "tools"]
        elif option == 3:
            return [self.max_price_beer, self.min_price_beer, self.beer, "beer"]
        elif option == 4:
            return [self.max_price_wine, self.min_price_wine, self.wine, "wine"]
        elif option == 5:
            return [self.max_price_cloth, self.min_price_cloth, self.cloth, "cloth"]

    def how_many_buy(self, choosen_product):
        option = input("How many do you want to buy?\n")
        option = Functionalities.Utilities.correct_values(0, 99_999, option)
        if option < choosen_product[2]:
            medium_price = self.calculate_group_trade(choosen_product[1], choosen_product[0], choosen_product[2],
                                                      -option)
            total_price = medium_price * option
            if self.player.coins > total_price:
                self.decrease_product_number([option, choosen_product[3]])
                self.coins += total_price
                self.player.coins -= total_price
                print("You have bought {} items at {} coins each."
                      .format(option, medium_price))
                print("-" * 60)
                return option, choosen_product[3], medium_price
            else:
                print("You cannot afford to buy {} {}".format(option, choosen_product[3]))
        else:
            print("There are less than {} {} in {}".format(option, choosen_product[3], self.name))

    def how_many_sell(self, choosen_product):
        # Seguir con esto
        option = input("How many do you want to sell? You have {}.\n")
        option = Functionalities.Utilities.correct_values(0, choosen_product[2], option)
        medium_price = self.calculate_group_trade(choosen_product[1], choosen_product[0], choosen_product[2],
                                                  option)
        total_price = medium_price * option
        self.increase_product_number([option, choosen_product[3]])
        self.coins -= total_price
        self.player.coins += total_price
        print("You have sold {} items at {} coins each."
              .format(option, medium_price))
        return option, choosen_product[3], medium_price

    def decrease_product_number(self, products):
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

    def increase_product_number(self, products):
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

    def menu_city_buildings(self):
        print("What do you want to do?:\n"
              "1- Go to your comercial office.\n"
              "2- Go to prestamist.\n"
              "3- Go to shipyard.\n"
              "4- Go to tavern.\n"
              "5- Go to weapon master.\n"
              "6- Construct buildings.\n"
              "7- Exit\n")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 7, option)
        if option == 7:
            pass
        else:
            self.choose_city_building

    def choose_city_building(self, option):
        if option == 1:
            self.commercial_office.show_menu()
        elif option == 2:
            self.prestamist.show_menu()
        elif option == 3:
            self.shipyard.show_menu()
        elif option == 4:
            self.tavern.show_menu()
        elif option == 5:
            self.weapon_master.show_menu()
        elif option == 6:
            self.menu_city_buildings()
