import cv2
print(cv2.__version__)

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=1,tol2=.5):
        self.hands = self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands



width=1920   
height=1080
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
findHands = mpHands()
paddleWidth = 125
paddleHeight = 25
paddleColor = (0,255,0)
ballRadius = 15
ballColor = (255,0,0)
xPos = int(width/2)
yPos = int(height/2)
DeltaX = 10
DeltaY = 10
score = 0
lives = 5
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ignore, frame = cam.read()
    handData = findHands.Marks(frame)
    cv2.circle(frame,(xPos,yPos),ballRadius,ballColor,-1)
    cv2.putText(frame,str(score),(25,6*paddleHeight),font,6,(0,0,0),5)
    cv2.putText(frame,str(lives),(width-125,6*paddleHeight),font,6,(0,0,0),5)
    for hand in handData:
        cv2.rectangle(frame,((int(hand[8][0]-paddleWidth/2)),0),((int(hand[8][0]+paddleWidth/2)),paddleHeight),paddleColor,-1)
    topEdgeBall = yPos-ballRadius
    bottomEdgeBall = yPos+ballRadius
    leftEdgeBall = xPos-ballRadius
    rightEdgeBall = xPos+ballRadius
    if leftEdgeBall <=0 or rightEdgeBall >= width:
        DeltaX = DeltaX*(-1)
    if bottomEdgeBall >=height:
        DeltaY = DeltaY*(-1)
    if topEdgeBall<= paddleHeight:      
        if xPos >=(int(hand[8][0]-paddleWidth/2)) and xPos<=int(hand[8][0]+paddleWidth/2):
            DeltaY = DeltaY*(-1)
            score += score
        else:
            xPos = int(width/2)
            yPos = int(height/2)
            lives = lives-1
    xPos = xPos + DeltaX
    yPos = yPos + DeltaY
    #Window 1
    cv2.imshow("my WebCam",frame)
    cv2.moveWindow("my WebCam",0,0)
    if lives == 0:
        break
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cam.release()