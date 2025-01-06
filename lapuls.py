import cv2
import numpy as np
 
# 讀取圖像
image = cv2.imread('path_to_your_image.jpg')
 
# 轉換為灰度圖像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# 使用拉普拉斯運算元進行邊緣檢測
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
 
# 將拉普拉斯圖像轉換為8位元圖像
laplacian = cv2.convertScaleAbs(laplacian)
 
# 銳化圖像：原圖 + 拉普拉斯圖像
sharpened = cv2.addWeighted(gray, 1.5, laplacian, -0.5, 0)
 
# 顯示結果
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Edge Detection', laplacian)
cv2.imshow('Sharpened Image', sharpened)
 
# 等待按鍵，然後關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
