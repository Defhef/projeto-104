import cv2 

img = cv2.imread(“solar-system.jpg”)

cv2.putText(img,"Sol", (100,80), cv2,FONT_HERESHEY_COMPLEX,2, (0,0,255))

cv2.putText(img,"Venus", (150,80), cv2,FONT_HERESHEY_COMPLEX,2, (0,0,155))

cv2.putText(img,"Marte", (150,80), cv2,FONT_HERESHEY_COMPLEX,2, (0,0,175))

cv2.putText(img,"Terra", (200,80), cv2,FONT_HERESHEY_COMPLEX,2, (0,0,200))


cv2.imwrite(“Solar_systemwithname.jpg”,img)

cv2.imshow(“resultado”,img)
cv2.waitKey(0)