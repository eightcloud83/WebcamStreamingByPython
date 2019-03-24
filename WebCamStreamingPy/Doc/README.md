# WebcamStreamingByPython
<pre>
based on http://www.chioka.in/python-live-video-streaming-example/
use "multipart/x-mixed-replace" protocol, 
     not supported by IE.
     https://en.wikipedia.org/wiki/MIME#Mixed-Replace
add multithreading (event, lock), 
   seperate cv2.viedo.read() from web's response thread,
   let multiple http connections share data of cv2's reading.

feature-branch-save-compresed-video-manually (implmenting)
   (preview-low-resolution web-video-streaming)
   (save-hight-resolution compressed-video)

feature-branch-save-compresed-video-by-opencv-detecting-object-move (plan)


</pre>
