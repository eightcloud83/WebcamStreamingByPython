import RunCamera;
import RunFlask;
camera=None
flaskapp=None

def Init():
    global camera
    global flaskapp
    camera=RunCamera.RunCamera()
    flaskapp=RunFlask.Init()
