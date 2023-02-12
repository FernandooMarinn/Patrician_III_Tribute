import time


class Achievements:
    """
    For saving the information about player achievements and Easter eggs inside the object player.
    """
    def __init__(self):
        self.player = 0

        self.half_million = False
        self.one_million = False

        self.all_cites = False
        self.visited_cities = []

        self.all_commercial_offices = False

        self.ten_ships = False
        self.ships = 0

        self.asked_ten_loans = False
        self.asked_loans = 0
        self.granted_ten_loans = False
        self.granted_loans = 0

        self.first_convoy = False

        self.five_factories = False
        self.twenty_factories = False
        self.factories = 0

        self.first_combat = False

        self.travels = 0
        self.travels_more_than_ten = False
        self.travels_more_than_fifty = False
        self.travels_more_than_hundred = False


    def coins_achievements(self):
        if self.player.coins >= 500_000 and not self.half_million:
            self.achiemevents_separation()
            print("Congratulations!! Your wealth is now 500_000 coins!")
            self.achiemevents_separation()
            self.half_million = True

        elif self.player.coins >= 1_000_000 and not self.one_million:
            self.achiemevents_separation()
            print("Congratulations!! You have arrived to 1.000.000 coins!")
            self.achiemevents_separation()
            self.one_million = True

    def response_to_names(self, name):
        if name.lower() == "fernandoomarinn":
            self.achiemevents_separation()
            print("You are lying! There's only one FernandooMarinn, and its not you!")
            self.achiemevents_separation()

        elif name.lower() == "fernando":
            self.achiemevents_separation()
            print("You have a beautiful name!")
            self.achiemevents_separation()

        elif name.lower() == "beneke":
            self.achiemevents_separation()
            print("Ohhh, I see that you are a fan of Patrician III!")
            self.achiemevents_separation()

    def visiting_city(self, city):
        if city not in self.visited_cities:
            self.visited_cities.append(city)

        if len(self.visited_cities) == 10:
            self.achiemevents_separation()
            print("You have visited all cities in the hanseatic league!")
            self.achiemevents_separation()

    def calculate_commercial_offices(self):
        if not self.all_commercial_offices:
            counter = 0
            for city in self.player.all_cities_list:
                if city.commercial_office != False:
                    counter += 1
            if counter == 10:
                self.achiemevents_separation()
                print("You have conquered all the hanseatic league! Congratulations on having commercial offices on all"
                      " the cities!")
            self.all_commercial_offices = True

    def achiemevents_separation(self):
        print("*" * 120)

    def increase_ship_number(self):
        self.ships += 1
        if self.ships == 10:
            self.achiemevents_separation()
            print("You have build ten ships! The ocean is waiting for you!")
            self.achiemevents_separation()

    def increase_loan_number(self, type):
        if type == "grant" and not self.granted_ten_loans:
            self.granted_loans += 1
            if self.granted_loans == 10:
                self.achiemevents_separation()
                print("You have granted ten loans. You are the master of investment!")
                self.achiemevents_separation()
                self.granted_ten_loans = True

        elif type == "ask" and not self.asked_ten_loans:
            self.asked_loans += 1
            if self.asked_loans == 10:
                self.achiemevents_separation()
                print("You are drowning in a sea of interest. You have asked for ten loans. Congratulations?")
                self.achiemevents_separation()
                self.asked_ten_loans = True

    def check_when_first_convoy(self):
        if not self.first_convoy:
            self.achiemevents_separation()
            print("You have created your first convoy! This opens a world of possibilities. Nicely done!")
            self.achiemevents_separation()
            self.first_convoy = True

    def build_factories(self, number):
        self.factories += number
        if self.factories >= 5 and not self.five_factories:
            self.achiemevents_separation()
            print("You have created five factories! You really are a business man!")
            self.achiemevents_separation()
            self.five_factories = True

        elif self.factories >= 20 and not self.twenty_factories:
            self.achiemevents_separation()
            print("You have made twenty factories! You are feeding lots of families that are grateful to you.")
            self.achiemevents_separation()
            self.twenty_factories = True

    def check_if_first_combat(self):
        if not self.first_combat:
            self.achiemevents_separation()
            print("You are about to get on you first fight! Good luck!")
            self.achiemevents_separation()
            time.sleep(2.5)
            self.first_combat = True

    def calculate_travels(self):
        self.travels += 1
        if self.travels >= 10 and not self.travels_more_than_ten:
            self.travels_more_than_ten = True
            self.achiemevents_separation()
            print("You have made 10 travels between cities!")
            self.achiemevents_separation()

        elif self.travels >= 50 and not self.travels_more_than_fifty:
            self.travels_more_than_fifty = True
            self.achiemevents_separation()
            print("You have made 50 travels between cities! You are such a sailor!")
            self.achiemevents_separation()

        elif self.travels >= 100 and not self.travels_more_than_hundred:
            self.travels_more_than_hundred = True
            self.achiemevents_separation()
            print("You have made 100 travels between cities! You are becoming the king of the seas.")
            self.achiemevents_separation()

