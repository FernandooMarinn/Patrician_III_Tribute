import os
import pickle
import Classes.Game
import Classes.Boats_and_Convoys
import Classes.Player
import Functionalities.Utilities


def check_current_folder_files():
    # Get the path of the folder where the current script is located
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Specify the file extension you want to search for
    file_extension = '.pickle'

    # Use the listdir() function to list the files in the folder
    saved_games_folder = os.path.join(folder_path, "saved games")
    if not os.path.exists(saved_games_folder):
        os.mkdir(saved_games_folder)
    files = os.listdir(saved_games_folder)
    saved_games = []
    # Iterate over the files and check if they have the desired extension
    for file in files:
        if file.endswith(file_extension):
            saved_games.append(file)
            print(os.path.join(saved_games_folder, file))
    if len(saved_games) == 0:
        print("You don't have any saved game in this folder.\n")
        return False
    else:
        return True


def save_game(game):
    """
    Ask for a name, and save a game in the script's folder.
    :param game:
    :return:
    """
    to_save = [game]

    name = input("What is the name of this game?\n")
    script_folder = os.path.dirname(os.path.abspath(__file__))
    saved_games_folder = os.path.join(script_folder, "saved games")
    if not os.path.exists(saved_games_folder):
        os.mkdir(saved_games_folder)
    save_path = os.path.join(saved_games_folder, f"{name}.pickle")
    try:
        os.remove(save_path)
    except FileNotFoundError:
        pass
    with open(save_path, "wb") as savefile:
        pickle.dump(to_save, savefile)


def load_game():
    """
    Load game, if file exist.
    :param current_game:
    :return:
    """
    while True:
        if not check_current_folder_files():
            return False
        else:
            name = input("\nWhat is the name of your saved game?\n")
            folder_path = os.path.dirname(os.path.abspath(__file__))
            saved_games_folder = os.path.join(folder_path, "saved games")
            save_path = os.path.join(saved_games_folder, f"{name}.pickle")
            try:
                with open(save_path, "rb") as savefile:
                    game = pickle.load(savefile)
                    game = game[0]
                return game
            except FileNotFoundError:
                print("There is not a file named {}.\n".format(name))


def load_or_new_game():
    """
    First function of the game. Ask if want to create a new game, or if want to load one. If load, it creates an empty
    player and cities objects, in order to copy the game inside them.

    Else, it creates a player, all cities, pirates, and boats for start a new game, and return it all in a game object.
    :return:
    """
    print("Do you want to start a new game, or load a previus one?.\n"
          "1- New.\n"
          "2- Load.\n")
    option = input()
    option = Functionalities.Utilities.correct_values(1, 2, option)
    if option == 2:
        saved_game = load_game()
        if not saved_game:
            print("\nYou are going to start a new game.\n")
            option = 1
        else:
            return saved_game

    if option == 1:
        player = Functionalities.Utilities.create_player()
        cities = Functionalities.Utilities.create_cities(player)
        player.city = Functionalities.Utilities.ask_initial_city(cities)
        player.all_cities_list = cities

        cities_list = Functionalities.Utilities.add_all_buildings(cities)

        boat1 = Classes.Boats_and_Convoys.Boat(100, 3, [0, 0, 0, 0, 0, 0], 20, True, 0, "Freedom", player.city, player)
        player.boats.append(boat1)
        boat2 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0, 0], 8, False, 0, "Eagle", player.city, player)
        player.boats.append(boat2)

        create_pirates = Functionalities.Utilities.create_pirate_and_pirate_city()
        player.pirate = create_pirates[0]
        player.pirate_city = create_pirates[1]

        WHOLE_GAME = Classes.Game.Game(player, cities_list)
        return WHOLE_GAME


def choose_save_or_load_game(game):
    """
    Function to save or load a game whenever we want, during the game.
    :param game:
    :return:
    """
    print("What do you want to do?.\n"
          "1- Save game.\n"
          "2- Load game.\n")
    option = input()
    option = Functionalities.Utilities.correct_values(1, 2, option)
    if option == 1:
        save_game(game)
    elif option == 2:
        load_game()





