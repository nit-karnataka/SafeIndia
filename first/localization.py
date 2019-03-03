import numpy as np
import cv2
str2="sample.png"
rgb = cv2.imread(str2,0)
cv2.imshow('original',rgb)
fresh=cv2.imread(str2)
cv2.imshow('colour',fresh)
morphKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3, 3))
cv2.imshow('morph',morphKernel)
grad=cv2.morphologyEx(rgb, cv2.MORPH_GRADIENT, morphKernel)
cv2.imshow('gradient',grad)
retval,bw =cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('bnw',bw)
morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, morphKernel)
cv2.imshow('connects',connected)
mask = np.zeros(bw.shape, dtype = "uint8")

image,contours2, hierarchy = cv2.findContours(connected,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('connects2',image)
txtRect=[]
txtContour=[]
x=0
while x<len(contours2):
	print(x)
	(start_x,start_y,width,height)= cv2.boundingRect(contours2[x])
	
	rect=(start_x,start_y,width,height)
	print(start_x,start_y,width,height)
	maskROI =mask, cv2.boundingRect(contours2[x])
	#if(x>100 and x<150):
	#cv2.imwrite("final_mask" +str(x)+ str2 , maskROI)
	maskROI = (0, 255, 0)
	cv2.drawContours(mask, contours2, x, (255, 255, 255), cv2.FILLED)
	g = cv2.countNonZero(maskROI)
	print("g=",g)
	r=float(g)/(width*height)
	print("r=",r)
	if (height >10 and width > 10 and height<0.3*np.size(rgb, 0) and width<0.3*np.size(rgb, 1)):
	#if 1:
		cv2.rectangle(fresh, (start_x,start_y),(width+start_x,height+start_y),(0, 255, 0), 2)
		txtRect.append(rect)
    	txtContour.append(contours2[x])
	x=x+1
	#x = hierarchy[x][0][1]
cv2.imshow('Characters', fresh)
cv2.imwrite("final" + str2 , fresh)



cv2.waitKey(0)
