import numpy as np
import cv2 

width = 1920
height = 1080

cap = cv2.VideoCapture(1)
cap.set( 3, width )
cap.set( 4, height )

fourcc = cv2.cv.CV_FOURCC(*'XVID')
framesPerSecond = 20.0

cropper = 1

#out = cv2.VideoWriter( 'output.avi', fourcc, framesPerSecond, (width,height) )
out = cv2.VideoWriter( 'output.avi', fourcc, framesPerSecond, (width,height) )

while (True) :
  ret, frame = cap.read()
#  print frame.shape

  if ret == True:
    out.write( frame )

    h1 = max( 0, int( height - height * cropper ) )
    h2 = int( height * cropper )
    w1 = max( 0, int( width - width * cropper ) )
    w2 = int( width * cropper )
#    cropped = frame[ cropper : height * cropper, cropper : width * cropper ]
    cropped = frame[ h1 : h2, w1 : w2 ]

    cv2.imshow( 'frame', cropped )
    print cropped.shape
    print cropper

    key = cv2.waitKey(1) & 0Xff

    if key == ord( '+' ) or key == ord( '=' ):
      cropper += 0.05

    elif key == ord( '-' ):
      cropper -= 0.05

    elif key == ord( 'q' ):
      break

  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()

