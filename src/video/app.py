import cv2
import time

# create an object with the method that triggers a video capture object
# param 0 means (index 0)it will use the webcam on the computer but you put also a path
video = cv2.VideoCapture(0)

# number of frame
f = 0

while True:
    f = f+1
    # "check" is used to check if the video is running or not
    # "frame" is a numpy array
    check, frame = video.read()

    print(check)
    print(frame)

    # converting the frame so the color frame in a gray imag
    gray_color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Wait a certain amount of time before executing the next line
    # time.sleep(3)

    # show a window
    cv2.imshow("Capturing", gray_color)

    # wait time in millisecond
    key = cv2.waitKey(1)
    # if the button key is pressed break
    if key == ord('q'):
        break
print(f)
# access my object video
video.release()

# distroy a window
cv2.destroyAllWindows
