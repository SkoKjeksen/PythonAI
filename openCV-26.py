import cv2
print(cv2.__version__)

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=1,tol2=.5):
        self.hands = self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands = []
        handsType = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                #print(hand)
                #print(hand.classification)
                #print(hand.classification[0])
                handType = hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType



width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
findHands = mpHands()
while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    handData,handsType = findHands.Marks(frame)
    for hand,handType in zip(handData,handsType):
        if handType =="Right":
            handColor=(255,0,0)
        if handType =="Left":
            handColor=(0,0,255)
        for index in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
            cv2.circle(frame,hand[index],5,handColor,-1)
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()