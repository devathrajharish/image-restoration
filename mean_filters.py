import cv2
import numpy as np
import math
from decimal import Decimal, getcontext


def nthroot(n, A, precision):
    getcontext().prec = precision

    n = Decimal(n)
    a = A / n  # step 1: make a while guess.
    b = 1  # need it to exist before step 2
    while True:
        # step 2:
        a, b = b, (1 / n) * ((n - 1) * a + (A / (a ** (n - 1))))
        if np.any(a == b):
            return a




def arithmetic_filter(image):
    val = 0
    pixels = 0
    height = image.shape[0]
    width = image.shape[1]
    arithmetic_image =  image.copy()
    for row in range(height):
        for col in range(width):
            pixel = get_neighbors(row, col, image, 1)
            total = sum(pixel)
            pixels = total / 9
            arithmetic_image[row][col] = pixels
    return arithmetic_image

def geometric_filter1(image):
    height = image.shape[0]
    width = image.shape[1]
    val = 0
    total1 = 0
    product = 1
    geo_image = image.copy()
    for row in range(height):
        for col in range(width):
            pixel = get_neighbors(row, col, image, 1)
            pixel1 = np.prod(pixel)
            total = nthroot(9, pixel1, 10)
            geo_image[row][col] = total
    return geo_image


def get_neighbors(row, col, img, distance):
    return img[max(row - distance, 0):min(row + distance + 1, img.shape[0]),
           max(col - distance, 0):min(col + distance + 1, img.shape[1])].flatten()


lenna = cv2.imread("Lenna.png", 0)
image = cv2.imread("salt.png", 0)
restored_image = geometric_filter1(image)
cv2.imshow("lenna", lenna)
cv2.imshow("noise_image", image)
cv2.imshow("restored_image", restored_image)
cv2.waitKey(0)

# from matplotlib import pyplot as plt
#
# plt.figure("noise")
# plt.hist(image.ravel(), 256, [0, 256])
#
# plt.figure("restored")
# plt.hist(restored_image.ravel(), 256, [0, 256])
#
# plt.figure("lenna")
# plt.hist(lenna.ravel(), 256, [0, 256])
# plt.show()
