from matplotlib import pyplot as plt

import numpy as np


from skimage.feature import canny

from skimage import measure

import cv2
import os
def get_contours(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    edges = canny(img.copy(), sigma=3, low_threshold=10, high_threshold=30).astype(np.uint8)
    edges = cv2.dilate(edges.copy(), cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))

    #plt.imshow(edges, cmap='gray')
    contours = measure.find_contours(edges, 0.7)
    #contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

def sort_contours(cnts):
    pass



def load_images(path):
    images = []
    for filename in os.listdir(path):
        image = cv2.imread(os.path.join(path, filename))
        images.append(image)
    return images




