import os
import pickle
import Classes.Game
import Classes.Boats_and_Convoys
import Functionalities.Utilities


def check_current_folder_files():
    # Get the path of the folder where the current script is located
    folder_path = os.path.dirname(__file__)

    # Specify the file extension you want to search for
    file_extension = '.pickle'

    # Use the listdir() function to list the files in the folder
    files = os.listdir(folder_path)
    saved_games = []
    # Iterate over the files and check if they have the desired extension
    for file in files:
        if file.endswith(file_extension):
            saved_games.append(file)
            print(os.path.join(folder_path, file))
    if len(saved_games) == 0:
        print("You don't have any saved game in this folder. You are going to start a new game.\n")
        return False
    else:
        return True


def save_game(game):
    to_save = [game]

    name = input("What is the name of this game?\n")
    with open(f"{name}.pickle", "wb") as savefile:
        pickle.dump(to_save, savefile)


def load_game(save_game):
    while True:
        if not check_current_folder_files():
            return False
        else:
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
        if not load_game(WHOLE_GAME):
            option = 1
        else:
            return WHOLE_GAME

    if option == 1:
        player = Functionalities.Utilities.create_player()
        Cities = Functionalities.Utilities.create_cities(player)
        player.city = Functionalities.Utilities.ask_initial_city(Cities)
        player.all_cities_list = Cities

        cities_list = Functionalities.Utilities.add_all_buildings(Cities)


        boat1 = Classes.Boats_and_Convoys.Boat(100, 3, [0, 0, 0, 0, 0], 20, True, 0, "Prueba", player.city, player)
        player.boats.append(boat1)
        boat2 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0], 8, False, 0, "Adios", cities_list[2], player)
        player.boats.append(boat2)

        create_pirates = Functionalities.Utilities.create_pirate_and_pirate_city()
        player.pirate = create_pirates[0]
        player.pirate_city = create_pirates[1]

        WHOLE_GAME = Classes.Game.Game(player, cities_list)
        return WHOLE_GAME


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


def update_player(saved_player, current_player):
    current_player.name = saved_player.name
    current_player.coins = saved_player.coins
    current_player.level = saved_player.level
    current_player.city = saved_player.city
    current_player.experience = saved_player.experience
    current_player.boats = saved_player.boats
    current_player.convoys = saved_player.convoys
    current_player.turn = saved_player.turn
    current_player.all_cities_list = saved_player.all_cities_list

    current_player.number_of_offices = saved_player.number_of_offices
    current_player.can_build_offices = saved_player.can_build_offices
    current_player.bill = saved_player.bill




def update_cities(saved_cities, current_cities):
    for i in range(len(saved_cities)):
        current_cities[i].coins = saved_cities[i].coins
        current_cities[i].skins = saved_cities[i].skins
        current_cities[i].tools = saved_cities[i].tools
        current_cities[i].beer = saved_cities[i].beer
        current_cities[i].wine = saved_cities[i].wine
        current_cities[i].cloth = saved_cities[i].cloth
        current_cities[i].name = saved_cities[i].name

        current_cities[i].skins_consumption_ratio = saved_cities[i].skins_consumption_ratio
        current_cities[i].tools_consumption_ratio = saved_cities[i].tools_consumption_ratio
        current_cities[i].beer_consumption_ratio = saved_cities[i].beer_consumption_ratio
        current_cities[i].wine_consumption_ratio = saved_cities[i].wine_consumption_ratio
        current_cities[i].cloth_consumption_ratio = saved_cities[i].cloth_consumption_ratio

        current_cities[i].skins_consumption = saved_cities[i].skins_consumption
        current_cities[i].tools_consumption = saved_cities[i].tools_consumption
        current_cities[i].beer_consumption = saved_cities[i].beer_consumption
        current_cities[i].wine_consumption = saved_cities[i].wine_consumption
        current_cities[i].cloth_consumption = saved_cities[i].cloth_consumption

        current_cities[i].skins_production = saved_cities[i].skins_production
        current_cities[i].tools_production = saved_cities[i].tools_production
        current_cities[i].beer_production = saved_cities[i].beer_production
        current_cities[i].wine_production = saved_cities[i].wine_production
        current_cities[i].cloth_production = saved_cities[i].cloth_production

        current_cities[i].skins_factories = saved_cities[i].skins_factories
        current_cities[i].tools_factories = saved_cities[i].tools_factories
        current_cities[i].beer_factories = saved_cities[i].beer_factories
        current_cities[i].wine_factories = saved_cities[i].wine_factories
        current_cities[i].cloth_factories = saved_cities[i].cloth_factories

        current_cities[i].can_produce_skins = saved_cities[i].can_produce_skins
        current_cities[i].can_produce_tools = saved_cities[i].can_produce_tools
        current_cities[i].can_produce_beer = saved_cities[i].can_produce_beer
        current_cities[i].can_produce_wine = saved_cities[i].can_produce_wine
        current_cities[i].can_produce_cloth = saved_cities[i].can_produce_cloth

        current_cities[i].price_skins = saved_cities[i].price_skins
        current_cities[i].price_tools = saved_cities[i].price_tools
        current_cities[i].price_beer = saved_cities[i].price_beer
        current_cities[i].price_wine = saved_cities[i].price_wine
        current_cities[i].price_cloth = saved_cities[i].price_cloth
        current_cities[i].houses = saved_cities[i].houses
        current_cities[i].population = saved_cities[i].population

        current_cities[i].commercial_office = saved_cities[i].commercial_office
        current_cities[i].have_commercial_office = saved_cities[i].have_commercial_office
        current_cities[i].money_lender = saved_cities[i].money_lender
        current_cities[i].shipyard = saved_cities[i].shipyard
        current_cities[i].tavern = saved_cities[i].tavern
        current_cities[i].weapon_master = saved_cities[i].weapon_master
        current_cities[i].possition = saved_cities[i].possition

        current_cities[i].boats = saved_cities[i].boats
        current_cities[i].convoys = saved_cities[i].convoys
        current_cities[i].player = saved_cities[i].player
        current_cities[i].tavern = saved_cities[i].tavern

        current_cities[i].construction_queue = saved_cities[i].construction_queue
