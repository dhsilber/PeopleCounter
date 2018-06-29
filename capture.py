import numpy as np
import cv2 

cap = cv2.VideoCapture(1)

fourcc = cv2.cv.CV_FOURCC(*'XVID')
framesPerSecond = 20.0
out = cv2.VideoWriter( 'output.avi', fourcc, framesPerSecond, (640,480) )

while (True) :
  ret, frame = cap.read()

  if ret == True:
    out.write( frame )

    cv2.imshow( 'frame', frame )

    if cv2.waitKey(1) & 0xFF == ord( 'q' ):
      break

  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()

