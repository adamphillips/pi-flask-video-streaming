from null_gopigo import gopigo

# Tests the gopigo null class
# None of these methods need to actually do anything, they just need
# to not error when called on a system that doesn't support GoPiGo.
# Therefore we just call each required method to check that it is defined.
class TestNullGopigo:
  def test_set_speed(self):
    gopigo.set_speed(50)

  def test_stop(self):
    gopigo.stop()

  def test_left_rot(self):
    gopigo.left_rot()

  def test_right_rot(self):
    gopigo.right_rot()

  def test_fwd(self):
    gopigo.fwd()
