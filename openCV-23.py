import cv2
print(cv2.__version__)


class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=1,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(2)

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    frame=cv2.flip(frame, 1)
    handData=findHands.Marks(frame)
    for hand in handData:
        
        for ind in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
            cv2.circle(frame,hand[ind],5,(255,0,0),3)
   
   

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()