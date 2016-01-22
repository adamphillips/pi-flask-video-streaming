import cv2
import pdb
import numpy as np

class ImageProcessor(object):

  def process(self, stream):
    image = cv2.imdecode(np.fromstring(stream.getvalue(), dtype=np.uint8), 1)

    # draw a test rectangle
    # cv2.rectangle(image, (10, 400), (300, 300), (0, 255, 0), 1)
    # draw a test square
    # image[10:20, 10:20] = (255, 0, 0)

    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.equalizeHist(image)

    lap = cv2.Laplacian(image, cv2.CV_64F)
    image = np.uint8(np.absolute(lap))

    image = cv2.Canny(image, 30, 150)

    return cv2.imencode('.jpg', image)[1].tostring()


