import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def ifukkie_check():
    img_rgb = cv.imread('test3.jpg')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('sample.jpg',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.358
    loc = np.where( res >= threshold)
    if str(loc) != "(array([], dtype=int32), array([], dtype=int32))":
        return True
    else:
        return False

test = ifukkie_check()
print(test)
