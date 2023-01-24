import Classes.Tavern
import Classes.Weapon_Master
import Classes.Shipyard
import Classes.Player
import Classes.Money_Lender
import Classes.Cities
import Classes.Comercial_Office
import Functionalities.Combat
import random


# For check every value, in order to avoid errors.

def correct_values_number(start, final, number_to_check):
    try:
        if start <= int(number_to_check) <= final:
            return number_to_check
        else:
            while not start <= number_to_check <= final:
                print("You have written an incorrect value, your options goes from {} to {}".format(start, final))
                number_to_check = int(input())
            return number_to_check
    except ValueError:
        return False
    except TypeError:
        return False


def correct_values(start, final, number_to_check):
    """
        Avoid Value and Type errors, as well as out of range errors.
        :param start:
        :param final:
        :param number_to_check:
        :return:
        """
    is_a_number = correct_values_number(start, final, number_to_check)
    if is_a_number is False:
        print("You have to write a number\n")
        while is_a_number is False:
            number_to_check = input("Introduce a value from {} to {}.\n".format(start, final))
            is_a_number = correct_values_number(start, final, number_to_check)
        return int(is_a_number)
    else:
        return int(is_a_number)


def check_if_affordable(price, quantity, money):
    if price * quantity <= money:
        return True
    else:
        return False


def how_many_can_afford(price, money):
    if price == 0:
        return 0
    else:
        can_afford_number = round(money / price)
        return can_afford_number


def ask_initial_money():
    print("How much money do you wnat to start with?\n"
          "1- 5000 (very few).\n"
          "2- 10000 (few).\n"
          "3- 20000 (normal).\n"
          "4- 50000 (too much).\n")
    option = input("\n")
    option = correct_values(1, 4, option)
    money = {1: 5000, 2: 10_000, 3: 20_000, 4: 50_000}
    return money[option]


def ask_initial_city(cities):
    for i in range(len(cities)):
        print("{}- {}.".format(i + 1, cities[i].name))
    option = input("Wich city do you choose as your birthplace?\n\n")
    option = correct_values(1, len(cities), option)
    add_commercial_office(cities[option - 1])
    return cities[option - 1]


def create_player():
    """
    returns object player
    :return:
    """
    name = input("What is your name?\n")
    coins = ask_initial_money()
    player = Classes.Player.Player(name, coins)
    return player


def create_cities(player):
    # Puta mierda
    #  nombre   consumption    initial            production       can_pruduce
    lubeck = Classes.Cities.City("Lubeck", 3, 4, 6, 3, 3, 40, 60, 40, 50, 30, 0, 15, 0, 9, 0, False, True, False, True,
                                 False, False, 1, player)
    rostock = Classes.Cities.City("Rostock", 3, 4, 6, 3, 3, 40, 40, 40, 50, 30, 0, 0, 0, 0, 0, False, False, False,
                                  False,
                                  False, False, 1, player)
    malmo = Classes.Cities.City("Malmo", 3, 4, 6, 3, 3, 60, 60, 30, 30, 50, 8, 0, 0, 0, 7, True, False, False, False,
                                True, False, 1, player)
    stettin = Classes.Cities.City("Stettin", 3, 4, 6, 3, 3, 40, 50, 70, 50, 30, 0, 0, 15, 0, 0, False, False, True,
                                  True,
                                  False, False, 1, player)
    gdanks = Classes.Cities.City("Gdanks", 3, 4, 4, 3, 3, 30, 40, 60, 40, 40, 0, 0, 10, 0, 0, False, False, True, False,
                                 False, False, 1, player)

    return lubeck, rostock, malmo, stettin, gdanks


def add_all_buildings(cities):
    cities = create_taverns(cities)
    cities = create_shipyards(cities)
    cities = create_weapon_masters(cities)
    cities = create_money_lender(cities)
    return cities


def return_taverns(cities):
    all_taverns = []
    for city in cities:
        all_taverns.append(city.tavern)
    return all_taverns


