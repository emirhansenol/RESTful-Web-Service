import requests
import json

GEOCOD_IO_API_URL = "https://api.geocod.io/v1.7/geocode"
YELP_API_URL = "https://api.yelp.com/v3/businesses/search"


class GeocodioClient(object):
    """
    The client that makes request to the Geocodio
    to get the corresponding (latitude, longitude) pair.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = GEOCOD_IO_API_URL

    def request(self, addr):
        params = {"q": addr.replace(" ", "-"),
                  "api_key": self.api_key}

        response = requests.get(self.base_url, headers=None, params=params)

        if 400 <= response.status_code < 500:
            raise ValueError("Client Error {} - Please check the address you entered."
                             .format(response.status_code))
        elif 500 <= response.status_code < 600:
            raise ValueError("Server Error {} - Geocod.io server is experiencing an issue. Please try again later."
                             .format(response.status_code))
        elif response.ok:
            data = json.loads(response.content)

            latitude = data["results"][0]["location"]["lat"]
            longitude = data["results"][0]["location"]["lng"]

            return latitude, longitude
        else:
            response.raise_for_status()


class YelpClient(object):
    """
    The client that makes request to the Yelp
    to get a list of nearby restaurants.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = YELP_API_URL

    def request(self, latitude, longitude):
        headers = {"Authorization": "Bearer {}".format(self.api_key)}
        params = {"latitude": latitude,
                  "longitude": longitude,
                  "categories": "Food"}

        response = requests.get(self.base_url, headers=headers, params=params)

        if 400 <= response.status_code < 500:
            raise ValueError("Client Error {} - Please check the latitude and longitude values you entered."
                             .format(response.status_code))
        elif 500 <= response.status_code < 600:
            raise ValueError("Server Error {} - Yelp server is experiencing an issue. Please try again later."
                             .format(response.status_code))
        elif response.ok:
            data = json.loads(response.content)

            restaurants = []
            for business in data["businesses"]:
                restaurant = {"name": business["name"],
                              "address": business["location"]["address1"],
                              "rating": business["rating"]}
                restaurants.append(restaurant)

            return restaurants
        else:
            response.raise_for_status()
