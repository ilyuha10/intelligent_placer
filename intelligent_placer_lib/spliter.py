import shapely.wkt
import shapely.ops
import numpy as np
from operator import sub




def split_contours(cnts:list[np.ndarray])->tuple[np.ndarray, list[np.ndarray]]:
    '''
    Разделяет контуры на нарисованный многоугольник и предметы
    :param cnts: список контуров
    :return: контур нарисованной фигуры, и список контуров предметов
    '''
    '''Она немного костыльная, т.к накладывает дополнительное ограничение на входные данные:
    1) На фото обязан быть многоугольник, иначе программа будет неверно работать
    2) Предметы должны располагаться под многоугольником'''
    min_y = 1000000
    for cnt in cnts:
        cur_y = min(cnt[:, 0][:, 1])
        if min_y > cur_y:              # просто находим контур, который будет выше остальных на фото
            poly_cnt = cnt
            min_y = cur_y
    cnts.remove(poly_cnt)
    return poly_cnt, cnts


    
