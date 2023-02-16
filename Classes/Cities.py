import random

import Classes.Comercial_Office
import Functionalities.Utilities


class City:
    def __init__(self, name, skins_consumption_ratio, tools_consumption_ratio, beer_consumption_ratio,
                 wine_consumption_ratio, cloth_consumption_ratio, grain_consumption_ratio, initial_skins,
                 initial_tools, initial_beer, initial_wine, initial_cloth, initial_grain, skins_production,
                 tools_production, beer_production, wine_production, cloth_production, grain_production,
                 can_produce_skins, can_produce_tools, can_produce_beer, can_produce_wine, can_produce_cloth,
                 can_produce_grain, commercial_office, position, player):

        self.coins = 100_000
        # Products quantity.
        self.skins = initial_skins
        self.tools = initial_tools
        self.beer = initial_beer
        self.wine = initial_wine
        self.cloth = initial_cloth
        self.grain = initial_grain
        self.name = name

        # City consuption of each item.
        self.skins_consumption_ratio = skins_consumption_ratio
        self.tools_consumption_ratio = tools_consumption_ratio
        self.beer_consumption_ratio = beer_consumption_ratio
        self.wine_consumption_ratio = wine_consumption_ratio
        self.cloth_consumption_ratio = cloth_consumption_ratio
        self.grain_consumption_ratio = grain_consumption_ratio

        self.skins_consumption = 0
        self.tools_consumption = 0
        self.beer_consumption = 0
        self.wine_consumption = 0
        self.cloth_consumption = 0
        self.grain_consumption = 0

        # City base production of each item.
        self.skins_production = skins_production
        self.tools_production = tools_production
        self.beer_production = beer_production
        self.wine_production = wine_production
        self.cloth_production = cloth_production
        self.grain_production = grain_production

        # Factories in the city
        self.skins_factories = 0
        self.tools_factories = 0
        self.beer_factories = 0
        self.wine_factories = 0
        self.cloth_factories = 0
        self.grain_factories = 0

        # Is it possible to create factories
        self.can_produce_skins = can_produce_skins
        self.can_produce_tools = can_produce_tools
        self.can_produce_beer = can_produce_beer
        self.can_produce_wine = can_produce_wine
        self.can_produce_cloth = can_produce_cloth
        self.can_produce_grain = can_produce_grain

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
        self.max_price_grain = 220
        self.min_price_grain = 80

        # Current values.
        self.price_skins = 0
        self.price_tools = 0
        self.price_beer = 0
        self.price_wine = 0
        self.price_cloth = 0
        self.price_grain = 0
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
        self.grain_consumption = round((self.population * self.grain_consumption_ratio) / 1000)

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
        self.price_grain = self.calculate_individual_price(self.max_price_grain, self.min_price_grain, self.grain)

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
        self.grain -= self.grain_consumption

    def city_production(self):
        """
        Adds city production of every item.
        :return:
        """
        self.skins += self.skins_production
        self.tools += self.tools_production
        self.beer += self.beer_production
        self.wine += self.wine_production
        self.cloth += self.cloth_production
        self.grain += self.grain_production

    def factories_production(self):
        """
        Calculate factory production for each item.
        :return:
        """
        if not self.commercial_office:
            pass
        else:
            self.commercial_office.skins += self.skins_factories * 2
            self.commercial_office.tools += self.tools_factories * 4
            self.commercial_office.beer += self.beer_factories * 5
            self.commercial_office.wine += self.wine_factories * 3
            self.commercial_office.cloth += self.cloth_factories * 3
            self.commercial_office.grain += self.grain_factories * 3

            self.add_factories_prices()

    def add_factories_prices(self):
        """
        Update prices when there is a factory production. Every factory produces items at minimum cost.
        :return:
        """
        office = self.commercial_office
        office_list = [
            [office.price_skins, office.skins, self.min_price_skins, self.skins_factories * 2, "skins"],
            [office.price_tools, office.tools, self.min_price_tools, self.tools_factories * 4, "tools"],
            [office.price_beer, office.beer, self.min_price_beer, self.beer_factories * 5, "beer"],
            [office.price_wine, office.wine, self.min_price_wine, self.wine_factories * 3, "wine"],
            [office.price_cloth, office.cloth, self.min_price_cloth, self.cloth_factories * 3, "cloth"],
            [office.price_grain, office.grain, self.min_price_grain, self.grain_factories * 3, "grain"]
        ]
        for factory in office_list:
            price = Functionalities.Utilities.calculate_average_price(factory[0], factory[1], factory[2], factory[3])
            Functionalities.Utilities.change_prices(factory[4], price, self.commercial_office)

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
        if self.grain < 0:
            self.grain = 0

    def population_growth(self):
        # Let population grow if there is beer and grain in the city.
        if self.beer >= 20 and self.grain >= 20:
            self.population += round(self.population / 15)
        # It can also decrease the pupulation.
        elif self.beer == 0 and self.grain == 0 and self.population >= 1000:
            self.population -= round(self.population / 15)


    def random_items_fill(self):
        """
        This function works as a random trader that arrives in a city. It will sell a certain number of items, of a
        certain number of different products, all based in probability and random numbers.
        :return:
        """
        all_products = ["skins", "tools", "beer", "wine", "cloth", "grain"]
        probability = random.randint(0, 12)
        number_of_items_to_fill = random.randint(0, 6)
        number_of_products_to_add = [random.randint(0, 40) for _ in range(number_of_items_to_fill)]
        if probability == 5:
            for i in range(number_of_items_to_fill):
                product_to_fill = random.choice(all_products)
                current_number = getattr(self, product_to_fill)
                setattr(self, product_to_fill, current_number + number_of_products_to_add[i])
                all_products.remove(product_to_fill)


    def show_prices(self):
        """
        Check prices of everything.
        :return:
        """
        Functionalities.Utilities.text_separation()
        self.calculate_prices()
        print("""\nCurrent prices are:
        1- Skins: {} coins, {} units.
        2- Tools: {} coins, {} units.
        3- Beer: {} coins, {} units.
        4- Wine: {} coins, {} units.
        5- Cloth: {} coins, {} units.
        6- Grain: {} coins, {} units.
        """.format(self.price_skins, self.skins, self.price_tools, self.tools,
                   self.price_beer, self.beer, self.price_wine, self.wine, self.price_cloth, self.cloth,
                   self.price_grain, self.grain))
        Functionalities.Utilities.text_separation()

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
                Functionalities.Utilities.text_separation()
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
        option = input("How many do you want to sell. You have {} units at {} coins.\n"
                       .format(boat_products[0], boat_products[1]))
        option = Functionalities.Utilities.correct_values(0, boat_products[0], option)
        medium_price = self.calculate_group_trade(choosen_product[1], choosen_product[0], choosen_product[2],
                                                  option)
        total_price = medium_price * option
        Functionalities.Utilities.increase_product_number(self, choosen_product[3])
        self.coins -= total_price
        self.player.coins += total_price
        print("You have sold {} items at {} coins each.\n"
              .format(option, medium_price))
        return option, choosen_product[3], medium_price

    def choose_product(self):
        """
        Return max and min values for each product.
        :return:
        """
        self.calculate_prices()
        self.show_prices()
        option = input("What do you want to trade?\n")
        option = Functionalities.Utilities.correct_values(1, 6, option)
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
        elif option == 6:
            return [self.max_price_grain, self.min_price_grain, self.grain, "grain"]


    def menu_city_buildings(self):
        """
        Loop that prints city menu.
        :return:
        """
        while True:
            print("What do you want to do?\n\n"
                  "1- Go to your commercial office.\n"
                  "2- Go to money lender.\n"
                  "3- Go to shipyard.\n"
                  "4- Go to tavern.\n"
                  "5- Go to weapon master.\n"
                  "6- Construct buildings.\n"
                  "7- Check factory production.\n"
                  "8- Go to city hall.\n"
                  "9- Exit.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 9, option)
            if option == 9:
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
            if not my_ship:
                print("You don't have any ships in {}!".format(self.name))
            else:
                self.tavern.show_menu(my_ship)
        elif option == 5:
            self.weapon_master.show_menu()
        elif option == 6:
            self.menu_construct_buildings()
        elif option == 7:
            self.check_factory_production()
        elif option == 8:
            self.city_hall()

    def menu_construct_buildings(self):
        """
        Prints construction menu.
        :return:
        """
        while True:
            print("What do you want to do?\n"
                  "1- Build warehouses.\n"
                  "2- Build factories.\n"
                  "3- Build commercial office.\n"
                  "4- Check building queue.\n"
                  "5- Exit.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 5, option)
            if option == 5:
                break
            else:
                self.choose_city_buildings(option)

    def choose_city_buildings(self, option):
        """
        Selects choosen option from construction menu.
        :param option:
        :return:
        """
        if option == 1:
            self.build_warehouses()
        elif option == 2:
            self.create_factories_menu()
        elif option == 3:
            self.build_commercial_office()
        elif option == 4:
            self.check_building_queue()


    def create_factories_menu(self):
        """
        Print menu and take input.
        :return:
        """
        print("Wich type of factory do you want to create?\n"
              "1- Skins.\n"
              "2- Tools.\n"
              "3- Beer.\n"
              "4- Wine.\n"
              "5- Cloth.\n"
              "6- Grain.\n"
              "7- Exit.\n")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 7, option)
        if option == 7:
            pass
        else:
            self.check_if_can_build_factory(option)

    def check_if_can_build_factory(self, election):
        """
        Check if it is possible to build a certain factory in a city.
        :param election:
        :return:
        """
        can_build_correspondencies = {
            1: self.can_produce_skins,
            2: self.can_produce_tools,
            3: self.can_produce_beer,
            4: self.can_produce_wine,
            5: self.can_produce_cloth,
            6: self.can_produce_grain
        }
        factories_type = {
            1: "skins_factories",
            2: "tools_factories",
            3: "beer_factories",
            4: "wine_factories",
            5: "cloth_factories",
            6: "grain_factories"
        }
        names = {
            1: "skins",
            2: "tools",
            3: "beer",
            4: "wine",
            5: "cloth",
            6: "grain"
        }

        if can_build_correspondencies[election]:
            self.create_factories(factories_type[election], names[election])
        else:
            print("You cannot produce {} in {}.\n".format(names[election], self.name))

    def create_factories(self, type, name):
        """
        Ask if want to create a factory, and adding it to the queue.
        :param type:
        :param name:
        :return:
        """
        can_afford = Functionalities.Utilities.how_many_can_afford(25000, self.player.coins)
        how_many = input("How many {} factories do you want to create? Each one cost 25.000 coins.\n"
                         "You can afford {}.\n".format(name, can_afford))
        how_many = Functionalities.Utilities.correct_values(0, can_afford, how_many)
        if how_many > 0:
            print("It will take 5 turns to build a factory.\n")
            self.add_building_to_queue(how_many, 5, type, 25_000)
            self.player.achievements.build_factories(how_many)

    def build_warehouses(self):
        """
        Ask if want to create a warehouse, and adding it to the queue.
        :return:
        """
        Functionalities.Utilities.text_separation()
        if not self.commercial_office:
            print("You can´t build in this city if you dont have a commercial office in it.\n")
        else:
            print("You have {} warehouses in this city. Do you want to build more? (5000 coins each)\n"
                  "1- Yes.\n"
                  "2- No.\n".format(self.commercial_office.warehouse))
            option = input()
            option = Functionalities.Utilities.correct_values(1, 2, option)
            if option == 1:
                how_much_can_afford = round(self.player.coins / 5000)
                how_much = input("How many do you want to build? You can afford {}\n".format(how_much_can_afford))
                how_much = Functionalities.Utilities.correct_values(0, how_much_can_afford, how_much)
                self.add_building_to_queue(how_much, 2, "warehouse", 5000)
        Functionalities.Utilities.text_separation()

    def build_commercial_office(self):
        """
        Function to create a commercial office, checking if player is famous enough.
        :return:
        """
        Functionalities.Utilities.text_separation()
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
                        self.add_building_to_queue(1, 10, "commercial_office", 50_000)
                        self.player.achievements.calculate_commercial_offices()

                    else:
                        print("Unfortunately, you can´t afford to pay 50.000 coins.\n")

            else:
                print("You are not famous enough to build this office. Win some more money and try again.\n")

        else:
            print("You already have an office in {}!".format(self.name))
        Functionalities.Utilities.text_separation()

    def get_total_turns_queue(self):
        """
        Calculate total of turns in the building queue.
        :return:
        """
        counter = 0
        for building in self.construction_queue:
            if building[0] > counter:
                counter = building[0]
        return counter

    def add_building_to_queue(self, quantity, turns, type, cost):
        """
        Adding building to the queue.
        :param quantity:
        :param turns:
        :param type:
        :return:
        """
        for _ in range(quantity):
            total_turns = self.get_total_turns_queue()
            self.construction_queue.append([turns + total_turns, type])
        self.player.coins -= cost

    def decrease_turns_building_queue(self):
        """
        Decrease turns, and if they are finished, sending building to be finished.
        :return:
        """
        if len(self.construction_queue) > 0:
            first_building = self.construction_queue[0]
            for building in self.construction_queue:
                building[0] -= 1
            if first_building[0] == 0:
                self.finish_building(first_building)

    def finish_building(self, building):
        """
        Last step for building construction. Adding them to the city and deleting them from the queue.
        :param building:
        :return:
        """
        Functionalities.Utilities.text_separation()
        building_type = building[1]
        if building_type == "warehouse":
            self.commercial_office.warehouse += 1

        elif building_type == "commercial_office":
            new_commercial_office = Classes.Comercial_Office.CommercialOffice(self)
            self.commercial_office = new_commercial_office

        else:
            factory_name = Functionalities.Utilities.return_factory_name(building_type)
            if not factory_name:
                print("A new {} is ready in {}!".format(building_type, self.name))
            else:
                print("A new {} is ready in {}!".format(factory_name, self.name))
            current_building_number = getattr(self, building_type)
            setattr(self, building_type, current_building_number + 1)

        self.construction_queue.remove(building)
        Functionalities.Utilities.text_separation()

    def check_building_queue(self):
        """
        Print every building in queue.
        :return:
        """
        counter = 1
        Functionalities.Utilities.text_separation()
        if len(self.construction_queue) == 0:
            print("There are no works at the moment.")
        else:
            for building in self.construction_queue:
                factory_name = Functionalities.Utilities.return_factory_name(building[1])
                if not factory_name:
                    print("{}-{}, will be ready in {} turns.".format(counter, building[1], building[0]))
                    counter += 1
                else:
                    print("{}-{}, will be ready in {} turns.".format(counter, factory_name, building[0]))
                    counter += 1
        Functionalities.Utilities.text_separation()

    def check_factory_production(self):
        """
        Check factory production for a city.
        :return:
        """
        Functionalities.Utilities.text_separation()
        all_factories = [self.skins_factories, self.tools_factories, self.beer_factories, self.wine_factories,
                         self.wine_factories]
        products_production = (
            ("skins", 2),
            ("tools", 4),
            ("beer", 5),
            ("wine", 3),
            ("cloth", 3),
            ("grain", 3)
        )
        print("In {} you have:\n".format(self.name))
        for i, x in enumerate(all_factories):
            print("{} factories that are producing {} {} per turn."
                  .format(x, products_production[i][1] * x, products_production[i][0]))
        Functionalities.Utilities.text_separation()

    def control_overproduction(self):
        items = (self.skins, self.tools, self.beer, self.wine, self.cloth, self.grain)
        for item in items:
            random_number = random.randint(20, 50)
            if item > 200:
                item -= random_number

    def city_hall(self):
        self.set_consumption()
        if not self.commercial_office:
            office = "You dont have a commercial office in the city."
        else:
            office = "You have a commercial office in this town."
        Functionalities.Utilities.text_separation()


        print(f"""This is the city hall of the great city of {self.name}.
        
There are {self.population} people living in this city. Current consumption for turn is:
        
- {self.skins_consumption} units of skins.
- {self.tools_consumption} units of tools.
- {self.beer_consumption} units of beer.
- {self.wine_consumption} units of wine.
- {self.cloth_consumption} units of cloth.
- {self.grain_consumption} units of grain.

- Money lender is level {self.money_lender.level}. Shipyard is level {self.shipyard.level}. Weapon master is level {self.weapon_master.level}.
- There are {self.tavern.sailors} sailors in the tavern.
- {office}
""")
        Functionalities.Utilities.text_separation()

    def change_turn(self):
        """
        Everything that have to happen everytime a turn passes.
        :return:
        """
        self.create_houses()
        self.get_taxes()
        self.random_items_fill()
        self.set_consumption()
        self.city_consumption()
        self.city_production()
        self.factories_production()
        self.avoid_minus_zero_items()
        self.calculate_prices()
        self.tavern.change_turn()
        self.shipyard.change_turn()
        self.money_lender.change_turn()
        self.weapon_master.change_turn()
        if self.commercial_office:
            self.commercial_office.change_turn()
        self.decrease_turns_building_queue()
        self.population_growth()
        self.control_overproduction()
