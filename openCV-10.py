import numpy as np
import cv2

x = np.zeros([256,720,3],dtype=np.uint8)

for row in range(0,256,1):
    for column in range(0,720,1):
        x[row][column] = (int(column/4),row,255)

x=cv2.cvtColor(x,cv2.COLOR_HSV2BGR)

y = np.zeros([256,720,3],dtype=np.uint8)

for row in range(0,256,1):
    for column in range(0,720,1):
        y[row][column] = (int(column/4),255,row)

y=cv2.cvtColor(y,cv2.COLOR_HSV2BGR)
        

while True:
    cv2.imshow("my HSV",x)
    cv2.moveWindow("my HSV",0,0)
    cv2.imshow("my HSV2",y)
    cv2.moveWindow("my HSV2",0,row+30)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cv2.destroyAllWindows()