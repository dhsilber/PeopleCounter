import numpy as np
import cv2 
import time
import datetime

directory = '/tmp'
height = 480
width = 640

cap = cv2.VideoCapture(1)
cap.set( 3, width )
cap.set( 4, height )

fourcc = cv2.cv.CV_FOURCC(*'XVID')
framesPerSecond = 20.0


seconds = 10
#fps = 60
fps = 30
progress_data = []
progress_data.append( seconds )
#progress_data.append( fps )
def progression ( data = progress_data ) :
#  fps = data[ 1 ] - 10
#  if fps <= 0:
#    fps = 60
  data[0] = data[0] * 2
#  data[1] = fps
  return ( data )


while (True) :
  ret, frame = cap.read()

  if ret == True:
    data = progression()
    seconds = data[0]
    endtime = time.time() + seconds
#    framesPerSecond = data[1]
    framesPerSecond = 30
    now = datetime.datetime.now()
    filename = '{}/{}_{}_seconds_{}_fps.avi'.format( directory, now.isoformat(), seconds, framesPerSecond )
    out = cv2.VideoWriter( filename, fourcc, framesPerSecond, (width,height) )
    print ( filename )
    while time.time() < endtime :
      out.write( frame )

#      cv2.imshow( 'frame', frame )
      ret, frame = cap.read()

      if cv2.waitKey(1) & 0xFF == ord( 'q' ):
        break

    out.release()
  else:
    break

cap.release()
cv2.destroyAllWindows()

