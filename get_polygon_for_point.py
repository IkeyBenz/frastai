from get_addresses import get_polygons

polygons = get_polygons()


sub_districts = {}
for p in polygons:
    sub_districts[p.unique_code] = p.sub_district

def get_subdistrict_from_unique_code(polygon_code):
    return sub_districts[polygon_code]


def get_polygon_for_point(point):
    for polygon in polygons:
        shapely_polygon = polygon.to_shapely_polygon()
        if shapely_polygon is None:
            return None
        
        if shapely_polygon.contains(point):
            return polygon.unique_code