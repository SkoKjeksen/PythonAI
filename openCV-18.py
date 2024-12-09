import cv2
import face_recognition as FR
print(cv2.__version__)
font =cv2.FONT_HERSHEY_SIMPLEX
width=1440
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Camera config
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

emilFace=FR.load_image_file("C:/Users/Emil Nilsen/Documents/Python/demoImages/known/Emil Nilsen.jpg")
faceLoc=FR.face_locations(emilFace)[0]
emilFaceEncode=FR.face_encodings(emilFace)[0]


geirFace=FR.load_image_file("C:/Users/Emil Nilsen/Documents/Python/demoImages/known/Geir Ingvardsen.jpg")
faceLoc=FR.face_locations(geirFace)[0]
geirFaceEncode=FR.face_encodings(geirFace)[0]

knownEncodings=[emilFaceEncode,geirFaceEncode]
names=["Emil Nilsen","Geir Ingvardsen"]

while True:

    ignore, unknownFace = cam.read()
   
    unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
    faceLocations=FR.face_locations(unknownFaceRGB)
    unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        #print(faceLocation)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)
        name = "unknown Person"

        matches = FR.compare_faces(knownEncodings,unknownEncoding)
        #print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            #print(matchIndex)
            #print(names[matchIndex])
            name = names[matchIndex]
        cv2.putText(unknownFace,name,(left,top-10),font,1,(0,0,255),2)

    cv2.imshow("My Faces",unknownFace)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break
   
cam.release()
cv2.destroyAllWindows()