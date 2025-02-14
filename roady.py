from utils.distance import Distance
from utils.gas import Gas
from utils.init_config import config


class Roady:

    def __init__(self, dist: Distance, gas_price: Gas):
        self.distance = dist
        self.gas = gas_price


    def calculate_price(self, persons: int, fuel_consumption: float,
                        with_return: bool = False, currency: str= "RON"):

        km = 2 * self.distance.km if with_return else self.distance.km
        price = self.gas.last_price if currency == "RON" else 0.2 * self.gas.last_price

        total_liters = km * fuel_consumption / 100
        total_price = price * total_liters

        return total_price / persons

if __name__ == '__main__':

    d1 = Distance("Bucuresti", "Bacau", config)
    gas1 = Gas(config)

    roady = Roady(d1, gas1)
    print(roady.calculate_price(2,10,True))

