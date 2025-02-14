from utils.fuel import Fuel
from utils.init_config import config

class Gas(Fuel):

    def __init__(self, config: dict):
        super().__init__(config)



if __name__ == '__main__':
    gas1 = Gas(config)
    gas1.get_prices()
    print(gas1.average_price)



