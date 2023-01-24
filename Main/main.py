import Functionalities.Utilities
import Functionalities.Save_game
import Classes.Boats_and_Convoys
import Classes.Game
import Classes.Player
import pickle


""" To do list:
1- Hacer que suba la población.
4- Hacer todas las ciudades y todos los productos (ultimo).

"""


def save_game(game):
    to_save = [game]

    name = input("What is the name of this game?\n")
    with open(f"{name}.pickle", "wb") as savefile:
        pickle.dump(to_save, savefile)


def load_game(save_game):
    while True:
        name = input("\nWhat is the name of your saved game?\n")
        try:
            with open(f"{name}.pickle", "rb") as savefile:
                game = pickle.load(savefile)
            Functionalities.Save_game.update_player(game[0].player, save_game.player)
            Functionalities.Save_game.update_cities(game[0].cities, save_game.cities)
            break
        except FileNotFoundError:
            print("There is not a file named {}.\n".format(name))

def load_or_new_game():
    print("Do you want to start a new game, or load a previus one?.\n"
          "1- New.\n"
          "2- Load.\n")
    option = input()
    option = Functionalities.Utilities.correct_values(1, 2, option)

    if option == 2:
        player = Classes.Player.Player("player", 5000)
        Cities = Functionalities.Utilities.create_cities(player)
        WHOLE_GAME = Classes.Game.Game(player, Cities)
        load_game(WHOLE_GAME)
        return WHOLE_GAME

    elif option == 1:
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

        create_pirates = Functionalities.Utilities.create_pirate_and_pirate_city()
        player.pirate = create_pirates[0]
        player.pirate_city = create_pirates[1]

        WHOLE_GAME = Classes.Game.Game(player, cities_list)
        return WHOLE_GAME

WHOLE_GAME = load_or_new_game()
player = WHOLE_GAME.player
Cities = WHOLE_GAME.cities


def choose_save_or_load_game(game):
    print("What do you want to do?.\n"
          "1- Save game.\n"
          "2- Load game.\n")
    option = input()
    option = Functionalities.Utilities.correct_values(1, 2, option)
    if option == 1:
        save_game(game)
    elif option == 2:
        load_game(game)




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
        choose_save_or_load_game(WHOLE_GAME)
    elif option == 9:
        exit()



def main():
    welcome()
    game_loop()


if __name__ == '__main__':
    main()
