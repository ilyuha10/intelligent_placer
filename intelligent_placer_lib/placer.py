from shapely.geometry import Polygon, MultiPolygon, Point, box, LineString, MultiLineString
import math
from math import sqrt
import scipy.optimize
from intelligent_placer_lib.geometry import shift_geom
import numpy as np
from shapely import affinity

from matplotlib import pyplot as plt



def place_objects(poly:Polygon, objects:list[Polygon])->tuple[bool, list[Polygon]]:
    '''
    Размещение objects в poly
    :param poly: фигура внутри которой нужно разместить предметы
    :param objects: список предметов, которые нужно разместить в poly
    :return: кортеж, первым элементом которого является результат работы плейсера, то есть True or False
    в зависимости от того получилось ли уложить предметы, и список смещенных и повернутых предметов, которые
    удалось поместить в poly
    '''
    MAX_ITER = 10 
    ERROR_RATE = 1 # допустимая погрешность в 1 пиксель
    def _objective_function(args:tuple[float, float, float])->float:
        '''
        Целевая функция, которую использует differential_evolution
        :param args: кортеж из трех значений: угол поворота фигуры, смещение по х и смещение по у
        :return: значение целевой функции
        '''
        nonlocal i, prevs
        PENALTY_ZONE = 50 
        penalty = 0
        angle, shift_X, shift_y = args
        #if prevs != None:
        for p in prevs[i]:
            #текущие значения должны отличаться от неудачных хотя бы на величину PENALTY_ZONE
            check = abs(angle - p[0]) + abs(shift_X-p[1]) + abs(shift_y - p[2]) 
            if check < PENALTY_ZONE:
                #делим, тк хотим, чтобы при наименьшем отклонении от неудачных значений, больше штрафовалась
                #целевая функция, тем самым минимизируя риск поставить предмет примерно в ту же точку
                penalty = PENALTY_ZONE/(check+0.1) 
        o = affinity.rotate(shift_geom(obj, shift_X, shift_y), angle)
        #минимизируем разницу между площадьми полигона с предметом и без и минимизируем штраф на первой итерации 
        #penalty = 0, так же максимизируем функцию расстояния
        return (poly.union(o).area - poly.area) - distance(poly, o) + penalty


    minx, miny, maxx, maxy = poly.bounds
    # Пытаемся уложить предметы MAX_ITER раз
    the_best_result = []  #сюда сохраняем лучший результат

    #создаем список списков, который будет хранить предыдущие неудачные значения, при которой был найден 
    #минимум целевой функции для каждого предмета, необходим для того, чтобы differential_evolution
    # не возвращала примерно те же позиции предметов.
    #За приближение к неудачным результатам "штрафуем" целевую функцию
    prevs = [[] for g in range(MAX_ITER-1)]  
    poly_copy = poly
    objects_copy = objects.copy()
    
    for n in range(MAX_ITER):
        poly = poly_copy
        objects = objects_copy.copy()
        cur_res = []
        for i, obj in enumerate(objects):
            if obj.area > poly.area:
                #сравниваем площади, чтобы не заставлять алгоритм лишние MAX_ITER раз укладывать предметы
                #этот иф убрать можно, но сильно пострадает скорость выполнения, особенно тестах False
                #print(">")
                return False, the_best_result
            
            opt = scipy.optimize.differential_evolution(_objective_function, bounds=((0,360), (0, maxx), (0,maxy)))
            
            angle, shift_X, shift_y = opt.x
            prevs[i].append(opt.x)#сохраняем попытку
            o = affinity.rotate(shift_geom(obj, shift_X, shift_y), angle)

            if poly.union(o).area - poly.area < ERROR_RATE:
                cur_res.append(o) 
                if len(cur_res) > len(the_best_result):
                    the_best_result = cur_res.copy()

                if len(the_best_result) == len(objects):
                    #print(prevs)
                    return True, the_best_result
                poly = poly.difference(o)
            else:
                #print(poly.union(o).area - poly.area)
                break
    return len(the_best_result) == len(objects), the_best_result


def distance(poly:Polygon | MultiPolygon, obj: Polygon)->float:
    '''
    Вспомогательная функция для _objective_function
    :param poly: Фигура, в которую нужно поместить предмет
    :param obj: Предмет, который нужно поместить в нарисованную фигуру
    :return: сумма MAGIC/(d*d+1), где MAGIC =30, а d - расстояние между точками полигонов описывающих предмет
    и нарисованную фигуру
    '''
    MAGIC = 30 # константа для улучшения сходимости:) подобрана экспериментальным путем
    if poly.wkt.find("MULTIPOLYGON") > -1:
        p_ext = []
        for p in list(poly.geoms):
            p_ext.extend(list(zip(*p.exterior.xy)))
    else: 
        p_ext=list(zip(*poly.exterior.xy))
    
    o_ext = list(zip(*obj.exterior.xy))
    dist = 0
    
    for i in range(len(p_ext)):
        if i > 0 and i<len(p_ext)-1 and (p_ext[i+1][0] - p_ext[i-1][0]) * (p_ext[i][1] - p_ext[i-1][1])\
            - (p_ext[i][0] - p_ext[i-1][0]) *(p_ext[i+1][1] - p_ext[i-1][1]) < 1:
            # это условие проверяет не находятся ли точки полигона примерно на одной прямой
            # оно необходимо, чтобы объекты не магнитились к местам скопления точек полигона
            #пример работы алгоритма без этого условия можно посмотреть в папке image, фото example.png
            continue
        for j in range(len(o_ext)):
            d = math.dist(p_ext[i], o_ext[j])
            #хотим увеличить вес точек, которые находятся близко к границам, и почти не учитывать дальние точки
            dist+= MAGIC/(d*d+1)
    return dist
