from shapely.geometry import Polygon, MultiPolygon, Point, box, LineString, MultiLineString
from scipy.spatial.distance import euclidean
import math
from math import sqrt
import scipy.optimize
from intelligent_placer_lib.spliter import shift_geom
import numpy as np
from shapely import affinity
from sko.GA import GA
from matplotlib import pyplot as plt
con = 0
def calc_phi(x1, y1, x2, y2):
    print(x1, y1, x2, y2)
    t = x1*x2 + y1*y2
    t1 = sqrt(x1*x1 + y1*y1) * sqrt(x2*x2 + y2*y2)
    print(t, t1)
    
    return math.acos(t/t1)

def try_to_place(poly, obj):
    
    if poly.wkt.find("MULTIPOLYGON") > -1:
        a = []
        for o1 in poly:
            if o1.area > poly.area:
                a.extend(list(zip(*o1.exterior.xy)))
    else: 
        a = list(zip(*poly.exterior.xy))
    
    min_dist = 100000
    a = a[:-1]
    res = None
    j = 0
    phi = calc_phi(*a[-1], *a[0]) 
    bb = box(*obj.bounds).exterior.xy
    bbb = list(zip(*bb))[:-1]
    print(bbb)
    phi1 = calc_phi(*bbb[-1],*bbb[0])
    o = affinity.rotate(obj, (phi - phi1)* 57.2958)
    plt.plot(*poly.exterior.xy)
    plt.plot(*o.exterior.xy)
    for i in range(-1, len(a)-1):

        phi = calc_phi(*a[i], *a[i+1]) * 57.2958
        
        for alpha in range(0, 89, 90): 
            phi+=alpha
            
            o = affinity.rotate(o, phi)
            b = list(zip(*o.exterior.xy))
            for x,y in b:
                shift_x = a[i+1][0] - x
                shift_y = a[i+1][1] - y
                o1 = shift_geom(o, shift_x, shift_y)
                dist = distance(poly, o1)
                '''if(i == -1 and j == 7):
                    plt.plot(*poly.exterior.xy)
                    plt.plot(*o1.exterior.xy)
                '''
                if min_dist>dist:
                    min_dist = dist
                    res = o
                j+=1
    plt.show()
    return min_dist<0, res
def place_objects(poly, objects, count):
    def _objective_function(args):
        angle, shift_X, shift_y = args
        o = affinity.rotate(shift_geom(obj, shift_X, shift_y), angle)
        
        return distance(poly, o, count) 
    m1, m2, m3, m4 = poly.bounds
    ret = []
    o = None
    for i, obj in enumerate(objects):
        my_try= False
        k = i
        if not my_try:
            
            res = scipy.optimize.direct(_objective_function, bounds=((0,360), (0, m3), (0,m4)), eps = 0.01)
            if res.fun < 1000000:
                angle, shift_X, shift_y = res.x
                o = affinity.rotate(shift_geom(obj, shift_X, shift_y), angle)
                if poly.union(o).area - poly.area < 50:
                    ret.append(o)
                    poly = poly.difference(o)
                else:
                    break
                '''if o != None:
                    poly = poly.union(o)
                    k = i-1
                    res = scipy.optimize.basinhopping(_objective_function, (angle, shift_X, shift_y))
                    if res.fun < 0:
                        angle, shift_X, shift_y = res.x
                        o = affinity.rotate(shift_geom(obj, shift_X, shift_y), angle)
                        ret.append(o)
                        poly = poly.difference(o)
                    break'''
    return ret
'''def place_objects(poly, objects):
    def _objective_function(args):
        angle, shift_X, shift_y = args
        o = affinity.rotate(shift_geom(obj, shift_X, shift_y), angle)
        if poly.wkt.find("MULTIPOLYGON") > -1:
            m = 100000
            r = poly
            for p in poly:
                if p.area-o.area > 0 and p.area < m:
                    m = p.area
                    r = p
            return distance(r, o)
        return distance(poly, o) 
    m1, m2, m3, m4 = poly.bounds
    ret = []
    for obj in objects:
        res = scipy.optimize.dual_annealing(_objective_function, bounds=((0,360), (0, m3), (0,m4)))
        if res.fun < 0:
            angle, shift_X, shift_y = res.x
            o = affinity.rotate(shift_geom(obj, shift_X, shift_y), angle)
            ret.append(o)
            poly = poly.difference(o)
        else:
            
            break
    return ret'''
    