def create_taverns(cities):
    cities_with_tavern = []
    for city in cities:
        tavern = Classes.Tavern.Tavern(city)
        city.tavern = tavern
        cities_with_tavern.append(city)
    return cities_with_tavern


def create_shipyards(cities):
    cities_with_shipyard = []
    for city in cities:
        shipyard = Classes.Shipyard.Shipyard(city)
        city.shipyard = shipyard
        cities_with_shipyard.append(city)
    return cities_with_shipyard


def create_weapon_masters(cities):
    cities_with_weapon_master = []
    for city in cities:
        weapon_master = Classes.Weapon_Master.Weapon_master(city)
        city.weapon_master = weapon_master
        cities_with_weapon_master.append(city)
    return cities_with_weapon_master


def create_money_lender(cities):
    cities_with_money_lender = []
    for city in cities:
        money_lender = Classes.Money_Lender.MoneyLender(city)
        city.money_lender = money_lender
        cities_with_money_lender.append(city)
    return cities_with_money_lender


def calculate_list_mean(list_to_check):
    if sum(list_to_check) == 0:
        return 0
    else:
        mean = round(sum(list_to_check) / len(list_to_check))
        return mean


def calculate_average_price(old_price, old_items, new_price, new_items):
    # Calculate the average price of the old and new items
    if old_price == 0:
        return new_price
    elif new_items == 0:
        return old_price
    else:
        old_items_average_price = old_price * old_items
        new_items_average_price = new_price * new_items

        # Calculate the final average price
        average_price = (old_items_average_price + new_items_average_price) / (new_items + old_items)

        return round(average_price)


def set_new_captain(taverns):
    """
    Put a new captain in a random city, unless it was the one that had a captain.
    :param taverns:
    :return:
    """
    random_tavern = random.choice(taverns)
    while random_tavern.captain:
        random_tavern = random.choice(taverns)
    random_tavern.captain = True


def text_separation():
    """
    Aesthetic line, used to separate different notifications, bill, or a change turn.
    :return:
    """
    print("-" * 120)


def all_cities_change_turn(cities):
    for city in cities:
        city.change_turn()


def select_boat_from_convoy(convoy):
    counter = 1
    for boat in convoy.boats:
        print("{}- {}. ({}) {}% health.\n".
              format(counter, boat.name, boat.city.name, boat.health))
    option = input()
    option = correct_values(1, len(convoy.boats), option)
    return convoy.boats[option - 1]



def choose_boat_from_city(city):
    """
    Name self-explanatory, selects a ship (if there is one in the city)
    :param city:
    :return:
    """
    print("Is your ship free or in a convoy?\n"
          "1- Ship.\n"
          "2- Convoy.\n"
          "3- Exit.\n")
    option = input()
    option = correct_values(1, 3, option)
    if option == 3:
        return False
    elif option == 1:
        return choose_boat(city)
    elif option == 2:
        return choose_boat_from_convoy(city)


def choose_boat(city):
    counter = 1
    if len(city.boats) > 0:
        for boat in city.boats:
            print("{}- {}.".format(counter, boat.name))
            counter += 1
        option = input()
        option = correct_values(1, len(city.boats), option)
        return city.boats[option - 1]
    else:
        return False


def choose_boat_from_convoy(city):
    counter = 1
    if len(city.convoys) > 0:
        for convoy in city.convoys:
            print("{} {}".format(counter, convoy.name))
            counter += 1
        option = input()
        option = correct_values(1, len(city.convoys), option)
        return choose_boat(city.convoys[option - 1])
    else:
        return False


def choose_convoy(city):
    counter = 1
    for convoy in city.convoys:
        print("{} {}".format(counter, convoy.name))
        counter += 1
    option = input()
    option = correct_values(1, len(city.convoys), option)
    return city.convoys[option - 1]


