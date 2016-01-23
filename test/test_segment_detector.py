from segment_detector import SegmentDetector

class TestSegmentDetector():
  def setup_class(self):
    self.subject = SegmentDetector(image_width=300)

  def test_left(self):
    assert self.subject.segment(20) == 'left'

  def test_right(self):
    assert self.subject.segment(250) == 'right'

  def test_centre(self):
    assert self.subject.segment(150) == 'centre'


