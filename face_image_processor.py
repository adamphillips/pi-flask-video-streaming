import cv2
import pdb
import numpy as np
from face_detector import FaceDetector
from gopigo import gopigo

class ImageProcessor:
  def __init__(self):
    gopigo.set_speed(50)
    gopigo.stop
    print 'inited'

  def process(self, stream):
    image = cv2.imdecode(np.fromstring(stream.getvalue(), dtype=np.uint8), 1)

    (height, width) = image.shape[:2]
    quadrant_width = width / 4

    cv2.line(image, (quadrant_width, 0), (quadrant_width, height), (255, 0, 0), 1)
    cv2.line(image, (3 * quadrant_width, 0), (3 * quadrant_width, height), (255, 0, 0), 1)

    fd = FaceDetector('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #pdb.set_trace()
    faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    for (x, y, w, h) in faceRects:
      cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if (len(faceRects) > 0):
      (x, y, w, h) = faceRects[0]
      self.move(x + (w/2), quadrant_width)
    else:
      print("no faces found")
      gopigo.stop()
    # image = gray

    return cv2.imencode('.jpg', image)[1].tostring()

  def move(self, horiz_x, quadrant_width):
    mid_point = quadrant_width * 2
    offset = horiz_x - mid_point
    print(offset)
    if(offset > quadrant_width):
      print("right")
      gopigo.set_speed(10)
      gopigo.right_rot()
      #sleep(0.1)
    elif(offset < - quadrant_width):
      gopigo.set_speed(10)
      print("left")
      gopigo.left_rot()
      #sleep(0.1)
    else:
      gopigo.set_speed(50)
      print("fwd")
      gopigo.fwd()

