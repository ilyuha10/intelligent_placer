from shapely.geometry import Polygon
import shapely.ops
import numpy as np
def create_polygons(poly_cnt:np.ndarray, objects_cnt:list[np.ndarray])->tuple[Polygon, list[Polygon]]:
    '''
    Создает shapely.Polygons из контуров
    :param poly_cnt: контур нарисованной фигуры
    :param objects_cnt: список контуров предметов
    :return: полигон, задающий нарисованную фигуру и отсортированный по убыванию список полигонов задающих предметы
    '''
    POLYGON_SIMPLIFY = 5      #константы для упрощений полигонов, для обьектов берем меньшую константу,тк
    OBJECT_SIMPLIFY = 3       #они могут иметь овальные/круглые формы и бОльшее упрощение будет слишком грубым
    #упрощение нужно для улучшения скорости и работы алгоритма, тк в некоторых местах 
    #загущаются точки и алгоритм с бОльшей долей вероятности уложит той предмет той стороной, на которой
    #произошло загущение
    p1 = [tuple(p) for p in poly_cnt[:, 0]]
    poly = Polygon(p1).simplify(POLYGON_SIMPLIFY)
    
    objs = []
    for o in objects_cnt:
        o1 = [tuple(p) for p in o[:, 0]]
        objs.append(Polygon(o1).simplify(OBJECT_SIMPLIFY))
    objs.sort(key=lambda x: x.area, reverse=True) 
    return poly, objs

def shift_geom(geom:Polygon, shift_x:float, shift_y:float)->Polygon:
    '''
    Функция сдвигает все точки геометрии
    :param geom: геометрия, которую необходимо сдвинуть
    :param shift_x: величина, на которую сдвигаем геометрию по оси х
    :param shift_y: величина, на которую сдвигаем геометрию по оси у
    :return: geom, сдвинутый на shift_x и shift_y по осям х и у соответственно
    '''
    def _shift(x, y):
        return list([xi+shift_x for xi in x]), list([yi+shift_y for yi in y])
    return shapely.ops.transform(_shift, geom)

def shift_geom_to_the_beginning(geom: Polygon)->Polygon:
    '''
    Сдвиг геометрии к началу координат
    :param geom: геометрия, которую необходимо сдвинуть
    :return: geom, сдвинутый к началу координат
    '''
    min_x = geom.bounds[0]
    min_y = geom.bounds[1]

    return shift_geom(geom, -min_x, -min_y)