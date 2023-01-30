import Functionalities.Utilities

"""
Not so secret if you can read the code!
"""


def one_million(money):
    if money >= 1_000_000:
        Functionalities.Utilities.text_separation()
        print("Congratulations!! You have arrived to 1.000.000 coins!")
        Functionalities.Utilities.text_separation()


def response_to_names(name):
    if name.lower() == "fernandoomarinn":
        Functionalities.Utilities.text_separation()
        print("You are lying! There's only one FernandooMarinn, and its not you!")
        Functionalities.Utilities.text_separation()
    elif name.lower() == "fernando":
        Functionalities.Utilities.text_separation()
        print("You have a beautiful name!")
        Functionalities.Utilities.text_separation()
    elif name.lower() == "beneke":
        Functionalities.Utilities.text_separation()
        print("Ohhh, I see that you are a fan of Patrician III!")
        Functionalities.Utilities.text_separation()


def all_commercial_offices(cities):
    counter = 0
    for city in cities:
        if not city.commercial_office:
            pass
        else:
            counter += 1
    if counter == len(cities):
        print("Congratulations! You have build a commercial office in all the cities. You are great at this game!")



