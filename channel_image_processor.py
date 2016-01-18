import cv2
import pdb
import numpy as np

class ImageProcessor(object):

  def prepare_channel(self, B, G, R, new_dims):
    inter = cv2.INTER_AREA

    return cv2.resize(cv2.merge([B, G, R]), new_dims, interpolation = inter) 

  def process(self, stream):
    data = cv2.imdecode(np.fromstring(stream.getvalue(), dtype=np.uint8), 1)

    (orig_h, orig_w) = data.shape[:2]
    new_h = orig_h / 2
    new_w = orig_w / 2

    new_dims = (new_w, new_h)

    # draw a test rectangle
    cv2.rectangle(data, (10, 400), (300, 300), (0, 255, 0), 1)
    # draw a test square
    data[10:20, 10:20] = (255, 0, 0)
    (B, G, R) = cv2.split(data)

    zeros = np.zeros(data.shape[:2], dtype = "uint8")
    Brz = self.prepare_channel(B, zeros, zeros, new_dims)
    Grz = self.prepare_channel(zeros, G, zeros, new_dims)
    Rrz = self.prepare_channel(zeros, zeros, R, new_dims)
    Orz = self.prepare_channel(B, G, R, new_dims)

    row1 = np.concatenate((Orz, Rrz), axis = 1)
    row2 = np.concatenate((Brz, Grz), axis = 1)

    data = np.concatenate((row1, row2), axis = 0)

    return cv2.imencode('.jpg', data)[1].tostring()


