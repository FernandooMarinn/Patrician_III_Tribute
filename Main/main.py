import Functionalities.Utilities
import Classes.Boats_and_Convoys



""" To do list:
1- combat.
2- finish levels.
3- pirates
4- Hacer todas las ciudades y todos los productos (ultimo).
5- Guardado y cargado IMPORTANTE
8- Que no baje nunca de 0 el dinero
"""



# Creating everything to see if it works.
player = Functionalities.Utilities.create_player()
Cities = Functionalities.Utilities.create_cities(player)

player.city = Functionalities.Utilities.ask_initial_city(Cities)
player.all_cities_list = Cities

cities_list = Functionalities.Utilities.add_all_buildings(Cities)


boat1 = Classes.Boats_and_Convoys.Boat(100, 3, [0, 0, 0, 0, 0], 20, True, 0, "Prueba", player.city, player)
player.boats.append(boat1)
boat2 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0], 8, False, 0, "Adios", cities_list[2], player)
player.boats.append(boat2)

all_taverns = [city.tavern for city in cities_list]

def welcome():
    print("Welcome to this tribute to Patrician III by FernandooMarinn (GitHub)")


def print_menu():
    Functionalities.Utilities.text_separation()
    print("\nWhat do you want to do?. Your current turn is {}. Your are in {}\n\n"
          "1- Choose a boat.\n"
          "2- Choose a convoy.\n"
          "3- View moving boats and convoys.\n"
          "4- Go to city buildings.\n"
          "5- Change city.\n"
          "6- Check player stats.\n"
          "7- Pass turn.\n"
          "8- Exit game.\n".format(player.turn, player.city.name))


def game_loop():
    while True:
        change_turn(player, cities_list)
        Functionalities.Utilities.text_separation()
        Functionalities.Utilities.text_separation()
        while True:
            print_menu()
            option = input()
            option = Functionalities.Utilities.correct_values(1, 8, option)
            if option == 7:
                break
            else:
                choose_options(option)


def change_turn(player, cities_list):
    if player.turn == 0:
        player.turn += 1
    else:
        player.change_turn()
        Functionalities.Utilities.all_cities_change_turn(cities_list)


def random_new_captain():
    Functionalities.Utilities.set_new_captain(all_taverns)


def choose_options(option):
    if option == 1:
        player.check_boats()
    elif option == 2:
        player.check_convoys()
    elif option == 3:
        player.view_all_traveling_units()
    elif option == 4:
        player.city.menu_city_buildings()
    elif option == 5:
        player.change_city(Cities)
    elif option == 6:
        player.check_player()
    elif option == 8:
        exit()


def main():
    game_loop()


if __name__ == '__main__':
    main()
