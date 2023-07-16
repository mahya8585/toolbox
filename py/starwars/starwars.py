import swapi

# swapiを使ってすべての人物情報を取得する
# people = swapi.get_all("people")

# 1人分の情報を取得する
yoda = swapi.get_person(20)
print(yoda.get_homeworld.name)

# 惑星情報をすべて取得する
planets = swapi.get_all("planets")

# ルーク・スカイウォーカーが乗ったことある乗り物の情報を取得する
luke = swapi.get_person(1)
luke_vehicles = luke.get_vehicles()
for vehicle in luke_vehicles.items:
    print(vehicle.name)