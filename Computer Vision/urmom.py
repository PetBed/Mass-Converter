import cv2 as cv

count = 1
name = "1"
while(count < 250):
    img = cv.imread('media/cat.png')
    cv.imshow(name, img)
    count = count + 1
    name = '"' + str(count) + '"'
cv.waitKey(0)