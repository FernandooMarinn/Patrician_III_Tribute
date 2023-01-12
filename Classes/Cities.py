import Classes.Comercial_Office
import Functionalities.Utilities


class City:
    def __init__(self, name, skins_consumption_ratio, tools_consumption_ratio, beer_consumption_ratio,
                 wine_consumption_ratio, cloth_consumption_ratio, initial_skins, initial_tools, initial_beer,
                 initial_wine, initial_cloth, skins_production, tools_production, beer_production, wine_production,
                 cloth_production, can_produce_skins, can_produce_tools, can_produce_beer, can_produce_wine,
                 can_produce_cloth, commercial_office, position, player):

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
        self.have_commercial_office = False
        self.money_lender = 0
        self.shipyard = 0
        self.tavern = 0
        self.weapon_master = 0
        self.possition = position

        self.boats = []
        self.convoys = []
        self.player = player
        self.tavern = 0

        self.construction_queue = []

    def create_houses(self):
        """
        Automatically create houses when needed.
        :return:
        """

        while self.population > (self.houses - 10) * 4:
            self.houses += 2
            self.coins -= 200

    def get_taxes(self):
        """
        Get taxes from every house.
        :return:
        """
        self.coins += 10 * self.houses

    def set_consumption(self):
        """
        Set the city consumption depending on population growth
        :return:
        """
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
        Calculates mean price depending on max and min values, number of products and number of item that are we buying.
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
        """
        Calculate every price that will be displayed in the menu everytime that we want to trade an item.

        It uses the same function to calculate every price, depending on max and min values, as well as item number.
        :return:
        """
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
        """
        Adds city production of every item.
        :return:
        """
        # Add products, depending on city production.
        self.skins += self.skins_production
        self.tools += self.tools_production
        self.beer += self.beer_production
        self.wine += self.wine_production
        self.cloth += self.cloth_production

    def factories_production(self):
        """
        Calculate factory production for each item.
        :return:
        """
        self.skins += self.skins_factories * 3
        self.tools += self.tools_factories * 5
        self.beer += self.beer_factories * 10
        self.wine += self.wine_factories * 4
        self.cloth += self.cloth_factories * 4

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
        self.set_consumption()
        self.city_consumption()
        self.city_production()
        self.factories_production()
        self.avoid_minus_zero_items()
        self.calculate_prices()
        self.tavern.change_turn()
        self.shipyard.change_turn()
        self.money_lender.change_turn()
        if not self.commercial_office:
            pass
        else:
            self.commercial_office.change_turn()

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
        self.calculate_prices()
        self.show_prices()
        option = input("What do you want to trade?\n")
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

    def how_many_buy(self, choosen_product, empty_space):
        """
        Like in Class boat, this one is the most unreadable function.

        It starts asking how many products you want to buy.

        Check if everything is fine, and then calculate average and total price.

        Finally, it returns the data to the Boat class.
        :param choosen_product:
        :param empty_space:
        :return:
        """
        # Ask how many we want to buy, if it is 0, finish the function.
        option = input("How many do you want to buy?\n")
        option = Functionalities.Utilities.correct_values(0, empty_space, option)
        if option == 0:
            return 0, choosen_product[3], 0

        # Check if enough items in city.
        if option < choosen_product[2]:
            # Calculate mean and total price.
            medium_price = self.calculate_group_trade(choosen_product[1], choosen_product[0], choosen_product[2],
                                                      -option)
            total_price = medium_price * option

            # Check if player has enough money. If it does, takes the money and return to boat all the info.
            if self.player.coins > total_price:
                Functionalities.Utilities.decrease_product_number(self, [option, choosen_product[3]])
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
        return 0, choosen_product[3], 0

    def how_many_sell(self, choosen_product, boat_products):
        """
        Same as above, but no need to check anything.

        :param choosen_product:
        :param boat_products:
        :return:
        """
        option = input("How many do you want to sell. You have {}\n".format(boat_products))
        option = Functionalities.Utilities.correct_values(0, boat_products, option)
        medium_price = self.calculate_group_trade(choosen_product[1], choosen_product[0], choosen_product[2],
                                                  option)
        total_price = medium_price * option
        Functionalities.Utilities.increase_product_number(self, choosen_product[3])
        self.coins -= total_price
        self.player.coins += total_price
        print("You have sold {} items at {} coins each.\n"
              .format(option, medium_price))
        return option, choosen_product[3], medium_price

    def menu_city_buildings(self):
        """
        Loop that prints city menu.
        :return:
        """
        while True:
            print("What do you want to do?\n\n"
                  "1- Go to your comercial office.\n"
                  "2- Go to money lender.\n"
                  "3- Go to shipyard.\n"
                  "4- Go to tavern.\n"
                  "5- Go to weapon master.\n"
                  "6- Build buildings.\n"
                  "7- Exit\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 7, option)
            if option == 7:
                break
            else:
                self.choose_city_building(option)

    def choose_city_building(self, option):
        """
        Depending on choosen option, uses it´s function.
        :param option:
        :return:
        """
        if option == 1:
            if not self.commercial_office:
                print("You dont have a commercial office in {}".format(self.name))
            else:
                self.commercial_office.show_menu()
        elif option == 2:
            self.money_lender.show_menu()
        elif option == 3:
            self.shipyard.show_menu()
        elif option == 4:
            print("To enter the tavern, you must state which ship is yours.")
            my_ship = Functionalities.Utilities.choose_boat_from_city(self)
            self.tavern.show_menu(my_ship)
        elif option == 5:
            self.weapon_master.show_menu()
        elif option == 6:
            self.menu_city_buildings()
            pass
        if option == 7:
            pass
        else:
            print("\n\n\n Not ready yet.\n\n\n")

    def menu_city_buildings(self):
        print("What do you want to do?\n"
              "1- Build warehouses.\n"
              "2- Build factories.\n"
              "3- Build commercial office.\n"
              "4- Check building queue."
              "5- Exit.\n")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 5, option)
        if option == 4:
            pass
        else:
            self.choose_city_buildings(option)

    def choose_city_buildings(self, option):
        if option == 1:
            self.build_warehouses()
        elif option == 2:
            self.factories_production()
        elif option == 3:
            self.build_commercial_office()

    def create_factories(self, type, money):
        """
        Creates factories for a city.
        :param type:
        :param money:
        :return:
        """
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
        """
        Print menu and take input.
        :param money:
        :return:
        """
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
        """
        Check if it is possible to build a certain factory in a city.
        :param election:
        :param money:
        :return:
        """
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

    def build_warehouses(self):
        if not self.commercial_office:
            print("You can´t build in this city if you dont have a commercial office in it.\n")
        else:
            print("You have {} warehouses in this city. Do you want to build more? (5000 coins each)\n"
                  "1- Yes.\n"
                  "2- No.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 2, option)
            if option == 1:
                how_much_can_buy = round(self.player.coins / 5000)
                how_much = input()
                how_much = Functionalities.Utilities.correct_values(0, how_much_can_buy, how_much)
                self.add_building_to_queue(how_much, 2, "warehouses")

    def build_commercial_office(self):
        if not self.commercial_office:
            self.player.check_if_can_build_office()
            if self.player.can_build_offices:
                print("Do you want to build a commercial office in {}? It will cost 50.000 coins.\n"
                      "1- Yes.\n"
                      "2- No.\n".format(self.name))
                option = input()
                option = Functionalities.Utilities.correct_values(1, 2, option)
                if option == 1:
                    if Functionalities.Utilities.check_if_affordable(50_000, 1, self.player.coins):
                        print("Perfect, it will be ready in 10 turns.\n")
                        self.add_building_to_queue(1, 10, "commercial_office")
                    else:
                        print("Unfortunately, you can´t afford to pay 50.000 coins.\n")
            else:
                print("You are not famous enough to build this office. Win some more money and try again.\n")
        else:
            print("You already have an office in {}!".format(self.name))

    def get_total_turns_queue(self):
        counter = 0
        for building in self.construction_queue:
            counter += building[0]
        return counter

    def add_building_to_queue(self, quantity, turns, type):
        for _ in range(quantity):
            total_turns = self.get_total_turns_queue()
            self.construction_queue.append([turns + total_turns, type])

    def decrease_turns_building_queue(self):
        if len(self.construction_queue) > 0:
            first_building = self.construction_queue[0]
            for building in self.construction_queue:
                building[0] -= 1
            if first_building[0] == 0:
                self.finish_building(first_building)

    def finish_building(self, building):
        building_type = building[1]
        if building_type == "warehouses":
            self.commercial_office.warehouses += 1
        elif building_type == "commercial_office":
            new_commercial_office = Classes.Comercial_Office.CommercialOffice(self)
            self.commercial_office = new_commercial_office
        else:
            current_building_number = getattr(self, building_type)
            setattr(self, building_type, current_building_number + 1)

        self.construction_queue.remove(building)
