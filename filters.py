import cv2
import numpy as np

# Filter Gaussian
def apply_gaussian(img):
    return cv2.GaussianBlur(img, (5, 5), 0)

# Filter Median
def apply_median(img):
    return cv2.medianBlur(img, 5)

# Filter Hybrid (gabungan Gaussian + Median)
def apply_hybrid(img):
    gaussian = apply_gaussian(img)
    hybrid = apply_median(gaussian)
    return hybrid
