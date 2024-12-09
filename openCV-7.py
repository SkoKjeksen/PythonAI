import cv2
print(cv2.__version__)

evt = 0
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global point
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Mouse Event Was: ",event)
        print("at Position: ",xPos,yPos)
        evt = event
        point=(xPos,yPos)
    if event==cv2.EVENT_LBUTTONUP:
        print("Mouse Event Was: ",event)
        print("at Position: ",xPos,yPos)
        evt = event
    if event==cv2.EVENT_RBUTTONUP:
        print("Mouse Event Was: ",event)
        evt = event


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
    if evt==1 or evt ==4:
        cv2.circle(frame,point,25,(0,0,255),2)
    
        
    #grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     #cv2.circle(frame,(,180),125,(0,0,0),-1)
     
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)



    if cv2.waitKey(1) & 0xff == ord("q"):
        break



cam.release()