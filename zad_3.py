class Property:
    def __init__(self, area: str, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Powierzchnia nieruchomosci {self.area} m^2"
            f"\nLiczba pokoi {self.rooms}"
            f"\nCena {self.price}"
            f"\nAdres {self.address}"
            )


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nRozmiar działki {self.plot} m^2"
            )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nPietro {self.floor}"
            )


flat_1 = Flat(54.5, 3, 450000.0, "ul. Piotrkowska 12/4, Łódź", 2)
house_1 = House(120.0, 5, 850000.0, "ul. Słoneczna 15, Poznań", 600)

print(flat_1)
print("====================================================================")
print(house_1)