'''poly = poly.minimum_rotated_rectangle
    objects = objects.minimum_rotated_rectangle
    print(*poly.exterior.xy)
    print(*objects.exterior.xy)
    return poly, objects'''
    #return poly.area > sum([obj.area for obj in objects])


def distance(obj1:Polygon | MultiPolygon, obj2: Polygon, count):
    global con
    if obj1.wkt.find("MULTIPOLYGON") > -1:
        a = []
        for o in obj1:
            
            a.extend(list(zip(*o.exterior.xy)))
    else: 
        a = list(zip(*obj1.exterior.xy))
    b = list(zip(*obj2.exterior.xy))
    distances = []
    for i in range(0, len(a)):
        if i > 0 and i<len(a)-1 and (a[i+1][0] - a[i-1][0]) * (a[i][1] - a[i-1][1]) - (a[i][0] - a[i-1][0]) *(a[i+1][1] - a[i-1][1]) < 20:
            #print("pop")
            continue
        for y in b:
            
            distances.append((math.dist(a[i], y)))
            
    distances.sort()
    length = int(0.6 * (len(a) * len(b)))
    distances = distances[:length]
    minx, miny, maxx, maxy = obj1.bounds
    r = sqrt((maxx-minx)**2 +(maxy-miny)**2)
    
    dist = sum([count/(d*d+0.1) for d in distances])
    #dist = sum([d for d in distances])
    buf = obj1.buffer(-1)
    buf1 = obj1.buffer(1)
    buf2 = buf1.difference(buf)
    
    #plt.plot(*buf.interiors.xy)
    #plt.plot(*obj1.exterior.xy)
    
    ar = buf2.intersection(obj2.boundary)

    #ar = abs(obj1.union(obj2).area - obj1.area)
    #if ar != 0:
        #ar+=1/ar
    m = 0
    res = 0
    a1 = []
    #for o in bu:
            
    
    
    
    
    if type(ar) == MultiPolygon or type(ar) == MultiLineString:
        #print(ar)
        con+=1
        if con == 1:
            #plt.plot(*obj1.exterior.xy)
            #plt.plot(*obj2.exterior.xy)
            for t in ar:
                #plt.plot(*t.exterior.xy)
                
                
                m +=t.length

            
    if type(ar) == LineString :
            m = ar.length
        
    elif type(ar) == Polygon:
        m = ar.length
    f, f1 = obj1.centroid.coords.xy
    s, s1 = obj2.centroid.coords.xy
    
    #print(m, (obj1.union(obj2).area - obj1.area), euclidean((f[0], f1[0]), (s[0], s1[0])))
    #print(dist, (obj1.union(obj2).area - obj1.area) )
    
    #print(m, dist)
    
    return (obj1.union(obj2).area - obj1.area) - dist#- euclidean((f[0], f1[0]), (s[0], s1[0]))


'''def distance(obj1:Polygon | MultiPolygon, obj2: Polygon):
    lst = []
    if obj1.wkt.find("MULTIPOLYGON") > -1:
        
        for o in obj1:

            lst.append(list(zip(*o.exterior.xy)))
    else: 
        lst.append(list(zip(*obj1.exterior.xy)))
    
    b = list(zip(*obj2.exterior.xy))
    dist = -1
    for a in lst:
        
        distances = []
        for i in range(0, len(a)):
            if i > 0 and i<len(a)-1 and (a[i+1][0] - a[i-1][0]) * (a[i][1] - a[i-1][1]) - (a[i][0] - a[i-1][0]) *(a[i+1][1] - a[i-1][1]) < 20:
                #print("pop")
                continue
            for y in b:
                distances.append(math.dist(a[i], y))
        dist = max(sum([1/(d+0.1) for d in distances ]), dist)
   
    
    #length = int(0.4 * (len(a) + len(b)))
    #distances = distances[:length]
    
    
    
    return -dist+ abs(obj1.union(obj2).area - obj1.area)'''
