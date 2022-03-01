# Before anything, ensure environment variables are loaded
from dotenv import load_dotenv
load_dotenv()

from get_addresses import get_addresses
from get_coordinates_for_address import get_coordinates_for_address, convert_coordinate_to_point
from get_polygon_for_point import get_polygon_for_point, get_subdistrict_from_unique_code
# Read in the addresses
addresses = get_addresses()

for address in addresses[:5]:
    coordinate = get_coordinates_for_address(address)
    shapely_point = convert_coordinate_to_point(coordinate)
    polygon_unique_code = get_polygon_for_point(shapely_point)
    sub_district = get_subdistrict_from_unique_code(polygon_unique_code)



# We first want to get the coordinates of each address
# coordinates = list(map(addresses, get_coordinates_for_address))


# Match each point to given polygons

# Create GeoJSON file including polygons with their respective points within