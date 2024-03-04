from copy import deepcopy
import Functionalities.Utilities


class Captain:

    def __init__(self, boat):
        self.boat = boat
        self.player = boat.player

        self.current_city = None

        self.skins_instructions = [0, 0, 0, "skins"]
        self.tools_instructions = [0, 0, 0, "tools"]
        self.beer_instructions = [0, 0, 0, "beer"]
        self.cloth_instructions = [0, 0, 0, "cloth"]
        self.wine_instructions = [0, 0, 0, "wine"]
        self.grain_instructions = [0, 0, 0, "grain"]

        self.trading_instructions = [self.skins_instructions, self.tools_instructions, self.beer_instructions,
                                     self.wine_instructions, self.cloth_instructions, self.grain_instructions]

        self.route = {}

        self.in_route = False
        self.step_of_route = 1

        self.travel = False

    def show_menu(self):
        while True:
            print("Want do you want to do?\n"
                  "1- Check route.\n"
                  "2- Modify route.\n"
                  "3- Change trading options.\n"
                  "4- Check trading options for a city.\n"
                  "5- {}.\n"
                  "6- Dismiss captain.\n"
                  "7- Exit.\n".format(self.start_stop_route_message()))
            option = input()
            option = Functionalities.Utilities.correct_values(1, 7, option)
            if option == 7:
                break
            elif option == 6:
                self.boat.fire_captain()
                break
            else:
                self.choose_option(option)

    def get_all_route_cities(self):
        return [self.route[city]["name"] for city in self.route.keys()]

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
        elif option == 4:
            self.check_trading_options()
        elif option == 5:
            self.start_stop_route()

    def check_route(self):
        all_cities = self.get_all_route_cities()

        if len(all_cities) == 0:
            print("\nYour route is still empty\n")
            return False
        else:
            for num, city in enumerate(all_cities):
                print("{}.- {}.".format(num + 1, city))
            print("\n\n")
            return True

    def modify_route(self):
        while True:
            print("What do you want to do?\n"
                  "1- Add city to route.\n"
                  "2- Delete city from route.\n"
                  "3- Exit.")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 3, option)

            if option == 3:
                break
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
                for num, city in enumerate(cities):
                    print("{}- {}.".format(num + 1, city.name))

                option = input("\n")
                option = Functionalities.Utilities.correct_values(1, len(cities), option)
                self.add_new_city_to_route(cities[option - 1])

    def adjust_route(self):
        keys = sorted(self.route.keys())
        new_route = {}
        for i in range(len(self.route)):
            new_route[i + 1] = self.route[keys[i]]

        self.route = new_route

    def add_new_city_to_route(self, city):
        if self.route == {}:
            new_number = 1
        else:
            new_number = max(self.route.keys()) + 1

        self.route[new_number] = {"city": city,
                                  "name": city.name,
                                  "instructions": deepcopy(self.trading_instructions)}

    def modify_city(self):
        all_cities = self.get_all_route_cities()
        for num, city in enumerate(all_cities):
            print("{}.- {}.\n".format(num + 1, city))

        print("Witch city do you want do modify?")
        option = input()
        option = Functionalities.Utilities.correct_values(1, len(all_cities), option)

        self.current_city = option
        self.change_trading_options()

    def change_trading_options(self):
        """
        Menu for changing trading instructions given to a trader.
        :return:
        """
        item_list = ("skins", "tools", "beer", "wine", "cloth", "grain")
        print("What do you want to change?\n\n")
        for i, x in enumerate(item_list):
            print(f"{i + 1}- {x}")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 6, option)
        self.change_trading_options_individually(option - 1)

    def change_trading_options_individually(self, option):
        """
        Sets an individual instruction for buy/sell a certain product, and ask its price as well.
        :param option:
        :return:
        """
        item_to_change = self.route[self.current_city]["instructions"][option]
        print("Do you want to buy or sell {}?\n"
              "1- Buy.\n"
              "2- Sell.\n"
              "3- Reset instruction.\n"
              .format(item_to_change[3]))
        option = input()
        option = Functionalities.Utilities.correct_values(1, 3, option)
        if option == 1:
            item_to_change[0] = "Buy"
            print("How many items do you want to buy?\n")
            how_many = input()
            how_many = Functionalities.Utilities.correct_values(0, 99999, how_many)
            item_to_change[1] = how_many

        elif option == 2:
            item_to_change[0] = "Sell"

        elif option == 3:
            item_to_change[0] = 0
            return True

        how_much = input("What price do you want to set?\n")
        how_much = Functionalities.Utilities.correct_values(0, 99999, how_much)
        item_to_change[2] = how_much

    def check_trading_options(self):
        """
        Prints out current trading options.
        :return:
        """
        all_cities = self.get_all_route_cities()
        if len(all_cities) > 0:
            for num, city in enumerate(all_cities):
                print("{}.- {}.\n".format(num + 1, city))

            print("Witch city do you want do want to check?")
            option = input()
            option = Functionalities.Utilities.correct_values(1, len(all_cities), option)

            Functionalities.Utilities.text_separation()
            instructions = self.route[option]['instructions']
            for instruction in instructions:
                if instruction[0] == 0:
                    print("There are no instructions for {}.".format(instruction[3]))
                elif instruction[0] == "Sell":
                    print("{} {} at {} coins.".format(instruction[0], instruction[3], instruction[2]))
                else:
                    print("{} {} {} at {} coins.".format(instruction[0], instruction[1], instruction[3], instruction[2]))
            Functionalities.Utilities.text_separation()
        else:
            print("You don't have any city in your route.")

    def start_stop_route_message(self):
        if self.in_route:
            return "Stop automatic route"
        else:
            return "Start automatic route"

    def start_stop_route(self):
        if self.in_route:
            self.in_route = False
        else:
            self.in_route = True

    def automatic_route(self):
        if self.in_route and not self.boat.traveling:
            if self.travel:
                self.travel = False
            else:
                self.trade()
                self.step_of_route += 1
                if self.step_of_route > len(self.route):
                    self.step_of_route = 1
                Functionalities.Utilities.check_distance_between_cities(self.boat, None,
                                                                        possition=self.route[self.step_of_route]['city'].possition,
                                                                        city=self.route[self.step_of_route]['city'])
                self.travel = True

    def trade(self):
        buy_list = []
        sell_list = []
        for instruction in self.route[self.step_of_route]['instructions']:
            if instruction[0] == "Buy":
                buy_list.append(instruction)
            elif instruction[0] == "Sell":
                sell_list.append(instruction)
        if len(buy_list) != 0:
            self.buy_trade(buy_list)
        if len(sell_list) != 0:
            self.sell_trade(sell_list)

    def buy_trade(self, buy_list):
        for item in buy_list:
            self.calculate_how_many_can_buy(item)

    def sell_trade(self, sell_list):
        for item in sell_list:
            self.calculate_how_many_can_sell(item)

    def calculate_how_many_can_buy(self, item):
        """
        For a given instruction, calculate how many items can buy, until get to the given price.
        :param item:
        :return:
        """
        number_to_reach = item[1]
        price = item[2]
        name = item[3]
        product = Functionalities.Utilities.choose_products(name, self.boat)

        if number_to_reach > product:
            prices_and_city_item = Functionalities.Utilities.return_trading_items_values(name, self.boat.city)
            max_price = prices_and_city_item[0]
            min_price = prices_and_city_item[1]
            city_product = prices_and_city_item[2]
            number_to_reach_goal = number_to_reach - product
            how_many_can_buy = Functionalities.Utilities.calculate_how_many_can_buy_trader(price, min_price, max_price,
                                                                                           city_product)
            if how_many_can_buy < number_to_reach_goal:
                self.trade_can_not_buy_all(min_price, max_price, city_product, how_many_can_buy, name, product)
            else:
                self.trade_can_buy_all(min_price, max_price, city_product, number_to_reach_goal, name, product)

    def calculate_how_many_can_sell(self, item):
        """
        For a given instruction, calculate how many items can sell, until get to the given price.
        :param item:
        :return:
        """
        name = item[3]
        price_to_sell = item[2]
        city_price = Functionalities.Utilities.choose_prices(name, self.boat.city)
        number_of_products = Functionalities.Utilities.choose_products(name, self.boat)
        self.sell_one_by_one(name, price_to_sell, city_price, number_of_products)

    def sell_one_by_one(self, name, price_to_sell, city_price, number_of_products):
        """
        Function to sell one by one, in order to change prices gradually until reaching the given price to the trader.
        It also distributes money form city to player, and gain experience for the trader.
        :param name:
        :param price_to_sell:
        :param city_price:
        :param number_of_products:
        :return:
        """
        while price_to_sell < city_price and number_of_products > 0:
            Functionalities.Utilities.decrease_product_number(self.boat, [1, name])
            Functionalities.Utilities.increase_product_number(self.boat.city, [1, name])
            self.player.coins += city_price
            self.boat.city.coins -= city_price
            self.boat.city.calculate_prices()

            city_price = Functionalities.Utilities.choose_prices(name, self.boat.city)
            number_of_products = Functionalities.Utilities.choose_products(name, self.boat)

    def trade_can_not_buy_all(self, min_price, max_price, city_product, how_many_can_buy, name, product):
        """
        This function works when trader can not buy all the items that he wants to reach an instruction.
        :param min_price:
        :param max_price:
        :param city_product:
        :param how_many_can_buy:
        :param name:
        :param product:
        :return:
        """
        mean_price = self.boat.city.calculate_group_trade(min_price, max_price, city_product, -how_many_can_buy)
        self.boat.city.coins += mean_price * how_many_can_buy
        self.boat.player.coins -= mean_price * how_many_can_buy
        former_price = Functionalities.Utilities.choose_prices(name, self.boat)
        new_price = Functionalities.Utilities.calculate_average_price(former_price, product,
                                                                      mean_price, how_many_can_buy)

        Functionalities.Utilities.change_prices(name, new_price, self.boat)
        Functionalities.Utilities.decrease_product_number(self.boat.city, [how_many_can_buy, name])
        Functionalities.Utilities.increase_product_number(self.boat, [how_many_can_buy, name])

    def trade_can_buy_all(self, min_price, max_price, city_product, number_to_reach_goal, name, product):
        """
        This function works when trader can buy all the items that he needs to fulfill a certain instruction. Player
        has the money to continue buying items, so, in order to limit the number of items, we give as an argument the
        number to reach the instruction.
        :param min_price:
        :param max_price:
        :param city_product:
        :param number_to_reach_goal:
        :param name:
        :param product:
        :return:
        """
        mean_price = self.boat.city.calculate_group_trade(min_price, max_price, city_product, -number_to_reach_goal)
        self.boat.city.coins += mean_price * number_to_reach_goal
        self.player.coins -= mean_price * number_to_reach_goal
        former_price = Functionalities.Utilities.choose_prices(name, self.boat)
        new_price = Functionalities.Utilities.calculate_average_price(former_price, product,
                                                                      mean_price, number_to_reach_goal)

        Functionalities.Utilities.change_prices(name, new_price, self.boat)
        Functionalities.Utilities.decrease_product_number(self.boat.city, [number_to_reach_goal, name])
        Functionalities.Utilities.increase_product_number(self.boat, [number_to_reach_goal, name])
