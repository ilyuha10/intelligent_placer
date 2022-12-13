from intelligent_placer_lib.preproccesing import load_images
from intelligent_placer_lib.preproccesing import get_contours
from intelligent_placer_lib.spliter import split_contours
from intelligent_placer_lib.placer import place_objects
from intelligent_placer_lib.placer import distance
from intelligent_placer_lib.spliter import norm
from intelligent_placer_lib.spliter import shift_geom
from shapely.geometry import Polygon
from shapely import affinity
from shapely.ops import snap
import cv2
from matplotlib import pyplot as plt


    


images, name = load_images("images/tests")
i=1
j = 0
for im in images:
    if name[i-1] != '2.jpg':
        i+=1 
        continue
    
    plt.figure(i)
    plt.title(name[i-1])
    
    print(i)
    cnts = get_contours(im)
    poly, objects = split_contours(cnts)
    

    p1 = [tuple(p) for p in poly[:, 0]]
    pol = Polygon(p1)
    
    #pol = pol.simplify(0.2)
   
    objs = []
    for o in objects:
        o1 = [tuple(p) for p in o[:, 0]]
        obj = Polygon(o1)
        objs.append(obj)
    objects = sorted(objs, key=lambda x: x.area, reverse=True)
        #plt.plot(*obj.exterior.xy)
    #res = place_objects(pol, objs)
   # print( name[i-1], res)
    i+=1
    
    pol2 = norm(pol)
    
    pol2 = pol2.simplify(5)
    for k in range(len(objs)):
        objs[k] = norm(objs[k])
        objs[k] = objs[k].simplify(3)
    x, y = pol2.exterior.xy
    print(len(x))
    #plt.plot(*o.exterior.xy)
    #pol3 = pol2.difference(o)
    #for g in pol3:
    #plt.plot(*pol2.exterior.xy)
    flag = True
    count = 0
    #res = snap(pol2, o, 0.5)
    print(i)
    ''' while pol2.union(o).area > pol2.area:
        o = shift_geom(o, -1, -1)
        angle = 5
        while pol2.union(o).area > pol2.area and angle<=360:
            o = affinity.rotate(o, angle)
            angle+=5
        count+=1
        if count>500:
            flag = False
            break'''
    res = o
    dist = 1000
    
    '''while count < 300:
        count+=1
        o = shift_geom(o, -1, -1)
        angle = 0
        while angle<=360:
            o = affinity.rotate(o, angle)
            angle+=5
            r = distance(pol2, o)
            
            if r < dist and pol2.union(o).area == pol2.area:
                res = o
                dist = r
        '''
       
    if flag:
        plt.plot(*pol2.exterior.xy)
        
        res = place_objects(pol2, objs)
        for r in res:
            plt.plot(*r.exterior.xy)
            
      
        #print(*pol2.exterior.xy)
        #print(*o.exterior.xy)
plt.show()