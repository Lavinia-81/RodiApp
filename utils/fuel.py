import requests
from bs4 import BeautifulSoup
from utils.init_config import config



class Fuel:

    def __init__(self, config: dict):
        self.config = config
        self.url = config.get("gas_url", None)
        self.last_price = ""
        self.prices = self.get_prices()

    @property
    def average_price(self):
        return sum(self.prices.values()) / len(self.prices.values())


    @staticmethod
    def get_html_from_website(url: str) -> str:

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return ""
        except Exception as e:
            print(f"Exception raised on get requests: {e}")
            return ""


    def get_prices(self):
        html_text = self.get_html_from_website(self.url)
        soup = BeautifulSoup(html_text, features="html.parser")
        locations = soup.find_all("div", {"class": "location"})
        locations = [item.text for item in locations]
        prices = soup.find_all(id="box_pret")
        self.last_price = float(prices[0].text.split(" ")[0])
        prices = [float(item.text.split(" ")[0]) for item in prices]
        prices_dict = dict(zip(locations, prices))

        return prices_dict


if __name__ == '__main__':
    fuel1 = Fuel(config)
    fuel1.get_prices()
    print(fuel1.last_prices, fuel1.average_price)
