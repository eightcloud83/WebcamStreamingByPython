import threading
import cv2
import sys
from time import sleep

class RunCamera(object):
    def __init__(T):
        T.lock=threading.Lock()
        T.event=threading.Event()
        T.video = cv2.VideoCapture(0)
        T.frameI=None
        T.frameP=None
        T.frameidI=-1
        T.frameidP=-1
        T.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        T.video.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
    def __del__(self):
        self.video.release()
    def get_frameP(T,wfid):
        if wfid==T.frameidI:
            T.event.wait()
            T.event.clear()
        T.lock.acquire()
        fid=T.frameidI
        if T.frameidP==fid:
            frameP=T.frameP
        else:
            frame=cv2.resize(T.frameI,(320,180))
            ret, jpg = cv2.imencode('.jpg', frame)
            frameP=jpg.tobytes()
            T.frameP=frameP
            T.frameidP=fid
        T.lock.release()
        return fid,frameP
    def tRun(T):
        while True:
            success, image = T.video.read()
            T.lock.acquire()
            T.frameidI+=1
            T.frameI=image;
            T.event.set()
            T.lock.release()
        return



