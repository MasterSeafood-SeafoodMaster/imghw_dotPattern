import cv2
import numpy as np
import mat as m

orimg = cv2.imread("./flower.png")
#orimg = cv2.cvtColor(orimg, cv2.COLOR_BGR2GRAY)
orimg = cv2.resize(orimg, (600, 600))

img = orimg.copy()

color_list = []
color = 0
for i in range(10):
	color_list.append(int(i * (255/9)))

print(color_list)

h, w= img.shape


for x in range(0, w, 3):
	for y in range(0, h, 3):
		r = img[y:y+3, x:x+3]
		for i in range(9):
			if color_list[i] <= np.mean(r) < color_list[i+1]:
				img[y:y+3, x:x+3] = m.gMatList[i]

print(img)
final = cv2.hconcat( (orimg, img) )
final = cv2.resize(final, (1200, 600), interpolation=cv2.INTER_NEAREST)
cv2.imshow("live", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
