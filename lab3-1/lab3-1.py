# 2019113634 조준혁
import cv2

img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)

# image binarization before morphological operations
_, binarized = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Binarization Result', binarized)
cv2.imwrite('lenna_bi.png', binarized)

# define a cross sign kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# perform dilation and erosion
dilated = cv2.dilate(binarized, kernel, iterations=1)
eroded = cv2.erode(binarized, kernel, iterations=1)
cv2.imshow('Dilation Result', dilated)
cv2.imshow('Erosion Result', eroded)
cv2.imwrite('lenna_di.png', dilated)
cv2.imwrite('lenna_er.png', eroded)

# perform opening and closing
opened = cv2.morphologyEx(binarized, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(binarized, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Opening Result', opened)
cv2.imshow('Closing Result', closed)
cv2.imwrite('lenna_op.png', opened)
cv2.imwrite('lenna_cl.png', closed)

cv2.waitKey(0)
cv2.destroyAllWindows()