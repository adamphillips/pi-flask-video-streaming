class gopigo:
  @classmethod
  def log(cls, value):
    print('GoPiGo: ' + value)

  @classmethod
  def set_speed(cls, value):
    cls.log('Speed set to ' + str(value))

  @classmethod
  def stop(cls):
    cls.log('Stopped')

  @classmethod
  def left_rot(cls):
    cls.log('Rotated left')

  @classmethod
  def right_rot(cls):
    cls.log('Rotated right')

  @classmethod
  def fwd(cls):
    cls.log('Forward')
