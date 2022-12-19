from intelligent_placer_lib.loading import load_images
from intelligent_placer_lib.preproccesing import get_contours
from intelligent_placer_lib.spliter import split_contours
from intelligent_placer_lib.placer import place_objects
from intelligent_placer_lib.placer import distance

from intelligent_placer_lib.geometry import shift_geom_to_the_beginning, create_polygons
from shapely.geometry import Polygon
from intelligent_placer_lib.manager import check_image
import cv2
from matplotlib import pyplot as plt
import csv





images, name = load_images("images/tests")
i=0
j = 0
count = 0
for im in images:
    if name[i]!='19.jpg':
        i+=1
        continue
    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        
        for row in spamreader:
            if name[i] == row[0]+'.jpg':
                comment = row[2]
                correct_answer = bool(int(row[1]))
    
    answer, poly, objects_in_poly = check_image(im)
    count+=(correct_answer==answer)
    fig, ax = plt.subplots(1, 2)
    print(f'{name[i]}, Мой ответ: {answer} Правильный ответ: {correct_answer} Краткий коммент по тесту:{comment}')
    plt.title(name[i])
    ax[0].imshow(im)
    i+=1
    if  poly == None:
        continue
    ax[1].plot(*poly.exterior.xy)
    for o in objects_in_poly:
        ax[1].plot(*o.exterior.xy)
    
    
print(count/len(images))
plt.show()