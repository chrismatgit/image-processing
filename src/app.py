import cv2

# loading the image
img = cv2.imread("galaxy.jpg", 0)
print(type(img))  # to know the type
print(img)
print(img.shape)  # to check the values in the vertical direction
print(img.ndim)  # to check the dimension

# resize the image
# in order to keep the ration let me divide the shape by 2
resesized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
# displaying the image
cv2.imshow("Galaxy", resesized_image)
# write an image into a file
cv2.imwrite("Galaxy_resized_img.jpg", resesized_image)
# set time for window to be closed
# but if we put zero the window will stay until we press a button
cv2.waitKey(0)
# so we want to distroy all windows
cv2.destroyAllWindows()
