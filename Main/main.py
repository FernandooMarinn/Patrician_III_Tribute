import Classes.Boats_and_Convoys
import Functionalities.Utilities
from Classes import *
from Functionalities import *



# Inicializamos tutto a ver si rula
player = Functionalities.Utilities.create_player()
Lubeck = Functionalities.Utilities.create_cities()
boat1 = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0], 8, False, 0, "Leire", Lubeck)
player.boats.append(boat1)

def welcome():
    print("Welcome to this tribute to Patrician III by FernandooMarinn (GitHub)")

def game_loop():
    while True:
        print("What do you want to do?.\n"
              "1- Choose a boat.\n"
              "2- Choose a convoy.\n"
              "3- Go to city buildings.\n"
              "4- Change city.\n")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 4, option)
        choose_options(option)

def choose_options(option):
    if option == 1:
        player.check_boats()

def main():
    game_loop()

if __name__ == '__main__':
    main()