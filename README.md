# RESTful Web Service

A simple Web Service developed using Flask that will take an address and respond with info of nearby restaurants.

The web service then takes HTTP requests with address parameters and responds with a list of popular restaurants nearby.

The following two APIs are used to accomplish this task.

<img width="419" alt="image" src="https://user-images.githubusercontent.com/107651391/226203707-e4a8f878-f349-4bc8-b52f-9a24fb7ca02f.png">

- Learn more about the Geocod.io and get your API key - https://www.geocod.io/
- Learn more about API Authorization and getting your API key - https://www.yelp.com/developers/documentation/v3/authentication

## The Client

The Client defines two classes, GeocodioClient and YelpClient, that allow a user to make requests to the `Geocodio API` and the `Yelp API` respectively. Overall, it provides a simple way for a user to retrieve the latitude and longitude of an address, and to find nearby restaurants based on a location.

The **GeocodioClient** class has an __init__ method that initializes the client with an api_key parameter, which is used in the subsequent requests to the Geocodio API. The request method takes an addr parameter, which represents the address that the user wants to get the corresponding latitude and longitude pair for. The method sends a GET request to the Geocodio API with the addr parameter and the api_key parameter in the query string. It then parses the response to extract the latitude and longitude values for the address and returns them as a tuple.

The **YelpClient** class has a similar structure. Its __init__ method initializes the client with an api_key parameter, which is used in the subsequent requests to the Yelp API. The request method takes latitude and longitude parameters, which represent the latitude and longitude of a location. The method sends a GET request to the Yelp API with the latitude, longitude, and categories parameters in the query string, as well as an Authorization header containing the api_key. It then parses the response to extract a list of nearby restaurants and returns them as a list of dictionaries containing the restaurant name, address, and rating.

## The Server

The Server creates a web service using **Flask**, which has two REST endpoints:

`/restaurants` - This endpoint is used to get a list of nearby restaurants given an address. It accepts GET requests and expects an address query parameter to be provided. If the parameter is not provided, it returns an error response. The endpoint uses the GeocodioClient and YelpClient classes to call the corresponding web services, which provide the latitude and longitude of the given address and nearby restaurants, respectively.

`/restaurant/<restaurant_addr>` - This endpoint is similar to the /restaurants endpoint but allows the address to be provided as part of the URL path instead of a query parameter.

The web service is configured to run on `port 5000` by default but can be configured to run on a different port using the --port command-line argument.

The server code imports the `argparse` module to parse command-line arguments, the `Flask` module to create and configure the web service, the `jsonify` and `requests` modules to handle HTTP requests and responses, and the GeocodioClient and YelpClient classes to call the corresponding web services. 

The `GEOCOD_IO_API_KEY` and `YELP_API_KEY` variables contain the API keys needed to authenticate with the web services.

### Short description on the libraries/packages used:

**argparse**: A library in Python2 that provides an easy and efficient way to create command-line interfaces for Python programs. It allows to define the arguments that the program should accept and generates the help and usage messages for the program automatically. This library can be used to create professional-looking command-line interfaces for Python programs quickly and easily.

**Flask**: Flask is a lightweight web application framework for Python2 that is designed to be easy to use and to get started with. It provides tools and libraries for building web applications, including URL routing, templating, and handling HTTP requests and responses. Flask is widely used for building web applications and APIs, and it is known for its simplicity and flexibility.

**jsonify**: The jsonify library in Python2 is used to create JSON responses in web applications. JSON is a common data format used for sending and receiving data between web applications, and the jsonify library provides an easy way to create JSON responses from Python data structures. It automatically handles the conversion of Python objects to JSON format, and it can be used in conjunction with other web frameworks like Flask to create powerful web applications and APIs.

**requests**: The requests library in Python2 is used to make HTTP requests from Python code. It provides a simple and intuitive API for sending HTTP requests and handling responses, including support for authentication, cookies, and custom headers. The requests library is widely used in web scraping, testing, and building web applications and APIs. It simplifies the process of making HTTP requests and handling responses in Python, making it a valuable tool for web developers or data scientists.

## Architecture and Flow

<img width="500" alt="image" src="https://user-images.githubusercontent.com/107651391/226203843-86c4220a-dfca-4f0e-93e1-c348f94ebf13.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/107651391/226203867-2d2a7494-af1a-49d6-b025-064e51165640.png">

## JSON response formatJSON response format

<img width="500" alt="image" src="https://user-images.githubusercontent.com/107651391/226204116-96661d18-6e3f-4f8e-8e14-dfec7be097cd.png">

## How to start the web service?

- To run the `app.py` on **Pycharm**, first, you need to install the following packages:
- `Flask`
- `argparse`
- `requests`

<img width="745" alt="image" src="https://user-images.githubusercontent.com/107651391/226204605-48e4c025-4d0a-4d9f-bab1-b7e9b7240b55.png">

- To start the web service, use the following command on a Terminal CLI window (--port is optional, though):
`python app.py --port 5000`

- To test the **/restaurant** endpoint via a browser:
`http://127.0.0.1:5000/restaurant/<write_a_full_address>`

- To test the **/restaurants** endpoint via a browser:
`http://127.0.0.1:5000/restaurants?address=<write_a_full_address>`
