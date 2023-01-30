import Functionalities.Utilities
import Functionalities.Save_game


WHOLE_GAME = Functionalities.Save_game.load_or_new_game()
player = WHOLE_GAME.player
Cities = WHOLE_GAME.cities


def welcome():
    Functionalities.Utilities.text_separation()
    print("Welcome to this tribute to Patrician III by FernandooMarinn (GitHub)")
    Functionalities.Utilities.text_separation()


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
          "8- Save/Load game.\n"
          "9- Exit game.\n".format(player.turn, player.city.name))


def game_loop():
    while True:
        change_turn(player, Cities)
        Functionalities.Utilities.text_separation()
        Functionalities.Utilities.text_separation()
        while True:
            print_menu()
            option = input()
            option = Functionalities.Utilities.correct_values(1, 9, option)
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
        Functionalities.Save_game.choose_save_or_load_game(WHOLE_GAME)
    elif option == 9:
        goodbye()


def goodbye():
    print("\n\n\nBye! See you next time!\n")
    exit()


def main():
    welcome()
    game_loop()


if __name__ == '__main__':
    main()
