import random

import Functionalities.Utilities


class MoneyLender:
    def __init__(self, city):
        self.level = 1
        self.experience = 0
        self.city = city
        self.player = self.city.player

        self.grant_loans_this_turn = []
        self.ask_loans_this_turn = []
        self.current_loans = []

        self.level_increases = {
            1: [random.randint(5000, 20_000), random.randint(20, 50), random.randint(4, 10)],
            2: [random.randint(7000, 28_000), random.randint(20, 50), random.randint(3, 12)],
            3: [random.randint(10_000, 35_000), random.randint(20, 60), random.randint(2, 14)]
        }

        self.change_turn()

    def gain_experience(self, experience):
        self.experience += experience
        self.level_up()

    def level_up(self):
        if self.level == 1:
            if self.experience > 10_000:
                self.level += 1
                self.experience -= 10_000
        elif self.level == 2:
            if self.experience > 15_000:
                self.level += 1
                self.experience -= 15_000

    def generate_loans(self):
        """
        Return loan options.
        :return:
        """
        options = self.get_loan_options_depending_levels()
        for option in options:
            total_to_return = round(((option[0] * option[1]) / 100) + option[0])
            option.append(total_to_return)
        return options

    def print_loan_individually(self, option, counter):
        """
        Print out individually every loan option.
        :param option:
        :param counter:
        :return:
        """
        print("{}- {} with an interest of {}%, to repay in {} turns. Total to repay is {} coins.\n"
              .format(counter, option[0], option[1], option[2], option[3]))

    def print_loans(self, options, mode):
        counter = 1
        print("Your options are:\n")
        for loan_option in options:
            self.print_loan_individually(loan_option, counter)
            counter += 1
        option = input()
        option = Functionalities.Utilities.correct_values(1, 3, option)
        if mode == "ask":
            self.asking_loan(options[option - 1])
        elif mode == "grant":
            self.granting_loan(options[option - 1])

    def asking_loan(self, loan_option):
        """
        Checks if we want to accept a certain loan, changing money and adding to current loans.
        :param loan_option:
        :return:
        """
        print("Do you want to take this loan?\n")
        self.print_loan_individually(loan_option, "-")
        option = input("1- Yes.\n"
                       "2- No. \n")
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if option == 1:
            if self.check_if_less_than_three_loans():
                self.ask_loans_this_turn.remove(loan_option)
                loan_option.append("ask")
                self.money_change(loan_option)
                self.current_loans.append(loan_option)
                self.city.player.achievements.increase_loan_number("ask")

    def granting_loan(self, loan_option):
        """
        Check if we want to grant a loan, and calculates money.
        :param loan_option:
        :return:
        """
        print("Do you want to grant this loan?\n")
        self.print_loan_individually(loan_option, "-")
        option = input("1- Yes.\n"
                       "2- No. \n")
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if option == 1:
            if self.check_if_less_than_three_loans():
                if self.player.coins >= loan_option[0]:
                    self.grant_loans_this_turn.remove(loan_option)
                    loan_option.append("grant")
                    self.money_change(loan_option)
                    self.current_loans.append(loan_option)
                    self.city.player.achievements.increase_loan_number("grant")
                else:
                    Functionalities.Utilities.text_separation()
                    print("You dont have money to grant this loan.")
                    Functionalities.Utilities.text_separation()

    def money_change(self, loan_option):
        Functionalities.Utilities.text_separation()
        if loan_option[4] == "ask":
            self.player.coins += loan_option[0]
            print("You have received {} coins. Remember that you have to return it!".format(loan_option[0]))
        elif loan_option[4] == "grant":
            self.player.coins -= loan_option[0]
            print("You have granted a loan for {} coins. It will be returned to you.".format(loan_option[0]))
        Functionalities.Utilities.text_separation()

    def pass_turn_loans_and_finish_them(self):
        """
        When a turn changes, decreases every loan duration. If duration reaches 0, send loan to finishing.
        :return:
        """
        to_delete = []
        for loan in self.current_loans:
            loan[2] -= 1
            if loan[2] == 0:
                self.finish_loan(loan)
                to_delete.append(loan)
        for item_to_delete in to_delete:
            self.current_loans.remove(item_to_delete)

    def finish_loan(self, loan):
        """
        Finishes every loan. If it was granted, gives money to player. If it was taken, gets money from player.
        :param loan:
        :return:
        """
        Functionalities.Utilities.text_separation()
        if loan[4] == "ask":
            self.player.coins -= loan[3]
            print("One of your loans has expired in {}. You have paid {} coins to the money lender."
                  .format(self.city.name, loan[3]))
        elif loan[4] == "grant":
            self.player.coins += loan[3]
            print("One of your loans has expired in {}. You receive {} coins from the money lender."
                  .format(self.city.name, loan[3]))
        self.gain_experience(loan[3])
        Functionalities.Utilities.text_separation()

    def check_if_less_than_three_loans(self):
        """
        If there are 3 current loans, this function warns you and won't let you continue to get another.
        :return:
        """
        if len(self.current_loans) >= 3:
            print("You have three loans, you have to wait for one to finish.")
            return False
        else:
            return True

    def return_loan(self):
        """
        To return a loan before it finishes.
        :return:
        """
        counter = 1
        asked_loans = []
        for loan in self.current_loans:
            if loan[4] == "ask":
                asked_loans.append(loan)
        if len(asked_loans) > 0:
            for loan in asked_loans:
                self.print_loan_individually(loan, counter)
                counter += 1
            option = input()
            option = Functionalities.Utilities.correct_values(1, len(asked_loans), option)
            self.finish_loan(asked_loans[option - 1])
        else:
            print("You dont have loans to return.\n")

    def show_menu(self):
        """
        Prints out money lender menu.
        :return:
        """
        while True:
            print("What do you want to do?\n"
                  "1- Ask for a loan.\n"
                  "2- Grant a loan.\n"
                  "3- Check current loans.\n"
                  "4- Return loan.\n"
                  "5- Exit")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 5, option)
            if option == 5:
                break
            else:
                self.choose_option(option)

    def choose_option(self, option):
        if option == 1:
            self.print_loans(self.ask_loans_this_turn, "ask")
        elif option == 2:
            self.print_loans(self.grant_loans_this_turn, "grant")
        elif option == 3:
            self.check_loans()
        elif option == 4:
            self.return_loan()

    def check_loans(self):
        """
        Check every current loan, and prints out all the information.
        :return:
        """
        Functionalities.Utilities.text_separation()
        if len(self.current_loans) == 0:
            print("You dont have any loans to check.\n")
        else:
            counter = 1
            for loan in self.current_loans:
                self.print_loan_individually(loan, counter)
                if loan[4] == "ask":
                    print("You have asked for this loan, and you have to return it.\n")
                elif loan[4] == "grant":
                    print("You have granted this loan, you will have the money returned to you.\n")
                counter += 1
                Functionalities.Utilities.text_separation()
        Functionalities.Utilities.text_separation()

    def reboot_loans(self):
        """
        Depending on level, amount and interest of loans changes.
        :return:
        """
        self.level_increases = {
            1: [random.randint(5000, 20_000), random.randint(20, 50), random.randint(4, 10)],
            2: [random.randint(7000, 28_000), random.randint(20, 50), random.randint(3, 12)],
            3: [random.randint(10_000, 35_000), random.randint(20, 60), random.randint(2, 14)]
        }
        return self.level_increases[self.level]

    def change_loans_every_turn(self):
        self.grant_loans_this_turn = self.generate_loans()
        self.ask_loans_this_turn = self.generate_loans()

    def get_loan_options_depending_levels(self):
        return [self.reboot_loans() for _ in range(3)]

    def change_turn(self):
        """
        Every time a turn changes.
        :return:
        """
        self.level_up()
        self.pass_turn_loans_and_finish_them()
        self.change_loans_every_turn()
