from airport_api.api_route import AirportApi

airport_api = AirportApi()


def test_number_of_airports():
    default_airport_number = 30
    assert len(airport_api.get_airports()['data']) == default_airport_number, f'The number of airoports should be {default_airport_number}'


def test_airport_names():
    expected_airports = ['Akureyri Airport', 'St. Anthony Airport', 'CFB Bagotville']
    actual_airports = []
    all_airports = airport_api.get_airports()['data']

    for airport in all_airports:
        if airport['attributes']['name'] in expected_airports:
            actual_airports.append(airport['attributes']['name'])

    assert expected_airports == actual_airports, f'The actual {actual_airports} is different from expected {expected_airports}'


def test_airport_distance():
    expected_distance = 400
    actual_distance = airport_api.get_distance_between_airports(from_airport='KIX', to_airport='NRT')['data']['attributes']['kilometers']
    assert actual_distance > expected_distance, f'The expected distance {expected_distance} is smaller than actual distance {actual_distance}'
