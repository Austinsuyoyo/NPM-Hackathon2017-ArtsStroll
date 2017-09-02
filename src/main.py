# coding:utf8
import cv2
import numpy as np


def pic_sub(emptyimg,detection,back):
    for x in range(emptyimg.shape[0]):
        for y in range(emptyimg.shape[1]):
            if(back[x,y] is 0):
                emptyimg[x,y] = back[x,y]
            else:
                emptyimg[x,y] = detection[x,y]
    return emptyimg


def detect_video(video):
    camera = cv2.VideoCapture(video)
    cols = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    rows = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    history = 500   # 訓練次數
    
    bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)  # 背景減除器 陰影偵測
    bs.setHistory(history)

    frames = 0

    while True:
        res, frame = camera.read()
        
        
        if not res:
            break

        fg_mask = bs.apply(frame)   # 獲取 foreground mask

        if frames < history:
            frames += 1
            continue

        

        
        # 對原圖進行膨脹去雜訊
        th = cv2.threshold(fg_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=2)
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 3)), iterations=2)

        kernel = np.ones((5,5),np.float32)/25
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.dilate(dilated, kernel, iterations=1)
        dilated = cv2.dilate(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.dilate(dilated, kernel, iterations=1)
        dilated = cv2.dilate(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.dilate(dilated, kernel, iterations=1)
        dilated = cv2.dilate(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        dilated = cv2.erode(dilated, kernel, iterations=1)
        
        



        # 獲取所有檢測圖
        image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        """
        for c in contours:
            # 获取矩形框边界坐标
            x, y, w, h = cv2.boundingRect(c)
            # 计算矩形框的面积
            area = cv2.contourArea(c)
            if 500 < area < 3000:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        """
        #濾鏡
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.applyColorMap(frame, cv2.COLORMAP_PINK)

        #mask擷取
        img = cv2.imread('backgroung.jpg')
        orgPoint = [123,131]
        orgSize = (333,320)
        
        roi = img[orgPoint[1]:orgPoint[1]+orgSize[1],orgPoint[0]:orgPoint[0]+orgSize[0]]
        
        mask = cv2.resize(dilated,orgSize, interpolation=cv2.INTER_AREA)
        mask_inv = cv2.bitwise_not(mask)

        frame_resized = cv2.resize(frame,orgSize, interpolation=cv2.INTER_AREA)
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv2.bitwise_and(frame_resized,frame_resized,mask = mask)

        dst = cv2.add(img1_bg,img2_fg)
        resized = cv2.resize(dst,orgSize, interpolation=cv2.INTER_AREA)
        """
        emptyimg = cv2.bitwise_and(frame,frame,mask = dilated)
        emptyimg_inv = cv2.bitwise_not(dilated)
        dic = cv2.bitwise_and(emptyimg_inv,emptyimg_inv,mask = emptyimg)
        """
        #放入img
        img[orgPoint[1]:orgPoint[1]+orgSize[1],orgPoint[0]:orgPoint[0]+orgSize[0]] = resized

        
        cv2.imshow("detection", frame)
        cv2.imshow("back", dilated)
        cv2.imshow("output", resized)
        cv2.imshow("img", img)
        if cv2.waitKey(110) & 0xff == 27:
            break
    camera.release()


if __name__ == '__main__':
    video = 'person.avi'
    detect_video(video)

detect_video(0)
