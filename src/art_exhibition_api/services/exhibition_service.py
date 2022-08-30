import requests

from art_exhibition_api.services.geocode_service import GeocodeService

class ExhibitionService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.api_url = 'https://api.harvardartmuseums.org/exhibition'
        self.geocoding_service = GeocodeService()
    
    def call(self):
        self.__get_exhibitions()
        print('parsing exhibitions')
        self.exhibitions = [self.__parse_exhibitions(exhibition) for exhibition in self.exhibitions]
        return self.exhibitions

    def __get_exhibitions(self):
        try:
            print('getting exhibitions')
            result = requests.get(self.api_url, self.__params())
            self.exhibitions = result.json().get('records')
            print('got exhibitions')
        except:
            self.exhibitions = []

    def __params(self):
        return {'apikey': self.api_key, 'status': 'current', 'size': 100}

    def __parse_exhibitions(self, exhibition):
        print('parsing an exhibition')
        exhibition = self.__keep_first_venue(exhibition)
        exhibition = self.__set_locations(exhibition)
        return exhibition

    def __keep_first_venue(self, exhibition):
        print('setting venue')
        exhibition['venue'] = exhibition['venues'][0]
        del exhibition['venues']
        return exhibition

    def __set_locations(self, exhibition):
        print('setting location')
        if self.__can_set_location(exhibition):
            print('can set location')
            venue = exhibition['venue']
            exhibition['location'] = self.geocoding_service.call(venue['address1'], venue['city'], venue['state'])

        return exhibition

    def __can_set_location(self, exhibition):
        venue = exhibition['venue']
        return venue.get('city') is not None and venue.get('address1') is not None and venue.get('state') is not None
