import cv2
import glob

# glob returning a list of a paths of matching a pathname pattern
images = glob.glob("*.jpg")

for image in images:
    # loading the images
    img = cv2.imread(image, 0)
    # resize the images
    resize = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", resize)  # displaying the image
    # set time for window to be closed
    cv2.waitKey(500)
    cv2.destroyAllWindows()  # so we want to distroy all windows
    # save the image with the word 'resized' as first name then follow by the image name
    cv2.imwrite("resized_"+image, resize)
