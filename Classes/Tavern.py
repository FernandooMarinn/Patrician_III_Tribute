import Functionalities.Utilities


class Tavern:
    def __init__(self, city):
        self.city = city
        self.sailors = 12
        self.captain = False
        self.boat = 0
        self.convoy = 0

    def calculate_sailors(self):
        if self.sailors < 20:
            self.sailors += 8
        elif self.sailors < 55:
            self.sailors += 4

    def change_turn(self):
        self.calculate_sailors()

    def add_captain(self):
        self.captain = True

    def print_if_captain_and_sailors(self):
        Functionalities.Utilities.text_separation()
        if self.captain:
            print("This tavern does have a captain.\n")
        else:
            print("This tavern does´t have a captain.\n")
        print("There are {} sailors drinking beer.\n"
              .format(self.sailors))
        Functionalities.Utilities.text_separation()


    def show_menu(self, boat):
        self.print_if_captain_and_sailors()
        print("What do you want to do?\n"
              "1- Hire sailors.\n"
              "2- Hire captain.\n"
              "3- Exit.\n\n")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 3, option)
        if option == 3:
            pass
        else:
            self.choose_options(option, boat)
        boat.check_if_enough_sailors()

    def choose_options(self, option, boat):
        if option == 1:
            self.hire_sailors(boat)
        else:
            self.hire_captain(boat)

    def hire_sailors(self, boat):
        print("How many sailors do you want to hire? You have space for {}.\n".format(boat.max_sailors - boat.sailors))
        option = input()
        option = Functionalities.Utilities.correct_values(0, self.sailors, option)
        if boat.sailors + option > boat.max_sailors:
            print("So many sailors won´t fit in your boat.")
        else:
            boat.sailors += option
            print("Your new sailors are already in your ship.")



    def hire_captain(self, boat):
        if not self.captain:
            print("This tavern does not have a captain. You should go to another city and take a chance.")
        else:
            print("Do you want to hire a captain for your boat {}? It will cost 15 coins each turn.\n"
                  "1- Yes.\n"
                  "2- No.\n"
                  .format(boat.name))
            option = input()
            option = Functionalities.Utilities.correct_values(1, 2, option)
            if option == 1:
                boat.captain = True
                print("Your captain has enrolled your ship, and is ready to sail.")
                all_taverns = Functionalities.Utilities.return_taverns(self.city.player.all_cities_list)
                Functionalities.Utilities.set_new_captain(all_taverns)
                self.captain = False
            else:
                print("The captain watch you from the table. -Why do you even bother me?")

