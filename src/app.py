import cv2

# reading the cascade in python with opencv
# create a cascade classifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# loading the image
img = cv2.imread("news.jpg")

# convert the image from BGR(Blue, green, red) to a grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# returning the coordinates of the face in the image
faces = face_cascade.detectMultiScale(
    gray_img, scaleFactor=1.1, minNeighbors=5)

# drawing the rectangle to the image
for x, y, w, h in faces:
    '''
    @param x&y and are the coordinate of the face array (the top left corner point)
    @param w(width) and h(height) this the right corner point
    @param the color you want to give to the rectangle 
    @param the width of the line of the rectangle
    '''
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)


print(type(faces))  # class 'numpy.ndarray
print(faces)

# resize the image as you might have an image bigger than your screen resolution
resized_img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

# display the image
cv2.imshow("Gray Image", resized_img)
# the waiting time
cv2.waitKey(0)
# to destroy the window
cv2.destroyAllWindows()
