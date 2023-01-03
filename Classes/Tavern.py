class Tavern:
    def __init__(self, city):
        super().__init__()
        self.city = city
        self.sailors = 12
        self.captain = False

    def calculate_sailors(self):
        if self.sailors < 20:
            self.sailors += 8
        elif self.sailors < 55:
            self.sailors += 4

    def change_turn(self):
        self.calculate_sailors()

    def add_captain(self):
        self.captain = True

    def show_menu(self):
        print("Under construction")

