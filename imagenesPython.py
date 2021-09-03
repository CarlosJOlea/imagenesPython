import numpy as np
import cv2
import sys

  
def main():
    img = cv2.imread("D:/Python/ImagenesIA/goghan.jpg",cv2.IMREAD_UNCHANGED)
    gray = cv2.imread("D:/Python/ImagenesIA/goghan.jpg",cv2.IMREAD_GRAYSCALE)
    color = cv2.imread("D:/Python/ImagenesIA/goghan.jpg",cv2.cv2.IMREAD_COLOR)
    cv2.imshow("Display window", img)
    cv2.imshow("Display gray", gray)
    cv2.imshow("Display color", color)
    cv2.imwrite("D:/Python/ImagenesIA/goghanSin.jpg", img)
    cv2.imwrite("D:/Python/ImagenesIA/goghanGray.jpg", gray)
    cv2.imwrite("D:/Python/ImagenesIA/goghanColor.jpg", color)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()