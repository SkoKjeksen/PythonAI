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
while True:
    ignore, frame = cam.read()
    frameROI = frame[150:210,250:390]
    frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    frameROIBGR = cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR)
    frame[0:60,0:140] = frameROIBGR
    cv2.imshow("my ROI",frameROIBGR)
    cv2.moveWindow("my ROI",650,0)
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)


    if cv2.waitKey(1) & 0xff == ord("q"):
        break



cam.release()