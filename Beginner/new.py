import cv2

img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resize_image=cv2.resize(img,(900,600))
cv2.imshow("galaxy",resize_image)
cv2.waitKey(4000)
cv2.destroyAllWindows()