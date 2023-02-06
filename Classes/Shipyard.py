import Functionalities.Utilities
import Classes.Boats_and_Convoys


class Shipyard:
    def __init__(self, city):
        self.coins = 0
        self.level = 1
        self.experience = 0
        self.building_queue = []
        self.reparation_queue = []
        self.city = city

        self.repair_speed = 20
        self.build_speed = 6

    def gain_experience(self, exp):
        self.experience += exp

    def level_up(self):
        if self.level < 5:
            if self.experience > 10_000:
                self.experience = 0
                self.level += 1
                self.set_speed()

    def set_speed(self):
        """
        Set speed depending on level.
        :return:
        """
        if self.level == 1:
            self.repair_speed = 20
            self.build_speed = 6
        elif self.level == 2:
            self.repair_speed = 25
            self.build_speed = 5
        elif self.level == 3:
            self.repair_speed = 30
            self.build_speed = 5
        elif self.level == 4:
            self.repair_speed = 40
            self.build_speed = 4

    def check_if_convoy(self, unit):
        """
        return true if unit is a convoy.
        :param unit:
        :return:
        """
        if unit.is_convoy:
            return True
        else:
            return False

    def repair_convoy(self, convoy):
        """
        Calculates time and coins to repair a whole convoy.
        :param convoy:
        :return:
        """
        convoy.set_all_health()

        total_cost = 0
        number_of_turns = 1 + round((110 - convoy.min_health) / self.repair_speed)

        for boat in convoy.boats:
            total_cost += (boat.max_health - boat.health) * 100
        print("Do you want to repair your convoy {}? It will take {} turns and cost {} coins."
              .format(convoy.name, number_of_turns, total_cost))
        option = input("1- Yes.\n"
                       "2- No.\n")
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if option == 1:
            if Functionalities.Utilities.money_exchange(convoy.player, self, total_cost):
                self.reparation_queue.append([convoy, number_of_turns])
                self.city.player.convoys.remove(convoy)
                self.city.convoys.remove(convoy)
                self.gain_experience(total_cost)

    def repair_boat(self, boat):
        """
        Calculate time and coins to repair a single ship.
        :param boat:
        :return:
        """
        number_of_turns = 1 + round((boat.max_health - boat.health) / self.repair_speed)
        price = (boat.max_health - boat.health) * 100
        confirmation = input("Do you want to repair your ship {}? It will take {} turns and cost {} coins.\n"
                             "1- Yes.\n"
                             "2- No. \n"
                             .format(boat.name, number_of_turns, price))
        confirmation = Functionalities.Utilities.correct_values(1, 2, confirmation)
        if confirmation == 1:
            if self.city.player.coins >= price:
                self.city.player.coins -= price
                self.reparation_queue.append([boat, number_of_turns])
                self.city.player.boats.remove(boat)
                self.city.boats.remove(boat)
                self.gain_experience(price)
            else:
                print("You cannot afford the reparation.\n")

    def show_menu(self):
        """
        Prints ship menu.
        :return:
        """
        while True:
            print("What do you want to do?\n\n"
                  "1- Repair boat or convoy.\n"
                  "2- Improve ship.\n"
                  "3- Build new ship.\n"
                  "4- Check reparation queue.\n"
                  "5- Check build queue.\n"
                  "6- Change name (ship).\n"
                  "7- Exit.\n")
            option = input()
            option = Functionalities.Utilities.correct_values(1, 7, option)
            if option == 7:
                break
            else:
                self.choose_option(option)

    def choose_option(self, option):
        """
        Select option from menu.
        :param option:
        :return:
        """
        if option == 1 or option == 2:
            self.repair_or_improve(option)
        elif option == 3:
            self.building_menu()
        elif option == 4:
            self.check_repairing_boats()
        elif option == 5:
            self.check_building_boats()
        elif option == 6:
            self.change_name()

    def repair_or_improve(self, option):
        """
        Check if possible to improve/repair unit.
        :param option:
        :return:
        """
        type = input("Do you want to select a ship or a convoy?\n"
                     "1- Ship.\n"
                     "2- Convoy.\n"
                     "3- Exit.\n")
        type = Functionalities.Utilities.correct_values(1, 3, type)
        if type == 1:
            unit_to_select = Functionalities.Utilities.choose_boat(self.city)
        elif type == 2:
            unit_to_select = Functionalities.Utilities.choose_convoy(self.city)
        else:
            pass
        if option == 1:
            if not unit_to_select:
                print("There is no unit to select")
            elif not unit_to_select.is_convoy:
                self.repair_boat(unit_to_select)
            elif unit_to_select.is_convoy:
                self.repair_convoy(unit_to_select)
        elif option == 2:
            if not unit_to_select:
                print("There is no unit to select")
            elif not unit_to_select.is_convoy:
                self.ask_if_improve_boat(unit_to_select)
            elif unit_to_select.is_convoy:
                self.improve_convoy(unit_to_select)

    def change_name(self):
        """
        Changes name to a ship.
        :return:
        """
        ship = Functionalities.Utilities.choose_boat_from_city(self.city)
        if not ship:
            print("You don`t have any ships in {}".format(self.city.name))
        name = input("What are you thinking of naming your boat")
        ship.name = name

    def building_menu(self):
        """
        Check if want to build a ship.
        :return:
        """
        print("Do you want to build a new ship? It cost 10.000 coins.\n"
              "1- Yes.\n"
              "2- No.\n")
        option = input()
        option = Functionalities.Utilities.correct_values(1, 2, option)
        if option == 1:
            if self.city.player.coins >= 10_000:
                self.build_ship()
                self.city.player.coins -= 10_000
                self.gain_experience(10_000)
            else:
                print("You can´t afford a ship.")

    def build_ship(self):
        """
        Ask name for a new ship, and creates it.
        :return:
        """
        name = input("Witch name do you choose for your ship?")
        new_boat = Classes.Boats_and_Convoys.Boat(100, 1, [0, 0, 0, 0, 0, 0], 0, False, 0, name,
                                                  self.city, self.city.player)
        total_remaining_turns = self.calculate_remaining_turns()
        self.building_queue.append([new_boat, self.build_speed + total_remaining_turns])
        print("Your ship {} will be ready in {} turns.".format(new_boat.name, self.build_speed))

    def check_building_boats(self):
        """
        Shows every ship being build.
        :return:
        """
        for order in self.building_queue:
            boat = order[0]
            turns_remaining = order[1]
            print("{} is under construction. It will be ready in {} turns."
                  .format(boat.name, turns_remaining))

    def building_boats(self):
        """
        Decrease number of turns remaining for building each ship.
        :return:
        """
        boats_to_delete = []
        for boat in self.building_queue:
            ship = boat[0]
            remaining_turns = boat[1]
            if remaining_turns == 1:
                Functionalities.Utilities.text_separation()
                print("Your ship {} has been completed in {}".format(ship.name, self.city.name))
                Functionalities.Utilities.text_separation()
                self.city.player.boats.append(ship)
                self.city.boats.append(ship)
                boats_to_delete.append(boat)
                self.city.player.achievements.increase_ship_number()
            else:
                boat[1] -= 1
        for to_be_deleted in boats_to_delete:
            self.building_queue.remove(to_be_deleted)

    def repairing_boats(self):
        """
        Decrease number of turns remaining for repairing each ship.
        :return:
        """
        to_delete_list = []
        for repairing_unit in self.reparation_queue:
            remaining_turns = repairing_unit[1]
            unit = repairing_unit[0]
            if remaining_turns == 1:
                if unit.is_convoy:
                    self.finish_repairing_convoys(unit)
                else:
                    self.finish_repairing_boats(unit)
                to_delete_list.append(repairing_unit)
            else:
                repairing_unit[1] -= 1
        for item in to_delete_list:
            self.reparation_queue.remove(item)

    def finish_repairing_boats(self, boat):
        """
        Finish repair and prints a notification.
        :param boat:
        :return:
        """
        boat.health = boat.max_health
        self.city.player.boats.append(boat)
        self.city.boats.append(boat)
        print("Your ship {} has been repaired in {}.".format(boat.name, self.city.name))

    def finish_repairing_convoys(self, convoy):
        """
        Finish repair of a convoy.
        :param convoy:
        :return:
        """
        for boat in convoy.boats:
            boat.health = boat.max_health
        self.city.player.convoys.append(convoy)
        self.city.convoys.append(convoy)
        print("Your convoy {} has been repaired in {}.".format(convoy.name, self.city.name))

    def check_repairing_boats(self):
        """
        Check queue of repairing ships.
        :return:
        """
        Functionalities.Utilities.text_separation()
        for repairing_unit in self.reparation_queue:
            boat = repairing_unit[0]
            turns_remaining = repairing_unit[1]
            print("{}, {} turns remaining.".format(boat.name, turns_remaining))
        Functionalities.Utilities.text_separation()

    def ask_if_improve_boat(self, unit):
        """
        Check if want to improve ship.
        :param unit:
        :return:
        """
        if unit.level == 3:
            print("Your boat is already at its maximum level.")
        else:
            print("Your boat is currently at level {}.\n"
                  "What do you want to do?\n"
                  "1- Improve ship.\n"
                  "2- Exit.\n".format(unit.level))
            option = input()
            option = Functionalities.Utilities.correct_values(1, 2, option)
            if option == 2:
                pass
            else:
                self.improve_boat(unit)

    def improve_boat(self, boat):
        """
        Improve each ship to selected level.
        :param boat:
        :return:
        """
        if boat.level == 1:
            option = input("How do you want to improve your ship?\n"
                           "1- To level 2. (3000 coins and 3 turns)\n"
                           "2- To level 3. (6000 coins and 6 turns)\n")
            option = Functionalities.Utilities.correct_values(1, 2, option)
            if self.city.player.coins >= 3000 * option:
                boat.level = option + 1
                self.city.player.boats.remove(boat)
                self.city.boats.remove(boat)
                self.reparation_queue.append([boat, 3 * option])
                print("Your boat {} will be ready in {} turns.\n"
                      .format(boat.name, option * 3))
            else:
                print("You can´t afford to improve your ship.\n")

    def calculate_remaining_turns(self):
        counter = 0
        for ship in self.building_queue:
            counter += ship[1]
        return counter

    def improve_convoy(self, convoy):
        print("Ir order to improve a ship, it has to be out of a convoy.")

    def change_turn(self):
        """
        Everytime a turn changes.
        :return:
        """
        self.level_up()
        self.building_boats()
        if len(self.reparation_queue) > 0:
            self.repairing_boats()
