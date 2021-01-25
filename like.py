import cv2 as cv
import numpy as np
import os
import time
num=0
while(1):
	count=0 #照片序号&&点赞数量
	list = []
	while(1):
		print("count=",count)
		print("num=",num)
		os.system('adb shell screencap -p /sdcard/{}.png'.format(num))
		os.system('adb pull /sdcard/{}.png'.format(num))
		
		img = cv.imread('{}.png'.format(num),cv.IMREAD_COLOR)
		num+=1
		i=1 #照片列像素
		flag=0#判断点赞行为是否被实施，0为否
		while i<2400:
			blue1,red1,green1  = (int)(img[i,995,0]),(int)(img[i,995,1]),(int)(img[i,995,2]) 
			blue2,red2,green2  = (int)(img[i,1005,0]),(int)(img[i,1005,1]),(int)(img[i,1005,2]) 
			if(blue1==149 and red1==107 and green1 == 87 and blue2==248 and red2==248 and green2==248): 
				ok=0
				for j in range(count): #遍历是否点过赞
					if(list[j]==i):
						i+=20
						ok=1
						break 
				if(ok==1): continue
				os.system('adb shell input tap 995 {}'.format(i))
				os.system('adb shell input tap 531 {}'.format(i))#实行点赞操作
				time.sleep(1)
				print(i)
				flag=1
			else: i+=1
			if(flag==1):
				list.append(i) #将i加入已点赞序列
				count+=1#点赞量加1
				break
		if(i==2400): break
	os.system('adb shell input swipe 1000 2200 1000 300 1000')
	time.sleep(1)