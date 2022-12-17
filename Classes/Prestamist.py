import random
class Prestamist():
    def __init__(self, name):
        self.level = 1
        self.experience = 0
        self.coins = 0
        self.name = name

    def generate_loans(self):
        options = []
        #compren = []
        #compren = [[random.randint(5000, 20000), random.randint(20, 50), random.randint(4, 12)] for i in range(4)]
        #compren = [compren[i].append(round(compren[i[0]] + ((compren[i[0]] * compren[i[1]]) / 100))) for i in range(4)]
        #print(compren)
        for i in range(4):
            #        Quantity                      Interest                 Turns to repay
            option = [random.randint(5000, 20000), random.randint(20, 50), random.randint(4, 12)]
            # Total to repay
            option.append(round(option[0] + ((option[0] * option[1]) / 100)))
            options.append(option)
        print(options)
        return options

    def print_loans(self, options):
        option_1 = options[0]
        option_2 = options[1]
        option_3 = options[2]
        #all_options = [print("1- {} with an interest of {}%, to repay in {} turns. You have to repay {} coins."
                             #.format(option_1[0], option_1[1], option_1[2], option_1[3])) for i in range(3)]
        print("Your options are:\n"
              "1- {} with an interest of {}%, to repay in {} turns. You have to repay {} coins.\n"
              "2- {} with an interest of {}%, to repay in {} turns. You have to repay {} coins.\n"
              "3- {} with an interest of {}%, to repay in {} turns. You have to repay {} coins.\n"
              "4- Exit."
              .format(option_1[0], option_1[1], option_1[2], option_1[3],
                      option_2[0], option_2[1], option_2[2], option_2[3],
                      option_3[0], option_3[1], option_3[2], option_3[3]))

    def show_menu(self):
        print("What do you want to do?\n"
              "1- Ask for a loan.\n"
              "2- Exit")

    def choose_option(self):
        number = int(input())
        number = Funtionalities.correct_values(1, 2, number)
        if number == 1:
            self.print_loans(self.generate_loans())
        elif number == 2:
            return False
