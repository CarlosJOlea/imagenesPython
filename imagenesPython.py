import numpy as np
import cv2
import sys

  
def main():
    img = cv2.imread("images.jpg",cv2.IMREAD_UNCHANGED)
    gray = cv2.imread("images.jpg",cv2.IMREAD_GRAYSCALE)
    color = cv2.imread("images.jpg",cv2.IMREAD_LOAD_GDAL)
    cv2.imshow("Window", img)
    cv2.imshow("Gray", gray)
    cv2.imshow("Color", color)
    cv2.imwrite("1.jpg", img)
    cv2.imwrite("2.jpg", gray)
    cv2.imwrite("3.jpg", color)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()