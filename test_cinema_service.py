import requests


def test_get_all_cinemas(url: str):
    res = requests.get(url).json()
    assert (res == [
        {
            "cinemas_id": 1,
            "name": "KinoMax",
            "description": "47",
            "visitors": "1 billion",
            "address": "123 Main Street"
        },
        {
            "cinemas_id": 2,
            "name": "Cineplex",
            "description": "47",
            "visitors": "1 billion",
            "address": "456 Elm Street"
        },
        {
            "cinemas_id": 3,
            "name": "SilverScreen",
            "description": "47",
            "visitors": "1 billion",
            "address": "789 Oak Avenue"
        },
        {
            "cinemas_id": 4,
            "name": "StarCinema",
            "description": "47",
            "visitors": "1 billion",
            "address": "1010 Maple Drive"
        },
        {
            "cinemas_id": 5,
            "name": "GoldenTheater",
            "description": "47",
            "visitors": "1 billion",
            "address": "1212 Pine Lane"
        }
    ])


def test_get_cinema_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {
            "cinemas_id": 1,
            "name": "KinoMax",
            "description": "47",
            "visitors": "1 billion",
            "address": "123 Main Street"
        })


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/cinemas/'
    test_get_cinema_by_id(URL + '1')
    test_get_all_cinemas(URL)
