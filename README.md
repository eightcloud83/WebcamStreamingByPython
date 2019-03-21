# WebcamStreamingByPython
<pre>
based on http://www.chioka.in/python-live-video-streaming-example/
use "multipart/x-mixed-replace" protocol, 
     not supported by IE.
     https://en.wikipedia.org/wiki/MIME#Mixed-Replace
add multithreading (event, lock), 
   seperate cv2.viedo.read() from web's response thread,
   let multiple http connections share data of cv2's reading.
</pre>
