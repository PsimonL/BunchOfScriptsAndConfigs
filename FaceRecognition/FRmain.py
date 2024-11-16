from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)
capture = cv2.VideoCapture(0) # 0 value means webcam in usage

def captured_frames(): # camera frame
    while True:
        # serial.write(b'\x03')
        # key = cv2.waitKey(1)
        # if key == ord("q"):
        #     break
        success, frame = capture.read()
        if not success:
            break
        else: # https://github.com/opencv/opencv/tree/master
            face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
            eyes_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
            face = face_cascade.detectMultiScale(frame, 1.1, 7)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            for (x, y, width, height) in face:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0,0,255), 2) # BGR not RGB!
                # https://stackoverflow.com/questions/54727642/what-does-roi-gray-function-do-in-opencv
                roi_gray = gray[y : y + height, x : x + width]
                roi_color = frame[y : y + height, x : x + width]
                eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 3)
                for (ex, ey, ewidth, eheight) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ewidth, ey + eheight), (0, 255,0), 2)
            returnn, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # no return here, cause catching only 1 frame, no loop
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    capture.release()
    cv2.destroyAllWindows()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video")
def video():
    # https://blog.miguelgrinberg.com/post/video-streaming-with-flask/page/8
    return Response(captured_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True, port=80)
