import os
import cv2
import numpy as np

def load_images(path:str) ->tuple[list[np.ndarray], list[str]]:
    '''
    Загружает изображения из указанного пути
    :param path: путь, с которого загружать фото
    :return: список изображений и список имен этих изображений
    '''
    images = []
    names = []
    for filename in os.listdir(path):
        if filename.endswith(('.jpg', '.jpeg')):
            image = cv2.imread(os.path.join(path, filename))
            images.append(image)
            names.append(filename)
    return images, names