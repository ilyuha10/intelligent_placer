import shapely.wkt
import shapely.ops

from operator import sub

def shift_geom(geom, shift_x, shift_y):
    def _shift(x, y):
        return list([xi+shift_x for xi in x]), list([yi+shift_y for yi in y])
    return shapely.ops.transform(_shift, geom)

def split_contours(cnts):
    min_y = 1000000
    for cnt in cnts:
        cur_y = min(cnt[:, 0][:, 1])
        if min_y > cur_y:
            poly_cnt = cnt
            min_y = cur_y
    cnts.remove(poly_cnt)
    return poly_cnt, cnts

def norm(poly):
    min_y = poly.bounds[1]
    min_x = poly.bounds[0]
    return shift_geom(poly, -min_x, -min_y)
    
