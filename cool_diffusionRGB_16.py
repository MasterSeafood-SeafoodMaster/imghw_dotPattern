import cv2
import numpy as np
from toolkit import putRandom, getRandomMat, cool_diffusionRGB, cool_diffusionGray
#讀取套件

orimg = cv2.imread("./sky.png")
orimg = cv2.resize(orimg, (1024, 1024)) #讀取一張1024x1024得圖片
img = orimg.copy() #將原圖備份


img = cool_diffusionRGB(img, 8) #呼叫轉換涵式
final = cv2.hconcat( (orimg, img) )#將原圖與回傳圖合併
cv2.imwrite("./save/final.png", final)#儲存圖片


"""
final = cv2.resize(final, (1024, 512))
cv2.imshow("live", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""