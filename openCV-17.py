import cv2
import face_recognition as FR
font =cv2.FONT_HERSHEY_SIMPLEX

donFace=FR.load_image_file("C:/Users/Emil Nilsen/Documents/Python/demoImages/known/Donald Trump.jpg")
faceLoc=FR.face_locations(donFace)[0]
donFaceEncode=FR.face_encodings(donFace)[0]

nancyFace=FR.load_image_file("C:/Users/Emil Nilsen/Documents/Python/demoImages/known/Nancy Pelosi.jpg")
faceLoc=FR.face_locations(nancyFace)[0]
nancyFaceEncode=FR.face_encodings(nancyFace)[0]

mikeFace=FR.load_image_file("C:/Users/Emil Nilsen/Documents/Python/demoImages/known/Mike Pence.jpg")
faceLoc=FR.face_locations(mikeFace)[0]
mikeFaceEncode=FR.face_encodings(mikeFace)[0]

knownEncodings=[donFaceEncode,nancyFaceEncode,mikeFaceEncode]
names=["Donald Trump","Nancy Pelosi","Mike Pence"]

unknownFace = FR.load_image_file("C:/Users/Emil Nilsen/Documents/Python/demoImages/unknown/u7.jpg")
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknownFace)
unknownEncodings=FR.face_encodings(unknownFace,faceLocations)

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left=faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name = "unknown Person"

    matches = FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex=matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name = names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top-10),font,1,(0,0,255),2)
cv2.imshow("My Faces",unknownFaceBGR)

cv2.waitKey(15000) 