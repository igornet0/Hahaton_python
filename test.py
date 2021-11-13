import cv2
import numpy as np
from matplotlib import pyplot as plt

image_bgr = cv2.imread("4.png")
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
image_gray = np.float32(image_gray)

block = 2
aperature = 1
free_parameter = 0

ddetecter = cv2.cornerHarris(image_gray, block, aperature, free_parameter)

ddetecter_res = cv2.dilate(ddetecter, None)

thereshols = 0.02
image_bgr[ddetecter_res > thereshols * ddetecter_res.max()] = [255, 255, 255]

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

plt.imshow(image_gray, cmap='gray')
plt.axis("off")
plt.show()


image_10x10 = cv2.resize(image_gray, (100,100))
plt.imshow(image_10x10, cmap='gray')
plt.axis("off")
plt.show()
a = []
for i in image_10x10.flatten():
    if len(a) == 50:
        print(*a)
        a = [i]
    else:
        a.append(i)