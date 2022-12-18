import cv2
import random
import numpy as np

#輸入一空白矩陣mat，此函示將在此矩陣隨機位置加入num個點並回傳。
def putRandom(mat, num):
	n=0
	while n<num:
		x = random.randrange(0, len(mat), 1)
		y = random.randrange(0, len(mat), 1)

		if mat[x][y] == 0:
			mat[x][y]=255
			n+=1
	return mat

#輸入一數組 size 格式:[width, height], 此函示將回傳一組隨機產生的色階矩陣。
def getRandomMat(size):
	w=size[0]; h=size[1]; l = w*h+1
	matList=[]

	for i in range(l):
		mat = np.zeros(size).astype(np.uint8)
		mat = putRandom(mat, i)
		matList.append(mat)
	return matList

def combMat(matList):
	l = len(matList); s = int(l**(1/2))
	cLine = np.full( (s, 1), 100 ).astype(np.uint8)
	rLine = np.full( (1, l+s-2), 100).astype(np.uint8)
	img = ""; final=""
	for i in range(0, l):

		if i%s==0:
			if final=="" and img=="":
				pass
			elif final=="":
				final=img.copy()
			else:
				final=cv2.vconcat( (final, rLine) )
				final=cv2.vconcat( (final, img) )
			img=""
		if img=="": 
			img=matList[i]
		else:
			img = cv2.hconcat((img,cLine))
			img=cv2.hconcat( (img, matList[i]) )

	final = cv2.resize(final, (512, 512), interpolation=cv2.INTER_NEAREST)
	return final


def cool_diffusionRGB(img, matSize):

	#隨機產生紅、綠、藍三個顏色的色階矩陣。
	rColorMat = getRandomMat((matSize, matSize))
	gColorMat = getRandomMat((matSize, matSize))
	bColorMat = getRandomMat((matSize, matSize))

	cv2.imwrite("./save/r.png", combMat(rColorMat))
	cv2.imwrite("./save/g.png", combMat(gColorMat))
	cv2.imwrite("./save/b.png", combMat(bColorMat))

	#將原圖以matSize*matSize象素為一個單位進行平均，並視為一個像素。
	colorNum = matSize*matSize
	color_list = []
	color = 0

	#將0~255平均分割為65個區間。
	for i in range(colorNum+1):
		color_list.append(int(i * (255/(colorNum+1) )))

	h, w, c= img.shape
	rgbColorMat = [bColorMat, gColorMat, rColorMat]
	
	#將相對應的矩陣置換於對應的圖片位置中，重複三次。
	for C in range(c):
		for x in range(0, w, matSize):
			for y in range(0, h, matSize):
				r = img[y:y+matSize, x:x+matSize, C]
				for i in range(matSize*matSize):
					if color_list[i] <= np.mean(r) < color_list[i+1]:
						img[y:y+matSize, x:x+matSize, C] = rgbColorMat[C][i]

	return img

def cool_diffusionGray(img, matSize):
	
	colorNum = matSize*matSize

	color_list = []
	color = 0
	for i in range(colorNum+1):
		color_list.append(int(i * (255/(colorNum+1))))

	gColorMat = getRandomMat((matSize, matSize))

	h, w= img.shape

	for x in range(0, w, matSize):
		for y in range(0, h, matSize):
			r = img[y:y+matSize, x:x+matSize]
			for i in range(colorNum):
				if color_list[i] <= np.mean(r) < color_list[i+1]:
					img[y:y+matSize, x:x+matSize] = gColorMat[i]

	return img
