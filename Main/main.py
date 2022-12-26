import Functionalities.Utilities
import Classes.Boats_and_Convoys


# Inicializamos tutto a ver si rula
player = Functionalities.Utilities.create_player()
Cities = Functionalities.Utilities.create_cities()
Lubeck = Cities[0]
Rostock = Cities[1]
Malmo = Cities[2]
Stettin = Cities[3]
Gdanks = Cities[4]
boat1 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0], 8, False, 0, "Prueba", player.city)
player.boats.append(boat1)
boat2 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0], 8, False, 0, "Adios", Malmo)
player.boats.append(boat2)
turn = 1



def welcome():
    print("Welcome to this tribute to Patrician III by FernandooMarinn (GitHub)")


def game_loop():
    turn = 0
    while True:
        turn += 1
        while True:
            print("\nWhat do you want to do?. Your current turn is {}.\n\n"
                  "1- Choose a boat.\n"
                  "2- Choose a convoy.\n"
                  "3- Go to city buildings.\n"
                  "4- Change city.\n"
                  "5- Pass turn.\n"
                  "6- Check player stats.\n"
                  "7- Exit game.\n".format(turn))
            option = input()
            option = Functionalities.Utilities.correct_values(1, 7, option)
            if option == 5:
                break
            else:
                choose_options(option)


def choose_options(option):
    if option == 1:
        player.check_boats()
    elif option == 2:
        player.check_convoys()
    elif option == 3:
        current_city = player.city
        current_city.create_factories_menu(player.coins)
    elif option == 4:
        player.change_city(Cities)
    elif option == 6:
        player.check_player()
    elif option == 7:
        exit()


def main():
    game_loop()


if __name__ == '__main__':
    main()
