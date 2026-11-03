import Property


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nRozmiar działki {self.plot} m^2"
            )
