import cv2
import pdb
import numpy as np
from face_detector import FaceDetector

class ImageProcessor(object):

  def process(self, stream):
    image = cv2.imdecode(np.fromstring(stream.getvalue(), dtype=np.uint8), 1)

    fd = FaceDetector('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
    # draw a test rectangle
    # cv2.rectangle(image, (10, 400), (300, 300), (0, 255, 0), 1)
    # draw a test square
    # image[10:20, 10:20] = (255, 0, 0)

    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.equalizeHist(image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    for (x, y, w, h) in faceRects:
      cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

   # image = gray

    return cv2.imencode('.jpg', image)[1].tostring()


