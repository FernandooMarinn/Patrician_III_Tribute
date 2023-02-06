import Functionalities.Utilities

"""
Not so secret if you can read the code!
"""





def all_commercial_offices(cities):
    counter = 0
    for city in cities:
        if not city.commercial_office:
            pass
        else:
            counter += 1
    if counter == len(cities):
        print("Congratulations! You have build a commercial office in all the cities. You are great at this game!")


