from property import Property


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House:\n"
            f"  Area: {self.area} m2\n"
            f"  Rooms: {self.rooms}\n"
            f"  Price: {self.price} PLN\n"
            f"  Address: {self.address}\n"
            f"  Plot size: {self.plot} m2"
        )