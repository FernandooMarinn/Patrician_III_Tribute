import Classes.Cities
from Classes import Player


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
          "3- 25000 (normal).\n"
          "4- 50000 (too much).\n")
    option = input()
    return correct_values(1, 4, option)


def return_coins_quantity(option):
    if option == 1:
        return 5000
    elif option == 2:
        return 10000
    elif option == 3:
        return 25000
    elif option == 4:
        return 50000


def ask_initial_city():
    cities = ["Lubeck", "Stettin", "Malmo", "Rostock"]
    print("\n")
    for i in range(len(cities)):
        print("{}- {}.".format(i + 1, cities[i]))
    option = input("Wich city do you choose as your birthplace?\n")
    option = correct_values(1, 4, option)
    return cities[option - 1]


def create_player():
    """
    returns object player
    :return:
    """
    name = input("What is your name?\n")
    coins = return_coins_quantity(ask_initial_money())
    city = ask_initial_city()
    player = Player.Player(name, coins, city)
    return player


def create_cities():
    Lubeck = Classes.Cities.City("Lubeck", 3, 4, 6, 3, 3, 40, 60, 50, 50, 30, 0, 15, 0, 9, 0, False, True, False, True,
                                 False, False)
    return Lubeck