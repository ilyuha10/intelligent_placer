from intelligent_placer_lib.preproccesing import load_images
from intelligent_placer_lib.preproccesing import get_contours
from intelligent_placer_lib.spliter import split_contours
from intelligent_placer_lib.placer import place_objects
from shapely.geometry import Polygon
import cv2
from matplotlib import pyplot as plt
images, name = load_images("images/tests")
i=1
for im in images:
    plt.figure(i)
    plt.title(name[i-1])
    
    
    cnts = get_contours(im)
    poly, objects = split_contours(cnts)
    

    p1 = [tuple(p) for p in poly[:, 0]]
    pol = Polygon(p1)
    
    plt.plot(*pol.exterior.xy)
   
    objs = []
    for o in objects:
        o1 = [tuple(p) for p in o[:, 0]]
        obj = Polygon(o1)
        objs.append(obj)
  
        plt.plot(*obj.exterior.xy)
    res = place_objects(pol, objs)
    print( name[i-1], res)
    i+=1
  
        
    
plt.show()