class SegmentDetector():
  def __init__(self, image_width=None):
    self.image_width = image_width
    self.segment_width = self.image_width / 3
    self.left_cutoff = self.segment_width
    self.right_cutoff = self.image_width - self.segment_width

  def segment(self, position):
    if(position < self.left_cutoff):
      return 'left'
    elif(position > self.right_cutoff):
      return 'right'
    else:
      return 'centre'

