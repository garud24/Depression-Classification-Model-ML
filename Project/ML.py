from flask import Flask
from flask import render_template
from flask import Response
from flask import url_for 
from flask import redirect


import cv2

from imutils.video import VideoStream
import imutils
#import time

app = Flask(__name__)
videoStream = VideoStream(src = 0).start()
#time.sleep(2.0)


@app.route("/")
def index():
    return render_template('videostream.html')

@app.route("/video", methods=["POST", "GET"])
def video():
    return Response(generateFrames(), mimetype='multipart/x-mixed-replace; boundary= frame')

def generateFrames():
    while True:
        frame = videoStream.read()
        frame = imutils.resize(frame, width = 600)
        (flag, encodedImage) = cv2.imencode(".jpg",frame)  
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')  

if __name__ == '__main__':
    app.debug = True
    app.run()



     