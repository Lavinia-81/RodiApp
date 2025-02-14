import requests
from bs4 import BeautifulSoup
from utils.init_config import config


class Distance:

    def __init__(self, departure_city: str, destination_city: str, config: dict):
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.config = config
        self.km = self.calculate_km()


    def get_html(self):
        url = self.config['distance_url'] + self.departure_city + "/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return ""
        except Exception as e:
            print(f"Probleme la request {e}")


    def calculate_km(self):
        html_text = self.get_html()
        soup = BeautifulSoup(html_text, feature="html.parser")
        distance = soup.find(string=self.destination_city).parent.parent

        for line in distance:
            if "km" in str(line).lower():
                return int(line.text.split(" ")[0])

        return ""



if __name__ == '__main__':
    d1 = Distance("Bucuresti", "Bacau", config)
    print(d1.km)

