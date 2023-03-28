import cv2
import numpy as np

## 读图
path = '2.jpg'
img = cv2.imread(path)
## 图片预处理
img = cv2.resize(img, (0,0),None,0.5,0.5)#图片太大，进行缩减方便展示
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 灰度化
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)     # 高斯模糊
imgCanny = cv2.Canny(imgBlur,100,100)     # 边缘检测
kernel = np.ones((5,5))
imgDial = cv2.dilate(imgCanny,kernel,iterations=3) # 膨胀
imgThre = cv2.erode(imgDial,kernel,iterations=2)   # 腐蚀

# 寻找所有的外轮廓
contours, hiearchy = cv2.findContours(imgThre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
finalCountours = []
minArea = 1000
filter = 4
# 遍历找到的轮廓
for i in contours:
    area = cv2.contourArea(i)  # 轮廓的面积
    if area > minArea:  # 如果大于设置的最小轮廓值，就往下走
        peri = cv2.arcLength(i, True)  # 封闭轮廓的长度
        approx = cv2.approxPolyDP(i, 0.02 * peri, True)  # 封闭轮廓曲线拐点坐标
        bbox = cv2.boundingRect(approx)  # 找到轮廓的最小矩形
        if filter > 0:  # 需不需要根据拐点个数进行过滤轮廓
            if len(approx) == filter:  # 拐点个数，面积，拐点坐标，边界框，轮廓
                finalCountours.append([len(approx), area, approx, bbox, i])
        else:
            finalCountours.append([len(approx), area, approx, bbox, i])
# 将轮廓从大到小进行排列
finalCountours = sorted(finalCountours,key=lambda x:x[1] , reverse=True)


cv2.imshow("sort",img)
cv2.waitKey(0)
cv2.destroyAllWindows()