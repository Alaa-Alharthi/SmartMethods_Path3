import cv2

image = cv2.imread('pic.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.namedWindow('orignal', cv2.WINDOW_NORMAL)
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)


cv2.imshow('orignal', image)
cv2.imshow('gray', gray)


cv2.waitKey(0)
cv2.destroyAllWindows()