import requests
import urllib
import json
from shapely.geometry import Point
import diskcache as dc
import os

def cached(fn):
    cache = dc.Cache('tmp')
    def call_fn(*args):
        key = hash(args)
        if key in cache:
            return cache[key]
        val = fn(*args)
        cache[key] = val
        return val
    return call_fn

# For google maps api
BASE_URL= "https://maps.googleapis.com/maps/api/geocode/json?"
AUTH_KEY = os.environ.get('GMAPS_AUTH_KEY')

@cached
def get_coordinates_for_address(address):
    print('getting coordinate for address', address);
    parameters = { "address": address, "key": AUTH_KEY }
    r = requests.get(f"{BASE_URL}{urllib.parse.urlencode(parameters)}")
    data = json.loads(r.content)

    if data.get('status') != 'ZERO_RESULTS':
        print('found results')
        return data.get('results')[0].get('geometry').get('location')

    print('DID NOT FIND RESULTS')



def saved_coordinate_for_address(address):
    with open('Address_Coordinates.json', 'w') as out:
        out

# def save_coordinate_for_address(address):
#     with open('coordinates_to_addresses')

def convert_coordinate_to_point(coordinate):
    return Point(coordinate['lng'], coordinate['lat'])