import csv
import json
from shapely.geometry.polygon import Polygon as ShapelyPolygon
from shapely.geometry import shape


def get_addresses():
    file_path = './BOSTON_MASTER.csv'
    with open(file_path) as csvfile:
        addresses = []
        readCSV = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(readCSV):
            if index > 0:
                address = row[0]
                addresses.append(address)
        return addresses

class Polygon:
    def __init__(self, sub_district, unique_code, coordinates, polygon_type):
        self.sub_district = sub_district
        self.unique_code = unique_code
        self.coordinates = coordinates
        self.type = polygon_type

    def to_shapely_polygon(self) -> ShapelyPolygon:
        return shape({
            'type': self.type,
            'coordinates': self.coordinates
        })
    
    def _adjust_coordinate(coordinate):
        return tuple(coordinate)


def get_polygons() -> list[Polygon]:
    with open('./BOSTON_SUBDISTRICTS.geojson') as geojson:
        data = json.load(geojson)
        polygons = []
        for feature in data["features"]:
            polygons.append(Polygon(
                feature['properties']['Zone_Desc'],
                feature['properties']['Unique_Code'],
                feature['geometry']['coordinates'],
                feature['geometry']['type']
            ))
        return polygons
            

        
