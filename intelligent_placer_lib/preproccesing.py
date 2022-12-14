import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_contours(image: np.ndarray):
    '''
    Находит контуры предметов и нарисованной фигуры на изображении
    :param image: массив, описывающий изображение
    :return: список обнаржуенных контуров
    '''
    MIN_AREA = 500

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    img = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)

    edges = cv2.Canny(img,60,105)
    edges = cv2.dilate(edges.copy(), cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = list(filter(lambda x: cv2.contourArea(x) > MIN_AREA,contours))

    return contours

def sort_contours(cnts):
    pass









