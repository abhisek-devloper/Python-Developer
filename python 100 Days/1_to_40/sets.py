info = {"Carla", 19, False, 5.9, 19}
print(info)


info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}

print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))
print(cities2.issubset(cities))
cities.add("Helsinki")
print(cities)
cities.update(cities2)
print(cities)
cities.remove("Tokyo")
print(cities)

item = cities.pop()
print(cities)
print(item)

cities.clear() #clear set element
print(cities)

del cities #delete cities
# print(cities)