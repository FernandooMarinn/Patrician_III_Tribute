import Functionalities.Utilities


class CommercialOffice:
    def __init__(self, city):
        self.city = city
        self.trader = False
        self.is_convoy = False
        self.warehouse = 0
        self.max_inventory_size = 500
        self.inventory_size = 0

        self.skins = 0
        self.price_skins = 0

        self.tools = 0
        self.price_tools = 0

        self.beer = 0
        self.price_beer = 0

        self.wine = 0
        self.price_wine = 0

        self.cloth = 0
        self.price_cloth = 0

        self.grain = 0
        self.price_grain = 0

        self.dagger = 0
        self.cannon = 0
        self.bombard = 0

    def set_max_inventory_size(self):
        self.inventory_size = 500 + self.warehouse * 2500

    def set_inventory_size(self):
        inventory = [self.skins, self.tools, self.beer, self.wine, self.cloth, self.grain * 10, self.dagger,
                     self.cannon * 5, self.bombard * 5]
        self.inventory_size = sum(inventory)

    def show_menu(self):
        while True:
            print("What do you want to do?\n"
                  "1- Buy from city.\n"
                  "2- Sell to city.\n"
                  "3- Check warehouse.\n"
                  "4- Trader menu.\n"
                  "5- Exit.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 5, option)
            if option == 5:
                break
            else:
                self.choosen_option(option)

    def choosen_option(self, option):
        if option == 1:
            Functionalities.Utilities.buy_from_city(self)
        elif option == 2:
            Functionalities.Utilities.sell_to_city(self)
        elif option == 3:
            self.check_warehouse()
        elif 4:
            self.trader_menu()

    def check_warehouse(self):
        """
        Prints out every important information in a commercial office.
        :return:
        """
        self.set_prices_to_zero_if_no_items()
        self.set_inventory_size()
        Functionalities.Utilities.text_separation()
        print("Your commercial office at {} have:\n"
              "{} skins at {} coins.\n"
              "{} tools at {} coins.\n"
              "{} beer at {} coins.\n"
              "{} wine at {} coins.\n"
              "{} cloth at {} coins.\n"
              "{} grain at {} coins.\n\n"
              "There are {} daggers, {} cannons and {} bombards.\n"
              .format(self.city.name, self.skins, self.price_skins, self.tools, self.price_tools, self.beer,
                      self.price_beer, self.wine, self.price_wine, self.cloth, self.price_cloth, self.grain,
                      self.price_grain, self.dagger, self.cannon, self.bombard))
        print("There are {} units of space occupied and {} warehouses. You can store another {} units before having "
              "to rent space in a warehouse."
              .format(self.inventory_size, self.warehouse, self.max_inventory_size - self.inventory_size))
        Functionalities.Utilities.text_separation()

    def set_prices_to_zero_if_no_items(self):
        """
        If the number of an item is equal to zero, it's price drop to zero as well.
        :return:
        """
        if self.skins == 0:
            self.price_skins = 0
        if self.tools == 0:
            self.price_tools = 0
        if self.beer == 0:
            self.price_beer = 0
        if self.wine == 0:
            self.price_wine = 0
        if self.cloth == 0:
            self.price_cloth = 0
        if self.grain == 0:
            self.price_grain = 0

    def total_bill(self):
        """
        Calculate total bill.
        :return:
        """
        self.set_inventory_size()
        if self.max_inventory_size < self.inventory_size:
            inventory_bill = self.max_inventory_size - self.inventory_size
        else:
            inventory_bill = 0
        return inventory_bill + self.warehouse * 20

    def pass_bill(self, bill):
        """
        Prints commercial office bill.
        :param bill:
        :return:
        """
        Functionalities.Utilities.text_separation()
        print("You have to pay {} for your commercial operations in {}."
              .format(bill, self.city.name))
        Functionalities.Utilities.text_separation()

    def trader_menu(self):
        """
        If there is not a trader, ask to hire one, else redirect to trader menu.
        :return:
        """
        if not self.trader:
            print("You don´t have a trader in {}.".format(self.city.name))
            self.hire_trader()
        else:
            self.trader.show_menu()

    def hire_trader(self):
        """
        Ask if want to hire a trader for a commercial office.
        :return:
        """
        print("Do you want to hire a trader? It will cost 20 coins each turn.\n"
              "1- Yes.\n"
              "2- No.\n")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if option == 1:
            self.city.player.coins -= 20
            Functionalities.Utilities.add_trader(self.city)
            self.trader.show_menu()
        else:
            pass

    def dismiss_trader(self):
        # To fire a trader.
        self.trader = False

    def change_turn(self):
        if not self.trader:
            pass
        else:
            self.trader.change_turn()


class Trader:
    def __init__(self, city, commercial_office):
        self.city = city
        self.commercial_office = commercial_office
        self.player = self.city.player
        self.level = 1
        self.experience = 0
        self.skins_instructions = [0, 0, 0, "skins"]
        self.tools_instructions = [0, 0, 0, "tools"]
        self.beer_instructions = [0, 0, 0, "beer"]
        self.cloth_instructions = [0, 0, 0, "cloth"]
        self.wine_instructions = [0, 0, 0, "wine"]
        self.grain_instructions = [0, 0, 0, "grain"]

        self.trading_instructions = [self.skins_instructions, self.tools_instructions, self.beer_instructions,
                                     self.wine_instructions, self.cloth_instructions, self.grain_instructions]

        self.speed = 3
        self.speed_counter = 1

    def gain_experience(self, exp):
        self.experience += exp
        self.level_up()

    def level_up(self):
        if self.level == 1:
            if self.experience >= 10_000:
                self.level += 1
                self.experience -= 10_000
                self.speed = 2
        elif self.level == 2:
            if self.experience >= 15_000:
                self.level += 1
                self.experience -= 15_000
                self.speed = 1

    def show_menu(self):
        while True:
            print("Want do you want to do?\n"
                  "1- Check trading options.\n"
                  "2- Change trading options.\n"
                  "3- Dismiss trader.\n"
                  "4- Exit.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 4, option)
            if option == 4:
                break
            elif option == 3:
                self.commercial_office.dismiss_trader()
                break
            else:
                self.choose_option(option)

    def choose_option(self, option):
        """
        Selects an option from trader menu.
        :param option:
        :return:
        """
        if option == 1:
            self.check_trading_options()
        elif option == 2:
            self.change_trading_options()

    def change_trading_options(self):
        """
        Menu for changing trading instructions given to a trader.
        :return:
        """
        item_list = ["skins", "tools", "beer", "wine", "cloth", "grain"]
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
        item_to_change = self.trading_instructions[option]
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
        Functionalities.Utilities.text_separation()
        for instruction in self.trading_instructions:
            if instruction[0] == 0:
                print("There are no instructions for {}.".format(instruction[3]))
            elif instruction[0] == "Sell":
                print("{} {} at {} coins.".format(instruction[0], instruction[3], instruction[2]))
            else:
                print("{} {} {} at {} coins.".format(instruction[0], instruction[1], instruction[3], instruction[2]))
        Functionalities.Utilities.text_separation()

    def trade(self):
        """
        When a turn passes, with the given instructions, calculates how many items sell/buy.
        :return:
        """
        self.city.calculate_prices()
        buy_list = []
        sell_list = []
        for instruction in self.trading_instructions:
            if instruction[0] == "Buy":
                buy_list.append(instruction)
            elif instruction[0] == "Sell":
                sell_list.append(instruction)
        if len(buy_list) != 0:
            self.buy_trade(buy_list)
        if len(sell_list) != 0:
            self.sell_trade(sell_list)

    def calculate_how_many_can_buy(self, item):
        """
        For a given instruction, calculate how many items can buy, until get to the given price.
        :param item:
        :return:
        """
        number_to_reach = item[1]
        price = item[2]
        name = item[3]
        product = Functionalities.Utilities.choose_products(name, self.commercial_office)

        if number_to_reach > product:
            prices_and_city_item = Functionalities.Utilities.return_trading_items_values(name, self.city)
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
        city_price = Functionalities.Utilities.choose_prices(name, self.city)
        number_of_products = Functionalities.Utilities.choose_products(name, self.commercial_office)
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
            Functionalities.Utilities.decrease_product_number(self.commercial_office, [1, name])
            Functionalities.Utilities.increase_product_number(self.city, [1, name])
            self.player.coins += city_price
            self.city.coins -= city_price
            self.city.calculate_prices()
            self.gain_experience(city_price)
            city_price = Functionalities.Utilities.choose_prices(name, self.city)
            number_of_products = Functionalities.Utilities.choose_products(name, self.commercial_office)

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
        mean_price = self.city.calculate_group_trade(min_price, max_price, city_product, -how_many_can_buy)
        self.city.coins += mean_price * how_many_can_buy
        self.city.player.coins -= mean_price * how_many_can_buy
        former_price = Functionalities.Utilities.choose_prices(name, self.commercial_office)
        new_price = Functionalities.Utilities.calculate_average_price(former_price, product,
                                                                      mean_price, how_many_can_buy)

        Functionalities.Utilities.change_prices(name, new_price, self.commercial_office)
        Functionalities.Utilities.decrease_product_number(self.city, [how_many_can_buy, name])
        Functionalities.Utilities.increase_product_number(self.commercial_office, [how_many_can_buy, name])
        self.gain_experience(mean_price * how_many_can_buy)

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
        mean_price = self.city.calculate_group_trade(min_price, max_price, city_product, -number_to_reach_goal)
        self.city.coins += mean_price * number_to_reach_goal
        self.city.player.coins -= mean_price * number_to_reach_goal
        former_price = Functionalities.Utilities.choose_prices(name, self.commercial_office)
        new_price = Functionalities.Utilities.calculate_average_price(former_price, product,
                                                                      mean_price, number_to_reach_goal)

        Functionalities.Utilities.change_prices(name, new_price, self.commercial_office)
        Functionalities.Utilities.decrease_product_number(self.city, [number_to_reach_goal, name])
        Functionalities.Utilities.increase_product_number(self.commercial_office, [number_to_reach_goal, name])
        self.gain_experience(mean_price * number_to_reach_goal)

    def buy_trade(self, buy_list):
        for item in buy_list:
            self.calculate_how_many_can_buy(item)

    def sell_trade(self, sell_list):
        for item in sell_list:
            self.calculate_how_many_can_sell(item)

    def calculate_trading_speed(self):
        """
        Depending on level, trader will trade each turn, or every x turns. This function calculate if next turn it will
        trade.
        :return:
        """
        if self.speed_counter == self.speed:
            self.trade()
            self.speed_counter = 1
        else:
            self.speed_counter += 1

    def change_turn(self):
        """
        Every time a turn changes.
        :return:
        """
        self.calculate_trading_speed()
        Functionalities.Utilities.set_price_to_zero(self.commercial_office)
