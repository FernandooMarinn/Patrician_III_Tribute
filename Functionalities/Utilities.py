import Classes.Cities, Classes.Tavern, Classes.Player
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
    can_afford_number = round(money / price)
    print("You can afford {}".format(can_afford_number))


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


def create_taverns(ciudades):
    taverns = [Classes.Tavern.Tavern(ciudades[0])]


def create_cities(player):
    # Puta mierda
    Lubeck = Classes.Cities.City("Lubeck", 3, 4, 6, 3, 3, 40, 60, 50, 50, 30, 0, 15, 0, 9, 0, False, True, False, True,
                                 False, False, 1, player)
    Rostock = Classes.Cities.City("Rostock", 3, 4, 6, 3, 3, 40, 60, 50, 50, 30, 0, 0, 0, 0, 0, False, False, False, False,
                                 False, False, 1, player)
    Malmo = Classes.Cities.City("Malmo", 3, 4, 6, 3, 3, 60, 60, 50, 50, 30, 0, 15, 0, 9, 0, True, False, False, False,
                                 True, False, 1, player)
    Stettin = Classes.Cities.City("Stettin", 3, 4, 6, 3, 3, 40, 60, 50, 50, 30, 0, 15, 0, 9, 0, False, False, True, True,
                                 False, False, 1, player)
    Gdanks = Classes.Cities.City("Gdanks", 3, 4, 4, 3, 3, 30, 40, 60, 40, 40, 0, 0, 10, 0, 0, False, False, True, False,
                                 False, False, 1, player)
    return Lubeck, Rostock, Malmo, Stettin, Gdanks

def calculate_list_mean(list):
    if sum(list) == 0:
        return 0
    else:
        mean = round(sum(list) / len(list))
        return mean

def calculate_average_price(old_price, old_items, new_price, new_items):
    # Calculate the average price of the old and new items
    if old_price == 0:
        return new_price
    else:
        old_items_average_price = old_price * old_items
        new_items_average_price = new_price * new_items

        # Calculate the final average price
        average_price = ((old_items_average_price + new_items_average_price)) / (new_items + old_items)

        return round(average_price)


def set_new_captain(taverns):
    random_tavern = random.randint(0, len(taverns))
    new_captain = taverns[random_tavern]
    new_captain.captain = True

def text_separation():
    print("-" * 60)

def all_cities_change_turn(cities):
    for city in cities:
        city.change_turn()