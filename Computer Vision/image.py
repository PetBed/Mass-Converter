import cv2 as cv

img = cv.imread('media/park.jpg')
# canny = cv.Canny()
dilated = cv.dilate(img, (7,7), iterations=3)
cv.imshow('Cat', dilated)


cv.waitKey(0)
# updating = True

# # def close():
# #     updating = False

# vid = cv.VideoCapture(0)
# # cv.createButton("Back", close, None, cv.QT_PUSH_BUTTON,1)

# while(updating):
#     ret, frame = vid.read()
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
    
# vid.release()
# cv.destroyAllWindows()