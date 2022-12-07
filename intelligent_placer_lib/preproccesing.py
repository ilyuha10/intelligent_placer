import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_contours(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)

    edges = cv2.Canny(img,60,105)
    edges = cv2.dilate(edges.copy(), cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    
    #plt.imshow(edges, cmap='gray')
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = list(filter(lambda x: cv2.contourArea(x) > 300,contours))
    #contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

def sort_contours(cnts):
    pass



def load_images(path):
    images = []
    names = []
    for filename in os.listdir(path):
        image = cv2.imread(os.path.join(path, filename))
        images.append(image)
        names.append(filename)
    return images, names




