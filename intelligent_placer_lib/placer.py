from shapely.geometry import Polygon
def place_objects(poly, objects):

    return poly.area > sum([obj.area for obj in objects])