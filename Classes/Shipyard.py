class Shipyard:
    def __init__(self, name):
        self.coins = 0
        self.level = 1
        self.experience = 0
        self.queue = []
        self.name = name

    def gain_experience(self, exp):
        self.experience += exp

    def level_up(self):
        if self.level < 5:
            if self.experience > 99:
                self.experience = 0
                self.level += 1

    def repair_convoy(self):
        pass

    def repair_boat(self):
        pass

    def show_menu(self):
        print("Under construction")
