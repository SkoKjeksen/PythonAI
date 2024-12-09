import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)
    #window 2
    cv2.imshow("my WebCam2",grayFrame)
    cv2.moveWindow("my WebCam2",641,0)
    #Window 4
    cv2.imshow("my WebCam4",frame)
    cv2.moveWindow("my WebCam4",641,511)
    #Window 3
    cv2.imshow("my WebCam3",grayFrame)
    cv2.moveWindow("my WebCam3",0,511)


    if cv2.waitKey(1) & 0xff == ord("q"):
        break



cam.release()