def select_item(ship_or_convoy):
    """
    Returns string with the name of the product that we want to create.
    :return:
    """
    print("What do you want to select?\n"
          "1- Skins. You have {} at {} coins.\n"
          "2- Tools. You have {} at {} coins.\n"
          "3- Beer. You have {} at {} coins.\n"
          "4- Wine. You have {} at {} coins.\n"
          "5- Cloth. You have {} at {} coins.\n"
          .format(ship_or_convoy.skins, ship_or_convoy.price_skins, ship_or_convoy.tools, ship_or_convoy.price_tools,
                  ship_or_convoy.beer, ship_or_convoy.price_beer, ship_or_convoy.wine, ship_or_convoy.price_wine,
                  ship_or_convoy.cloth, ship_or_convoy.price_cloth))
    option = input()
    option = correct_values(1, 5, option)
    equivalences = {1: "skins", 2: "tools", 3: "beer", 4: "wine", 5: "cloth"}
    return equivalences[option]


"""All of the next functions are very easy to understand, due to the fact that they only return an attribute
from an object, given an string."""


def decrease_product_number(object, products):
    quantity = products[0]
    if products[1] == "skins":
        object.skins -= quantity
    elif products[1] == "tools":
        object.tools -= quantity
    elif products[1] == "beer":
        object.beer -= quantity
    elif products[1] == "wine":
        object.wine -= quantity
    elif products[1] == "cloth":
        object.cloth -= quantity


def increase_product_number(object, products):
    quantity = products[0]
    if products[1] == "skins":
        object.skins += quantity
    elif products[1] == "tools":
        object.tools += quantity
    elif products[1] == "beer":
        object.beer += quantity
    elif products[1] == "wine":
        object.wine += quantity
    elif products[1] == "cloth":
        object.cloth += quantity


def choose_prices(name, object):
    if name == "skins":
        return object.price_skins
    elif name == "tools":
        return object.price_tools
    elif name == "beer":
        return object.price_beer
    elif name == "wine":
        return object.price_wine
    elif name == "cloth":
        return object.price_cloth


def choose_products(name, object):
    if name == "skins":
        return object.skins
    elif name == "tools":
        return object.tools
    elif name == "beer":
        return object.beer
    elif name == "wine":
        return object.wine
    elif name == "cloth":
        return object.cloth


def set_price_to_zero(object):
    """
    Avoid getting a price on a product when there are no units in the inventory.
    :param object:
    :return:
    """
    if object.skins == 0:
        object.price_skins = 0
    if object.tools == 0:
        object.price_tools = 0
    if object.beer == 0:
        object.price_beer = 0
    if object.wine == 0:
        object.price_wine = 0
    if object.cloth == 0:
        object.price_cloth = 0


def change_prices(name, new_price, object):
    if name == "skins":
        object.price_skins = new_price
    elif name == "tools":
        object.price_tools = new_price
    elif name == "beer":
        object.price_beer = new_price
    elif name == "wine":
        object.price_wine = new_price
    elif name == "cloth":
        object.price_cloth = new_price


def return_trading_items_values(name, city):
    if name == "skins":
        return [city.max_price_skins, city.min_price_skins, city.skins]
    elif name == "tools":
        return [city.max_price_tools, city.min_price_tools, city.tools]
    elif name == "beer":
        return [city.max_price_beer, city.min_price_beer, city.beer]
    elif name == "wine":
        return [city.max_price_wine, city.min_price_wine, city.wine]
    elif name == "cloth":
        return [city.max_price_cloth, city.min_price_cloth, city.cloth]


def buy_from_city(ship_or_office):
    """
    Trading is not easy, and it is probably the most difficult function to read in the whole game,
    especially buying.

    It starts with selecting the current city, updating its prices and printing them out.

    Then choose the product we want to buy, and calculate how much free space we have on the ship.

    After that, it asks how many products we want to buy, the city class calculates if we have enough money,
    and finally returns the products.

    It calculates the average price, which is updated to have a better reference when we trade.

    :return:
    """
    # Select current city, update prices and choose a product.
    choosen_product = ship_or_office.city.choose_product()
    # Finding out how many empty space we have. Only if it is a ship or a convoy.
    try:
        ship_or_office.set_empty_space_and_max_load()
        empty_space = ship_or_office.empty_space
    except AttributeError:
        empty_space = 99_999

    # Selecting how many we want to buy, and returning it`s price.
    new_products = ship_or_office.city.how_many_buy(choosen_product, empty_space)
    product_prices = choose_prices(new_products[1], ship_or_office)
    product = choose_products(new_products[1], ship_or_office)
    new_price = new_products[2]
    average_price = calculate_average_price(product_prices,
                                            product, new_price, product + new_products[0])
    # Adding bought products and changing it`s mean price.
    increase_product_number(ship_or_office, new_products)
    change_prices(new_products[1], average_price, ship_or_office)


