import G
import threading
import RunFlask

G.Init()
t=threading.Thread(target=G.camera.tRun)
t.start()
RunFlask.tRun()

