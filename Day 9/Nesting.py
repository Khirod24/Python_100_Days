#Nesting Dictionary and List inside a Dictionary

travel_log = {
    "France" : {"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany" : {"cities_visited":["Berlin","Numburg","Stuttgart"], "total_visits":5}
}
print(travel_log)
print(travel_log["France"])
print(travel_log["Germany"])
print(travel_log["Germany"]["cities_visited"])

#Nesting a Dictionary inside List
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

print(travel_log)
print(travel_log[0])
print(travel_log[1])
print(travel_log[0]["country"])