def sell_to_city(ship_or_office):
    """
    Selling is easier, as the city will always take everything.

    It chooses a product, calculate its price and then delete it from the boat.
    :return:
    """
    # Select current city, update prices and choose a product.
    choosen_product = ship_or_office.city.choose_product()
    inventory_product = choose_products(choosen_product[3], ship_or_office)
    product_price = choose_prices(choosen_product[3], ship_or_office)

    # Selecting how many we want to sell, and returning it`s price.
    new_products = ship_or_office.city.how_many_sell(choosen_product, [inventory_product, product_price])

    # deleting sold products.
    decrease_product_number(ship_or_office, new_products)
    if choose_products(choosen_product[3], ship_or_office) == 0:
        change_prices(choosen_product[3], 0, ship_or_office)


def calculate_how_many_can_buy_trader(given_price, minimum_price, maximum_price, num_products):
    """
    Calculates maximum number of items that a trader can buy, given the product prices and the trader settings.
    :param given_price:
    :param minimum_price:
    :param maximum_price:
    :param num_products:
    :return:
    """
    if given_price <= 0:
        return 0
    num_bought = 0
    proportional_price = minimum_price + (maximum_price - minimum_price) * (100 - num_products) / 100
    while num_bought < num_products and proportional_price <= given_price:
        num_bought += 1
        proportional_price = minimum_price + (maximum_price - minimum_price) * (100 - num_products + num_bought) / 100
    return num_bought


def add_trader(city):
    """
    Add trader to the commercial offices when hired.
    :param city:
    :return:
    """
    new_trader = Classes.Comercial_Office.Trader(city, city.commercial_office)
    city.commercial_office.trader = new_trader


def add_commercial_office(city):
    """
    Add a commercial office to the city when built.
    :param city:
    :return:
    """
    new_commercial_office = Classes.Comercial_Office.CommercialOffice(city)
    city.commercial_office = new_commercial_office


def return_factory_name(factory):
    """
    Necessary to use getatt
    :param factory:
    :return:
    """
    well_written = {"skins_factories": "skins factory",
                    "tools_factories": "tool factory",
                    "beer_factories": "beer factory",
                    "wine_factories": "wine factory",
                    "cloth_factories": "cloth factory"
                    }
    if factory in well_written:
        return well_written[factory]
    else:
        return False


def delete_convoy(convoy):
    """
    When a convoy is deleted, its ships have to return to the city as individual boats, then the former convoy object
    has to be deleted from city, player and finally from memory.
    :param convoy:
    :return:
    """
    city = convoy.city
    player = convoy.player
    for boat in convoy.boats:
        city.boats.append(boat)
        player.boats.append(boat)
    city.convoys.remove(convoy)
    player.convoys.remove(convoy)
    text_separation()
    print("Convoy {} has been dissolved.".format(convoy.name))
    text_separation()
    del convoy


def ask_witch_direction_to_move(object):
    if object.check_if_commercial_office():
        while True:
            print("What do you want to do?\n"
                  "1- Move from ship to warehouse.\n"
                  "2- Move from warehouse to ship.\n"
                  "3- Exit.\n")
            option = input("\n")
            option = correct_values(1, 3, option)
            if option == 3:
                break
            else:
                item_name = select_item()
            if option == 1:
                move_from_ship_or_convoy(object, item_name)
            elif option == 2:
                move_from_warehouse(object, item_name)


