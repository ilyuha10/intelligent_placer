
from intelligent_placer_lib.preproccesing import get_contours
from intelligent_placer_lib.spliter import split_contours
from intelligent_placer_lib.placer import place_objects
from intelligent_placer_lib.placer import distance

from intelligent_placer_lib.geometry import shift_geom_to_the_beginning, create_polygons
from shapely.geometry import Polygon

import cv2
from matplotlib import pyplot as plt

def check_image(image):
    cnts = get_contours(image)
    if len(cnts) == 0:
        return False, None, None
    poly_cnt, objects_cnts = split_contours(cnts)
    
    poly, objects = create_polygons(poly_cnt, objects_cnts)
    
    poly = shift_geom_to_the_beginning(poly)
    for k in range(len(objects)):
        objects[k] = shift_geom_to_the_beginning(objects[k])
        

    ans, res = place_objects(poly, objects)
           
        
    return ans, poly, res