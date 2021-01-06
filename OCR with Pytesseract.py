#OCR boxes

import cv2
import pytesseract as pyt
import numpy as np

#Adding path for pytesseract
pyt.tesseract_cmd= r"E:\AnacondaPython\tesseract.exe"
#Read the image
img= cv2.imread("F:\sampletext.png")
img1= np.copy(img)   #copy of original image
#grayscaling 
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Finding width and height of the image
hImg, wImg, _= img.shape

#Finding each Character
boxes= pyt.image_to_boxes(gray)
for b in boxes.splitlines():
    b= b.split(" ")       #splits the array and converts in string
    print (b)
    #Find which coloumn contains which information
    x, y, w, h= int(b[1]), int(b[2]), int(b[3]), int( b[4])
    #making a rectangle around each charcter
    img= cv2.rectangle(img, (x, hImg-y), (w, hImg- h), (0,0,255) , 2)
    img= cv2.putText(img, b[0], (x, hImg-y+ 20), 
                     cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,50), 2)

#Finding words

boxes= pyt.image_to_data(gray)
for x, aa in enumerate(boxes.splitlines()):
    aa= aa.split()
    print (aa)
    if x!=0:               #x is the counter
        if len(aa)==12:    #array contains 12 columns if a word is found
            
            x, y, w, h= int(aa[6]), int(aa[7]),int(aa[8]), int( aa[9])
            img1= cv2.rectangle(img1, (x, y), (x+w, y+ h), (0,0,255) , 2)
            img1= cv2.putText(img1, aa[11], (x, y), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,50), 2)


cv2.imshow("Image", img)
cv2.imshow("Words", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
    