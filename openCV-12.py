import cv2
import numpy as np
print(cv2.__version__)
#init values
hueLow = 0
hueHigh = 0
hueLow2 = 0
hueHigh2 = 0 
satLow = 0
satHigh = 0
valLow = 0
valHigh = 0
#Track functions
def onTrack1(val):
    global hueLow
    hueLow = val
    print("Hue Low: ",hueLow)

def onTrack2(val):
    global hueHigh
    hueHigh = val
    print("Hue High: ",hueHigh)

def onTrack3(val):
    global satLow
    satLow = val
    print("Sat Low: ",satLow)

def onTrack4(val):
    global satHigh
    satHigh = val
    print("Sat High: ",satHigh)

def onTrack5(val):
    global valLow
    valLow = val
    print("Val Low: ",valLow)

def onTrack6(val):
    global valHigh
    valHigh = val
    print("Val High: ",valHigh)

def onTrack7(val):
    global hueLow2
    hueLow2 = val
    print("hue Low2: ",hueLow2)

def onTrack8(val):
    global hueHigh2
    hueHigh2 = val
    print("hue High2: ",hueHigh2)

width=1000
height=600
TB1max = 179
TB2max = 255
TB3max = 255
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
#Create trackbar window and trackbars
cv2.namedWindow("myTracker")
cv2.resizeWindow("myTracker",(400,400))
cv2.moveWindow("myTracker",width,0)
cv2.createTrackbar("Hue1 Low","myTracker",10,TB1max,onTrack1)
cv2.createTrackbar("Hue1 High","myTracker",20,TB1max,onTrack2)
cv2.createTrackbar("Hue2 Low","myTracker",10,TB1max,onTrack7)
cv2.createTrackbar("Hue2 High","myTracker",20,TB1max,onTrack8)
cv2.createTrackbar("Sat Low","myTracker",10,TB2max,onTrack3)
cv2.createTrackbar("Sat High","myTracker",250,TB2max,onTrack4)
cv2.createTrackbar("Val Low","myTracker",10,TB3max,onTrack5)
cv2.createTrackbar("Val High","myTracker",250,TB3max,onTrack6)

while True:
    ignore, frame = cam.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow,satLow,valLow])
    upperBound = np.array([hueHigh,satHigh,valHigh])

    lowerBound2 = np.array([hueLow2,satLow,valLow])
    upperBound2 = np.array([hueHigh2,satHigh,valHigh])    

    myMask = cv2.inRange(frame,lowerBound,upperBound)
    myMask2 = cv2.inRange(frame,lowerBound2,upperBound2)
    myMaskComp = myMask | myMask2
    #myMask = cv2.bitwise_not(myMask)
    myObject = cv2.bitwise_and(frame,frame,mask=myMaskComp)
    myObjectSmall = cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow("myObject",myObjectSmall)
    cv2.moveWindow("myObject",int(width/2),int(height))
    myMaskSmall = cv2.resize(myMask,(int(width/2),int(height/2)))
    cv2.imshow("My Mask",myMaskSmall)
    cv2.moveWindow("My Mask",0,height)

    myMaskSmall2 = cv2.resize(myMask2,(int(width/2),int(height/2)))
    cv2.imshow("My Mask 2",myMaskSmall2)
    cv2.moveWindow("My Mask 2",0,height + 335)

    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)



    if cv2.waitKey(1) & 0xff == ord("q"):
        break



cam.release()