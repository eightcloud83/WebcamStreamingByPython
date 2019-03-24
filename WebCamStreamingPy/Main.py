import G
import threading

G.Init()
t=threading.Thread(target=G.camera.tRun)
t.start()
G.flask.tRun()
