# PeopleCounter

The goal of this project is to be able to count people who stop near an informative display and also track how long they stay near it.
This is for a museum to be able to quantify which signs attract attention. No attempt is being made to identify people.


To date (2018-06-29) most of what I've been doing is not really software development, but rather hacking around with the OpenCV library and learning the technology. My next step is to record video under the conditions with which I'll be counting people.

detect.py comes mostly from https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/ and is really just for playing with the pedestrian detection capabilities of OpenCV.

capture.py comes mostly from a docs.opencv.org example, except that VideoWriter_fourcc() does not exist in OpenCV 2.4. I had to dig around for an older example to find that cv2.cv.CV_FOURCC() is the equivalent.

Adrian Rosebrook's blog at https://www.pyimagesearch.com/ is very useful.
