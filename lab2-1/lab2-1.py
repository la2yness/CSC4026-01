# 2019113634 조준혁
import cv2

image1 = cv2.imread('img1.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('img2.png', cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread('img3.png', cv2.IMREAD_GRAYSCALE)
image4 = cv2.imread('img4.png', cv2.IMREAD_GRAYSCALE)

and_result = cv2.bitwise_and(image1, image2)
or_result = cv2.bitwise_or(image1, image2)
or_result_binarized = cv2.bitwise_or(image3, image4)

cv2.imshow('AND Result', and_result)
cv2.imshow('OR Result', or_result)
cv2.imshow('OR Result(Binarized)', or_result_binarized)

cv2.imwrite('and_result.png', and_result)
cv2.imwrite('or_result.png', or_result)
cv2.imwrite('or_result_binarized.png', or_result_binarized)

cv2.waitKey(0)
cv2.destroyAllWindows()