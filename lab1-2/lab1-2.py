# 2019113634 조준혁
import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(hist, title):
    plt.figure()
    plt.title(title)
    plt.xlabel('gray level')
    plt.ylabel('frequency')
    plt.scatter(np.arange(len(hist)), hist, s=10)
    plt.xlim([0, 256])
    plt.show()

in_image = cv2.imread('hand.jpg', cv2.IMREAD_GRAYSCALE)
in_image = cv2.resize(in_image, (900, 1200))

# Histogram Equalization using OpenCV 
out_image = cv2.equalizeHist(in_image)
out_hist = cv2.calcHist([out_image], [0], None, [256], [0,256]).flatten()

# CLAHE using OpenCV
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_image = clahe.apply(in_image)
clahe_hist = cv2.calcHist([clahe_image], [0], None, [256], [0,256]).flatten()

cv2.imshow('Input Image', in_image)
cv2.imshow('HE Result', out_image)
cv2.imshow('CLAHE Result', clahe_image)
cv2.imwrite('hand_eq.jpg', out_image)
cv2.imwrite('hand_clahe.jpg', clahe_image)

plot_histogram(out_hist, "HE histogram after equalization")
plot_histogram(clahe_hist, "CLAHE histogram after equalization")

cv2.waitKey(0)
cv2.destroyAllWindows()