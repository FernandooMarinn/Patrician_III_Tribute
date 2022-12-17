class Tavern:
    def __init__(self, city):
        super().__init__()
        self.city = city
        self.sailors = 0
        self.captain = False


    def calculate_sailors(self):
        if self.sailors < 20:
            self.sailors += 10
        elif self.sailors < 55:
            self.sailors += 4


    def change_turn(self):
        self.calculate_sailors()