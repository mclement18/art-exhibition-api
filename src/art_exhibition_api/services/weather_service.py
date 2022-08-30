import requests

class WeatherService:
    def __init__(self) -> None:
        self.api_url = 'https://api.weather.gov/points/'

    def call(self, exhibition):
        forcast_uri = self.__get_forcast_uri(exhibition)
        exhibition['forcast'] = self.__get_forecast(forcast_uri)
        return exhibition

    def __get_forcast_uri(self, exhibition):
        try:
            print('get forecast uri')
            response = requests.get(self.api_url + self.__get_location(exhibition))
            return response.json().get('properties').get('forecast')
        except Exception as err:
            print('forecast uri failed')
            print(err)
            return None

    def __get_location(self, exhibition):
        return ','.join([str(coordinate) for coordinate in exhibition['location']])

    def __get_forecast(self, uri):
        try:
            print('get forcast')
            response = requests.get(uri)
            return self.__parse_forcast(response.json().get('properties').get('periods'))
        except Exception as err:
            print('forcast error')
            print(err)
            return []

    def __parse_forcast(self, forcast):
        return [period for period in forcast if period['isDaytime']][0:2]
