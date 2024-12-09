import cv2
import time
print(cv2.__version__)
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))



faceCascade=cv2.CascadeClassifier("haar/haarcascade_frontalface_default.xml")
eyesCascade=cv2.CascadeClassifier("haar/haarcascade_eye.xml")

fps=10
timeStamp = time.time()

while True:
    ignore, frame = cam.read()

    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h = face
        #print("x=",x,"y=",y,"width=",w,"height=",h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    eyes = eyesCascade.detectMultiScale(frameGray,1.3,5)
    for eye in eyes:
        x,y,w,h = eye
        cv2.circle(frame,(int((x+x+w)/2),int((y+y+h)/2)),10,(0,0,255),2)

    #fps calc    
    loopTime = time.time()-timeStamp
    timeStamp=time.time()
    fpsNew = 1/loopTime
    fps=.9*fps+.1*fpsNew
    fps=int(fps)
    cv2.putText(frame,str(fps),(30,60),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2)
    #print(fps)
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)


    if cv2.waitKey(1) & 0xff == ord("q"):
        break



cam.release()