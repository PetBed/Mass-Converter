import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('media/park.jpg')
dilated = cv.dilate(img, (7,7), iterations=3)
cv.imshow('Cat', dilated)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

gray_hist = cv.calcHist([gray], [0], None, [265], [0, 265])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)