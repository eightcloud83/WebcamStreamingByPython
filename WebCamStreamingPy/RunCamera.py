import threading
import cv2
import sys
from time import sleep

class RunCamera(object):
    def __init__(T):
        T.lock=threading.Lock()
        T.event=threading.Event()
        T.video = cv2.VideoCapture(0)
        T.frame=None
        T.frameid=0
        T.video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        T.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    def __del__(self):
        self.video.release()
    def get_frame(T,wfid):
        if wfid==T.frameid:
            T.event.wait()
            T.event.clear()
        T.lock.acquire()
        frame=T.frame
        fid=T.frameid
        T.lock.release()
        return fid,frame
    def tRun(T):
        while True:
            sleep(0.1)
            success, image = T.video.read()
            ret, jpeg = cv2.imencode('.jpg', image)
            T.lock.acquire()
            T.frameid+=1
            T.frame=jpeg.tobytes()
            T.event.set()
            T.lock.release()
        return



