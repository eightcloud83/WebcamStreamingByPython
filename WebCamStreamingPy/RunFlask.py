
from flask import Flask, render_template, Response
import G
import threading

app = Flask(__name__)

class RunFlask(object):
    def __init__(T):
        global app
        T.app=app

    def  tRun(T):
        T.app.run(host="0.0.0.0",port=5000)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    wfid=0
    while True:
        wfid,frame = camera.get_frameP(wfid)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(G.camera), mimetype='multipart/x-mixed-replace; boundary=frame')

def Init():
    global app;
    return app;
