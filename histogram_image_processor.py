import cv2
import pdb
import numpy as np

class ImageProcessor(object):

  def process(self, stream):
    data = cv2.imdecode(np.fromstring(stream.getvalue(), dtype=np.uint8), 1)

    # draw a test rectangle
    cv2.rectangle(data, (10, 400), (300, 300), (0, 255, 0), 1)
    # draw a test square
    data[10:20, 10:20] = (255, 0, 0)

    data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    data = cv2.equalizeHist(data)

    return cv2.imencode('.jpg', data)[1].tostring()