def move_from_ship_or_convoy(object, name):
    product = choose_products(name, object)
    product_price = choose_prices(name, object)
    print("You have {} {} at {} coins. How many do you want to move?\n"
          .format(product, name, product_price))
    option = input("\n")
    option = correct_values(0, product, option)
    if option == 0:
        pass
    else:
        moving_products(name, option, product_price, object, object.city.commercial_office)


def moving_products(name, how_many, price, origin, destiny):
    decrease_product_number(origin, [how_many, name])
    increase_product_number(destiny, [how_many, name])
    old_items = choose_products(name, destiny)
    old_price = choose_prices(name, destiny)
    new_price = calculate_average_price(old_price, old_items, price, how_many)
    change_prices(name, new_price, destiny)


def move_from_warehouse(object, name):
    while True:
        product = choose_products(name, object.city.commercial_office)
        product_price = choose_prices(name, object.city)
        print("You have {} {} at {} coins. How many do you want to move?\n"
              .format(product, name, product_price))
        option = input("\n")
        if option == "0":
            pass
        else:
            option = correct_values(0, product, option)
            moving_products(name, option, product_price, object.city.commercial_office, object)


def choose_city_to_travel(object, cities):
    """
    Enumerate and choose a city from a list.
    :param cities:
    :return:
    """
    print("Where do you want to move?\n")
    for i, x in enumerate(cities):
        print("{}- {}.".format(i + 1, x.name))
    option = input("\n")
    option = correct_values(1, len(cities), option)
    check_distance_between_cities(object, option - 1)


def check_distance_between_cities(object, option):
    """
    Check distance between cities. If they are close, will take fewer turns to move.
    :param option:
    :return:
    """
    cities = object.cities_list
    distance = object.city.possition + cities[option].possition
    if object.city == cities[option]:
        print("You are already in {}".format(object.city.name))
    else:
        print("{} is now moving to {}. Will take {} turns."
              .format(object.name, cities[option].name, distance))
        set_travel(object, distance, cities[option])


def set_travel(object, distance, destination):
    """
    Start moving to another city.
    :param distance:
    :param destination:
    :return:
    """
    object.travel_turns = distance
    object.traveling = True
    object.destination = destination
    object.boat_deterioration()
    object.city_before_travel = object.city
    if object in object.city.boats:
        object.city.boats.remove(object)
    if object in object.city.convoys:
        object.city.convoys.remove(object)
    object.city = False


def while_traveling(object):
    """
    Works every turn until arrival. Check if ship or convoy has arrived and calculate how many turns remain.
    :return:
    """
    if object.travel_turns > 1:
        object.travel_turns -= 1
    elif object.travel_turns == 1:
        object.city = object.destination
        object.city.boats.append(object)
        object.traveling = False
        object.destination = 0
        if object.is_convoy:
            print("Your convoy {} has arrived at {}"
                  .format(object.name, object.city.name))
        else:
            print("Your boat {} has arrived at {}."
                  .format(object.name, object.city.name))
    Functionalities.Combat.calculate_probability(object)

def check_if_traveling(object):
    """
    Return True if in open sea.
    :return:
    """
    if object.traveling:
        return True
    else:
        return False


def check_if_overloaded(object):
    object.set_empty_space_and_max_load()
    if object.empty_space < 0:
        print(f"{object.name} is overloaded and can't sail.\n")
        return False
    else:
        return True



def create_pirate_and_pirate_city():
    pirate = Classes.Player.Player("Evil_pirate", 1_000_000)
    pirate_city = Classes.Cities.City("Evil pirate city", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, False, 5, pirate)
    return pirate, pirate_city


def money_exchange(object_who_pays, object_who_get_paid, ammount):
    """
    Function to exchange money from two objects.
    :param object_who_pays:
    :param object_who_get_paid:
    :param ammount:
    :return:
    """
    if object_who_pays.coins < ammount:
        print("You can't afford to pay {} coins. You only have {}".format(ammount, object_who_pays.coins))
        return False
    else:
        object_who_pays.coins -= ammount
        object_who_get_paid.coins += ammount
        return True

