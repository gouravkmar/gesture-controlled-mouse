import cv2
import numpy as np
import pyautogui

pyautogui.FAILSAFE = False
lowerBound=np.array([40,120,100])
upperBound=np.array([255,255,255])

cam= cv2.VideoCapture(0)

ret,first=cam.read()
(a,b,c,d,e,f,g,h)=(1,1,1,1,1,1,1,1)
lastvaluex=0
lastvaluey=0
flag=0
flag2=0
flag3=0
while True:
    ret, img=cam.read()
    img=cv2.flip(img,1)
    
   
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)   
    maskFinal=mask
    im2,conts,h=cv2.findContours(maskFinal,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,conts,-1,(255,0,0),3)
    
    index=0
    
    if len(conts):
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            if w>10 and h>10:
            #print("ghj")
                (a,b,c,d)=(x,y,w,h)
                index=i
                #print(index)
                break
        for j in range(len(conts)-index-1):
            j=j+index+1
            x,y,w,h=cv2.boundingRect(conts[j])
            if w>10 and h>10:
                (e,f,g,h)=(x,y,w,h)
                break       
        cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,0),3)
        cv2.rectangle(img,(e,f),(e+g,f+h),(0,255,255),3)
        
        if e>1:
            if flag:
                
                (a,b,c,d)=(e,f,g,h)
                if flag2:
                    pyautogui.click()
                    print("click")
                    flag2=0
                flag3=1    
            else:
                flag=1
                flag3=0
                
        else:
            flag=0
            flag2=1
        if a!=1 and flag3:
            
            if abs(a-lastvaluex)>1:
                #print(abs(a-lastvaluex))
                print(a)
                pyautogui.moveRel(0.1*pow((a-lastvaluex),2)*np.sign((a-lastvaluex)),0.1*pow((b-lastvaluey),2)*np.sign((b-lastvaluey)),duration=0)
                lastvaluex=a
                lastvaluey=b
                
    (a,b,c,d,e,f,g,h)=(1,1,1,1,1,1,1,1)
   
    cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.waitKey(10)