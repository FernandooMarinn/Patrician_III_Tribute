class CommercialOffice:
    def __init__(self, city):
        self.city = city
        self.inventory = [0, 0, 0, 0, 0]
        self.trader = False
        self.warehouses = 0
        self.max_inventory_size = 500
        self.inventory_size = 0

    def set_max_inventory_size(self):
        self.inventory_size = 500 + self.warehouses * 2500

    def set_inventory_size(self):
        self.inventory_size = sum(self.inventory)

    def show_menu(self):
        print("Under construction")