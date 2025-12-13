from house import House
from flat import Flat

house = House(
    area=120,
    rooms=5,
    price=850000,
    address="Krakow, Grodzka 5",
    plot=600,
)

flat = Flat(
    area=55,
    rooms=2,
    price=420000,
    address="Krakow, Basztowa 12",
    floor=3,
)

print(house)
print("-" * 30)
print(flat)
