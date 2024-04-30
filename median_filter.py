import cv2
import numpy as npy

original1 = cv2.imread("1.png", 1)
original2 = cv2.imread("2.png", 1)
original3 = cv2.imread("3.png", 1)
original4 = cv2.imread("4.png", 1)
original5 = cv2.imread("5.png", 1)
original6 = cv2.imread("6.png", 1)
original7 = cv2.imread("7.png", 1)
original8 = cv2.imread("8.png", 1)
original9 = cv2.imread("9.png", 1)
original10 = cv2.imread("10.png", 1)
original11 = cv2.imread("11.png", 1)
original12 = cv2.imread("12.png", 1)
original13 = cv2.imread("13.png", 1)
original14 = cv2.imread("14.png", 1)
original15 = cv2.imread("15.png", 1)
original16 = cv2.imread("16.png", 1)
original17 = cv2.imread("17.png", 1)
original18 = cv2.imread("18.png", 1)
original19 = cv2.imread("19.png", 1)

img = npy.zeros((562, 1000, 3), dtype=npy.uint8)

for i in range(0, 562):
    for j in range(0, 1000):
        for k in range(0, 3):
            all_pixel = [original1[i, j, k], original2[i, j, k], original3[i, j, k], original4[i, j, k],
                         original5[i, j, k], original6[i, j, k],
                         original7[i, j, k], original8[i, j, k], original9[i, j, k], original10[i, j, k],
                         original11[i, j, k], original12[i, j, k],
                         original13[i, j, k], original14[i, j, k], original15[i, j, k], original16[i, j, k],
                         original17[i, j, k], original18[i, j, k],
                         original19[i, j, k]]  # 將圖片的每一 pixel 讀入並排序
            all_pixel.sort()  # 排序
            img[i, j, k] = all_pixel[9]  # 取中間沒有人的值，因 19 張圖片的 index 為 0～18，故取 9

cv2.imshow('img', img)
cv2.imwrite('final.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
