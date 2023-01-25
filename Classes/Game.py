class Game:
    """
    Game is a class used to save and load different games. It stores cities and player, with every attribute inside
    them.
    """
    def __init__(self, player, cities):
        self.cities = cities
        self.player = player


