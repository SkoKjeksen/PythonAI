import cv2
import mediapipe as mp
print(cv2.__version__)
width=1080
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
hands = mp.solutions.hands.Hands(False,2,1,0.5)
mpDraw = mp.solutions.drawing_utils

while True:
    myHands=[]
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            myHand=[]
            mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            #for LandMark in handLandMarks.landmark:
            
                #myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
            
            
            cv2.circle(frame,myHand[17],10,(255,0,0),2)
            cv2.circle(frame,myHand[18],10,(255,0,0),2)
            cv2.circle(frame,myHand[19],10,(255,0,0),2)
            cv2.circle(frame,myHand[20],10,(255,0,0),2)
            myHands.append(myHand)
            print(myHands)
        



    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()