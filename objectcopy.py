import cv2
img=cv2.imread("squirrel.png", -1)
print(img.shape)
roi=img[200:500, 150:300]
print(roi.shape)
img2=img.copy()

img2[:roi.shape[0], :roi.shape[1]]=roi

cv2.imshow('img', img)
cv2.imshow('roi', roi)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()