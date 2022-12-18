import cv2
import numpy as np
from toolkit import putRandom, getRandomMat

orimg = cv2.imread("./flower.png")
orimg = cv2.cvtColor(orimg, cv2.COLOR_BGR2GRAY)
orimg = cv2.resize(orimg, (512, 512))

img = orimg.copy()

color_list = []
color = 0
for i in range(17):
	color_list.append(int(i * (255/17)))

print(color_list)

h, w= img.shape


gColorMat = getRandomMat((4, 4))

for x in range(0, w, 4):
	for y in range(0, h, 4):
		r = img[y:y+4, x:x+4]
		for i in range(16):
			if color_list[i] <= np.mean(r) < color_list[i+1]:
				img[y:y+4, x:x+4] = gColorMat[i]

final = cv2.hconcat( (orimg, img) )
#final = cv2.resize(final, (1200, 600), interpolation=cv2.INTER_NEAREST)
cv2.imshow("live", final)
cv2.waitKey(0)
cv2.destroyAllWindows()