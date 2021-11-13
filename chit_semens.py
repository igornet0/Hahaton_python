import numpy as np
import cv2


def chit_semen(file):
    image_bgr = cv2.imread(file)
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    image_gray = np.float32(image_gray)

    block = 2
    aperature = 29
    free_parameter = 0

    detecter = cv2.cornerHarris(image_gray, block, aperature, free_parameter)

    detecter_res = cv2.dilate(detecter, None)

    thereshols = 0.01

    image_bgr[detecter_res > thereshols * detecter_res.max()] = [255, 255, 255]
    n = 0
    for i in image_bgr:
        for j in i:
            if any(j == [255, 255, 255]):
                n += 1
                break

    n *= 3
    return n
