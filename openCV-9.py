import cv2
import numpy as np
print(cv2.__version__)
evt = 0
xVal = 0
yVal = 0

def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global xVal
    global yval
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos

    if event == cv2.EVENT_LBUTTONUP:
        evt = event
        print(event)

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cv2.namedWindow("my WebCam")
cv2.setMouseCallback("my WebCam",mouseClick)

while True:
    ignore, frame = cam.read()
    if evt == 1:
        x=np.zeros([250,250,3],dtype=np.uint8)
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        y2 = cv2.cvtColor(y,cv2.COLOR_HSV2BGR)
        clr = y2[yVal][xVal]
        print(clr)
        x[:,:] = clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow("Color Picker",x)
        cv2.moveWindow("Color Picker",width,0)
        evt = 0
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)



    if cv2.waitKey(1) & 0xff == ord("q"):
        break



cam.release()