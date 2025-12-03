import os #you dont have to put these
os.environ["QT_QPA_PLATFORM"] = "xcb" #you dont have to put these
import time
import  cv2

video = cv2.VideoCapture(0) # 0 of you are using your computer or laptop camera and 1 if external
time.sleep(1) ## it will negate the black color in the starting and help the camera load

while True:
    check,frame = video.read()
    cv2.imshow("My Video",frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
video.release()





