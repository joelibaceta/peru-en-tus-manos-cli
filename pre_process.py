import json
import os

districts_file = open(os.getcwd() + "/data")
districts = json.load(districts_file)

print(districts['220910'])

# cities_file = open(os.getcwd() + "/ubigeo/provincias.json")
# cities = json.load(cities_file)
# states_file = open(os.getcwd() + "/ubigeo/departamentos.json")
# states = json.load(states_file)

# states_dic = {}
# cities_dic = {}
# districts_dic = {}

# for state in states:
#     states_dic[state["id"]] = {
#         "name": state["name"]
#     }


# for city in cities:
#     cities_dic[city["id"]] = {
#         "name": city["name"],
#         "state": states_dic[city["department_id"]]["name"]
#     }


# for district in districts:
#     districts_dic[district["id"]] = {
#         "name": district["name"],
#         "city": cities_dic[district["province_id"]]["name"],
#         "state": states_dic[district["department_id"]]["name"]
#     }

#     print(districts_dic)

# with open('data.json', 'w') as fp:
#     json.dump(districts_dic, fp)