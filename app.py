import argparse

from flask import Flask, jsonify, request

from clients import GeocodioClient, YelpClient

GEOCOD_IO_API_KEY = "write_your_own_key"
YELP_API_KEY = "write_your_own_key"

DEFAULT_PORT = 5000

app = Flask(__name__)


@app.route('/restaurants', methods=['GET'])
@app.route('/restaurant/<restaurant_addr>', methods=['GET'])
def restaurants(restaurant_addr=None):
    if request.method == 'GET':

        if not restaurant_addr:
            # Get the address query parameter's value
            address = request.args.get('address')
            if not address:
                return jsonify({'error': 'Missing address parameter.'}), 400
            restaurant_addr = address

        # Create clients to call corresponding webservices
        geocodio_client = GeocodioClient(GEOCOD_IO_API_KEY)
        yelp_client = YelpClient(YELP_API_KEY)

        # Get the latitude and longitude of the given address using Geocodio API
        latitude, longitude = geocodio_client.request(restaurant_addr)
        if not latitude or not longitude:
            return jsonify({'error': 'Unable to get latitude and longitude of the address.'}), 400

        # Get the nearby restaurants using Yelp API
        nearby_restaurants = yelp_client.request(latitude, longitude)

        return jsonify({'restaurants': nearby_restaurants})
    else:
        return jsonify({'error': 'Invalid request method.'}), 405


##########################
# Do **NOT** remove this.
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=DEFAULT_PORT, help='port number.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    app.run(port=args.port)
