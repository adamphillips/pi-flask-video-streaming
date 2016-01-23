import cv2
import pdb
import numpy as np
from face_detector import FaceDetector
from null_gopigo import gopigo
import time

class ImageProcessor:
  def __init__(self):
    gopigo.set_speed(50)
    gopigo.stop
    self._face_detector = FaceDetector('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
    self.sizes_calculated = False
    self.image_height = None
    self.image_width = None
    self.segment_width = None

  def faces(self, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return self._face_detector.detect(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))

  def calculate_sizes(self, image):
    (self.height, self.width) = image.shape[:2]
    self.segment_width = self.width / 3
    self.sizes_calculated = True

  def process(self, stream):
    start_time = time.time()
    image = cv2.imdecode(np.fromstring(stream.getvalue(), dtype=np.uint8), 1)

    if(self.sizes_calculated == False):
      self.calculate_sizes(image)

    segment_width = self.segment_width

    cv2.line(image, (segment_width, 0), (segment_width, self.height), (255, 0, 0), 1)
    cv2.line(image, (2 * segment_width, 0), (2 * segment_width, self.height), (255, 0, 0), 1)

    faceRects = self.faces(image)
    for (x, y, w, h) in faceRects:
      cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if (len(faceRects) > 0):
      (x, y, w, h) = faceRects[0]
      self.move(x + (w/2), segment_width)
    else:
      print("no faces found")
      gopigo.stop()

    print(time.time() - start_time)

    return cv2.imencode('.jpg', image)[1].tostring()

  def move(self, horiz_x, segment_width):
    mid_point = segment_width * 1.5
    offset = horiz_x - mid_point
    print(offset)
    if(offset > segment_width):
      gopigo.set_speed(10)
      gopigo.right_rot()
    elif(offset < - segment_width):
      gopigo.set_speed(10)
      gopigo.left_rot()
    else:
      gopigo.set_speed(50)
      gopigo.fwd()

