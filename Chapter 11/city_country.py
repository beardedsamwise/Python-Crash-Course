def city_country(city,country,population=""):
    if population:
        full_city = (city.title() + ", " + country.title() + ', ' + str(population))
        return full_city
    else:
        full_city = (city.title() + ", " + country.title())
        return full_city

