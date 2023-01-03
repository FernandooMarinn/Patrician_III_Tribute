import Functionalities.Utilities
import Classes.Boats_and_Convoys


# Creating everything to see if it works.
player = Functionalities.Utilities.create_player()
Cities = Functionalities.Utilities.create_cities(player)
player.city = Functionalities.Utilities.ask_initial_city(Cities)

Lubeck = Cities[0]
Rostock = Cities[1]
Malmo = Cities[2]
Stettin = Cities[3]
Gdanks = Cities[4]

cities_list = [Lubeck, Rostock, Malmo, Stettin, Gdanks]


boat1 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0], 8, False, 0, "Prueba", player.city, player, cities_list)
player.boats.append(boat1)
boat2 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0], 8, False, 0, "Adios", Malmo, player, cities_list)
player.boats.append(boat2)


def welcome():
    print("Welcome to this tribute to Patrician III by FernandooMarinn (GitHub)")


def print_menu():
    print("\nWhat do you want to do?. Your current turn is {}.\n\n"
          "1- Choose a boat.\n"
          "2- Choose a convoy.\n"
          "3- View moving boats and convoys.\n"
          "4- Go to city buildings.\n"
          "5- Change city.\n"
          "6- Check player stats.\n"
          "7- Pass turn.\n"
          "8- Exit game.\n".format(player.turn))


def game_loop():
    while True:
        change_turn()
        while True:
            print_menu()
            option = input()
            option = Functionalities.Utilities.correct_values(1, 8, option)
            if option == 7:
                break
            else:
                choose_options(option)


def change_turn():
    player.change_turn()
    Functionalities.Utilities.all_cities_change_turn(cities_list)


def choose_options(option):
    if option == 1:
        player.check_boats()
    elif option == 2:
        player.check_convoys()
    elif option == 3:
        player.view_all_traveling_units()
    elif option == 4:
        current_city = player.city
        current_city.create_factories_menu(player.coins)
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
