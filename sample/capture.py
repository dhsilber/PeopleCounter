import numpy as np
import cv2 
import time
import datetime

directory = '/tmp'
#height = 480
height = 1080
#width = 640
width = 1920

# tall = 480
# wide = 640
#tall = 240
#wide = 320
tall = 120
wide = 160
#tall = 215
#wide = 383

h1 = height / 2 - tall / 2
h2 = height / 2 + tall / 2
w1 = width  / 2 - wide / 2
w2 = width  / 2 + wide / 2



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
    out = cv2.VideoWriter( filename, fourcc, framesPerSecond, (w2 - w1, h2 - h1) )
    print ( filename )
    while time.time() < endtime :
#      cropped = frame[ 440 : 640 , 820 : 1100 ]
      cropped = frame[ h1 : h2, w1 : w2 ]
      cv2.imshow( 'frame', cropped )
      out.write( cropped )

#      cv2.imshow( 'frame', frame )
      ret, frame = cap.read()

      if cv2.waitKey(1) & 0xFF == ord( 'q' ):
        break

    out.release()
  else:
    break

cap.release()
cv2.destroyAllWindows()

