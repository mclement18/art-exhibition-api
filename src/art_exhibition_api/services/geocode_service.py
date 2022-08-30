import requests


class GeocodeService:
    def __init__(self) -> None:
        self.api_url = 'https://geocoding.geo.census.gov/geocoder/locations/address'

    def call(self, street: str, city: str, state: str):
        print('geocoding')
        print(f"{street}, {city}, {state}")
        return self.__get_location(street, city, state)

    def __get_location(self, street: str, city: str, state: str):
        try:
            response = requests.get(self.api_url, self.__params(street, city, state))
            print('geocoded responded')
            print(response.text)
            coordinates = response.json().get('result').get('addressMatches')[0].get('coordinates')
            print('geocoded')
            return [coordinates.get('y'), coordinates.get('x')]
        except Exception as err:
            print('geocode error')
            print(err)
            return []
    
    def __params(self, street: str, city: str, state: str):
        return {'street': street, 'city': city, 'state': state, 'benchmark': 2020, 'format': 'json'}
