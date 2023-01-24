
def update_player(saved_player, current_player):
    current_player.name = saved_player.name
    current_player.coins = saved_player.coins
    current_player.level = saved_player.level
    current_player.city = saved_player.city
    current_player.experience = saved_player.experience
    current_player.boats = saved_player.boats
    current_player.convoys = saved_player.convoys
    current_player.turn = saved_player.turn
    current_player.all_cities_list = saved_player.all_cities_list

    current_player.number_of_offices = saved_player.number_of_offices
    current_player.can_build_offices = saved_player.can_build_offices
    current_player.bill = saved_player.bill




def update_cities(saved_cities, current_cities):
    for i in range(len(saved_cities)):
        current_cities[i].coins = saved_cities[i].coins
        current_cities[i].skins = saved_cities[i].skins
        current_cities[i].tools = saved_cities[i].tools
        current_cities[i].beer = saved_cities[i].beer
        current_cities[i].wine = saved_cities[i].wine
        current_cities[i].cloth = saved_cities[i].cloth
        current_cities[i].name = saved_cities[i].name

        current_cities[i].skins_consumption_ratio = saved_cities[i].skins_consumption_ratio
        current_cities[i].tools_consumption_ratio = saved_cities[i].tools_consumption_ratio
        current_cities[i].beer_consumption_ratio = saved_cities[i].beer_consumption_ratio
        current_cities[i].wine_consumption_ratio = saved_cities[i].wine_consumption_ratio
        current_cities[i].cloth_consumption_ratio = saved_cities[i].cloth_consumption_ratio

        current_cities[i].skins_consumption = saved_cities[i].skins_consumption
        current_cities[i].tools_consumption = saved_cities[i].tools_consumption
        current_cities[i].beer_consumption = saved_cities[i].beer_consumption
        current_cities[i].wine_consumption = saved_cities[i].wine_consumption
        current_cities[i].cloth_consumption = saved_cities[i].cloth_consumption

        current_cities[i].skins_production = saved_cities[i].skins_production
        current_cities[i].tools_production = saved_cities[i].tools_production
        current_cities[i].beer_production = saved_cities[i].beer_production
        current_cities[i].wine_production = saved_cities[i].wine_production
        current_cities[i].cloth_production = saved_cities[i].cloth_production

        current_cities[i].skins_factories = saved_cities[i].skins_factories
        current_cities[i].tools_factories = saved_cities[i].tools_factories
        current_cities[i].beer_factories = saved_cities[i].beer_factories
        current_cities[i].wine_factories = saved_cities[i].wine_factories
        current_cities[i].cloth_factories = saved_cities[i].cloth_factories

        current_cities[i].can_produce_skins = saved_cities[i].can_produce_skins
        current_cities[i].can_produce_tools = saved_cities[i].can_produce_tools
        current_cities[i].can_produce_beer = saved_cities[i].can_produce_beer
        current_cities[i].can_produce_wine = saved_cities[i].can_produce_wine
        current_cities[i].can_produce_cloth = saved_cities[i].can_produce_cloth

        current_cities[i].price_skins = saved_cities[i].price_skins
        current_cities[i].price_tools = saved_cities[i].price_tools
        current_cities[i].price_beer = saved_cities[i].price_beer
        current_cities[i].price_wine = saved_cities[i].price_wine
        current_cities[i].price_cloth = saved_cities[i].price_cloth
        current_cities[i].houses = saved_cities[i].houses
        current_cities[i].population = saved_cities[i].population

        current_cities[i].commercial_office = saved_cities[i].commercial_office
        current_cities[i].have_commercial_office = saved_cities[i].have_commercial_office
        current_cities[i].money_lender = saved_cities[i].money_lender
        current_cities[i].shipyard = saved_cities[i].shipyard
        current_cities[i].tavern = saved_cities[i].tavern
        current_cities[i].weapon_master = saved_cities[i].weapon_master
        current_cities[i].possition = saved_cities[i].possition

        current_cities[i].boats = saved_cities[i].boats
        current_cities[i].convoys = saved_cities[i].convoys
        current_cities[i].player = saved_cities[i].player
        current_cities[i].tavern = saved_cities[i].tavern

        current_cities[i].construction_queue = saved_cities[i].construction_queue
