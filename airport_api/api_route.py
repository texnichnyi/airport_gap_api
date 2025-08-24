import requests


class AirportApi:
    base_route = "https://airportgap.com/api/airports"

    def get_airports(self):
        return requests.get(self.base_route).json()

    def get_distance_between_airports(self, from_airport, to_airport):
        distance_data = {'from': from_airport, 'to': to_airport}
        return requests.post(f'{self.base_route}/distance', distance_data).json()
