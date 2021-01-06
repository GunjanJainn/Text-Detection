# OCR using pytesseract

import cv2
import pytesseract 

pytesseract.tesseract_cmd= r"E:\\AnacondaPython\\tesseract.exe"
def ocr_core(image):
     text= pytesseract.image_to_string(image )
     return text

img= cv2.imread("F:\sampletext.png")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sharp= cv2.medianBlur(gray, 5)
thresh= cv2.threshold(sharp, 0, 255, cv2.THRESH_BINARY)
textt= ocr_core(sharp)
print(textt)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()