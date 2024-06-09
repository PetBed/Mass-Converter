import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    # cv.imshow('Video', frame)
    # if cv.waitKey(20) & 0xFF == ord('d'):
    #     break
    
    #wait 20 miliseconds using cv.waitKey(20) and close window when clicking d using 0xFF == ord('d')
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()