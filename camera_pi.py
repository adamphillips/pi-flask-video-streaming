import time
import io
import threading
import picamera
import picamera.array
import cv2
import pdb
import numpy as np

class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (640, 480)
            camera.hflip = True
            camera.vflip = True
            camera.framerate = 12
            camera.brightness = 80
            camera.contrast = 30

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                stream.seek(0)

                data = cv2.imdecode(np.fromstring(stream.getvalue(), dtype=np.uint8), 1)
                #draw a test rectangle
                cv2.rectangle(data, (10, 400), (300, 300), (0, 255, 0), 2)
                frame = cv2.imencode('.jpg', data)[1].tostring()

                cls.frame = frame

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - cls.last_access > 10:
                    break
        cls.thread = None
