import cv2

print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

myText = "GIGA NIGGA"
while True:
    ignore, frame = cam.read()
    #frame[140:220,250:390]=(255,0,0)
    #cv2.rectangle(frame,(250,140),(390,220),(0,255,0),10)
    #cv2.circle(frame,(320,180),125,(0,0,0),-1)
    cv2.putText(frame,myText,(120,60),cv2.FONT_ITALIC,2,(0,0,255),2)
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

     

cam.release()