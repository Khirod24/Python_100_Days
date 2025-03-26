travel_log = [
    {
     "country":"France",
     "cities_visited":["Paris","Lille","Dijon"],
     "total_visits":12
    },
    {
     "country":"Germany",
     "cities_visited":["Berlin","Numburg","Stuttgart"],
     "total_visits":5
    }
]

def add_new_country(country, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["total_visits"] = times_visited
    new_country["cities_visited"] = cities_visited

    travel_log.append(new_country)

add_new_country("India",10,["Mumbai","Delhi","Noida"])
print(travel_log)